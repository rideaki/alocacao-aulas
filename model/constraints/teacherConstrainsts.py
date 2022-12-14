from math import ceil
import numpy
import model.loader.dataLoader as dataLoader
from model.business.tableFactory import constructClassTable
from model.constraints.entity.allocatedTeacher import AllocatedTeacher
from model.utils.shifts import NUMBER_OF_BLOCKS_IN_SHIFT

CONFLICT_PENALTY =        9999999999
AVAILABILITY_PENALTY =       3000000
CONSECUTIVE_BLOCKS_PENALTY = 2000000
SPARSE_DAYS_PENALTY =            100
SPARSE_HOURS_PENALTY =             1

def calculatePenalties(timeTablesDict): #recebe dicionario[classData] = tabela horária de cada turma (classData)
    penaltiesTablesDict = {} #retorna dicionario[classData] = tabela de penalidades de cada turma (classData)

    allocatedTeachers = __returnEmptyAllocatedTeachersDict()
    blocks = dataLoader.getBlocksCopy()

    hasPenalty = False
    #para cada timeTable de cada turma
    for classData, timeTable in timeTablesDict.items():
        penaltiesTablesDict[classData] = constructClassTable(0)
        penaltyTable = penaltiesTablesDict[classData]

        #para cada bloco do timeTable da turma
        for indexesPair, blockAllocation in numpy.ndenumerate(timeTable):
            if(blockAllocation == None):
                continue #pula para próximo bloco
            block = blocks[blockAllocation]
            teacher = block.teacher
            teacherName = teacher.name
            allocatedTeacher = allocatedTeachers[teacherName]
            allocationTable = allocatedTeacher.allocationsTables[block.classData.shift]
            if __hasConflict(penaltyTable, indexesPair, block, allocationTable):
                hasPenalty = True
                #break #sai do for de bloco e vai para próxima classData
            if __hasUnavailableDay(penaltyTable, indexesPair, teacher):
                hasPenalty = True
                #break #sai do for de bloco e vai para próxima classData
        if __hasConsecutivesBlocks(blocks, timeTable, penaltyTable):
            hasPenalty = True
            #continue #pula para próxima classData

    if not hasPenalty:
        __checkSparseDistribution(penaltiesTablesDict, allocatedTeachers)

    return penaltiesTablesDict, __penaltiesSum(penaltiesTablesDict)

#VERIFICA SE A DISTRIBUIÇÃO DE ALOCAÇÕES SE ESPALHOU POR MUITOS DIAS E HORÁRIOS PARA O PROFESSOR
def __checkSparseDistribution(penaltiesTablesDict, allocatedTeachers):
    #para cada professor alocado
    for allocatedTeacher in allocatedTeachers.values():
        concatenatedAllocationTable = __concatenateShiftsAllocationTables(allocatedTeacher)
        if(concatenatedAllocationTable is None):
            continue #professor não foi alocado, portanto não há penalidade. Pula para o próx. professor
        daysOfWeekAllocatedBoolean = ~numpy.all(concatenatedAllocationTable == None, axis = 0)
        __checkSparseDays(penaltiesTablesDict, concatenatedAllocationTable, daysOfWeekAllocatedBoolean)
        __checkSparseHours(penaltiesTablesDict, concatenatedAllocationTable, daysOfWeekAllocatedBoolean)

def __checkSparseHours(penaltiesTablesDict, concatenatedAllocationTable, daysOfWeekAllocatedBoolean):
    if not hasattr(daysOfWeekAllocatedBoolean, "__len__"):
        return # daysOfWeekAllocatedBoolean não é uma lista, professor não foi alocado
    for dayOfWeek in range(len(daysOfWeekAllocatedBoolean)):
        isAllocated = daysOfWeekAllocatedBoolean[dayOfWeek]
        if not isAllocated:
            continue #dia não alocado, pula proximo dia da semana
        hoursOfDay = concatenatedAllocationTable[:,dayOfWeek] #array que recebe a coluna do dia
        allocatedHoursIndexes = numpy.nonzero(hoursOfDay != None)[0]
        if (allocatedHoursIndexes is None) or len(allocatedHoursIndexes) <= 1:
            continue #não há alocacao no dia, há apenas uma aula. Pula para proximo dia
        firstAllocatedHourIndex = allocatedHoursIndexes[0]
        lastAllocatedHourIndex = allocatedHoursIndexes[-1]
        deltaAllocation = lastAllocatedHourIndex - firstAllocatedHourIndex + 1
        vacantHours = deltaAllocation - len(allocatedHoursIndexes)
        if vacantHours == 0:
            continue #não há horário vago, pula para próximo dia
        penalty = (vacantHours**2)*SPARSE_HOURS_PENALTY  

        firstAllocatedBlock = concatenatedAllocationTable[firstAllocatedHourIndex][dayOfWeek]
        firstClassData = firstAllocatedBlock.classData
        penaltiesTablesDict[firstClassData][firstAllocatedHourIndex % NUMBER_OF_BLOCKS_IN_SHIFT][dayOfWeek] += penalty/2

        lastAllocatedBlock = concatenatedAllocationTable[lastAllocatedHourIndex][dayOfWeek]
        lastClassData = lastAllocatedBlock.classData
        penaltiesTablesDict[lastClassData][lastAllocatedHourIndex % NUMBER_OF_BLOCKS_IN_SHIFT][dayOfWeek] += penalty/2

#VERIFICA SE A DISTRIBUIÇÃO DE ALOCAÇÕES SE ESPALHOU POR MUITOS DIAS PARA O PROFESSOR
def __checkSparseDays(penaltiesTablesDict, concatenatedAllocationTable, daysOfWeekAllocatedBoolean):
    numberOfBlocksAllocated = numpy.where(concatenatedAllocationTable != None, 1, 0).sum() 
    numberOfDaysAllocated = daysOfWeekAllocatedBoolean.sum()
    numberOfRowsInConcatenatedTable = 6 #len(concatenatedAllocationTable) #[:,0].size
    minDaysToBeAllocated = ceil(numberOfBlocksAllocated/numberOfRowsInConcatenatedTable)
    if (numberOfDaysAllocated <= minDaysToBeAllocated) or (
            numberOfDaysAllocated == 2 and numberOfBlocksAllocated == numberOfRowsInConcatenatedTable): #contem disciplinas com 3 blocos
        return #número de dias alocado já é mínimo, portanto não há penalidade.
    daysOfWeekAllocated = numpy.where(daysOfWeekAllocatedBoolean == True)[0]
        
    __applyPenaltiesOnFirstDay(penaltiesTablesDict, concatenatedAllocationTable, numberOfDaysAllocated, minDaysToBeAllocated, daysOfWeekAllocated)
    __applyPenaltiesOnLastDaty(penaltiesTablesDict, concatenatedAllocationTable, numberOfDaysAllocated, minDaysToBeAllocated, daysOfWeekAllocated)


#Aplica penalidades no primeiro dia esparco alocado
def __applyPenaltiesOnFirstDay(penaltiesTablesDict, concatenatedAllocationTable, numberOfDaysAllocated, minDaysToBeAllocated, daysOfWeekAllocated):
    firstDayAllocated = daysOfWeekAllocated[0]
    for index, block in enumerate(list(zip(*concatenatedAllocationTable))[firstDayAllocated]): # zip(*matrix) = transposed of matrix
        if block == None:
            continue
        penaltiesTablesDict[block.classData][index % NUMBER_OF_BLOCKS_IN_SHIFT][firstDayAllocated] += SPARSE_DAYS_PENALTY

#Aplica penalidades no ultimo dia esparco alocado
def __applyPenaltiesOnLastDaty(penaltiesTablesDict, concatenatedAllocationTable, numberOfDaysAllocated, minDaysToBeAllocated, daysOfWeekAllocated):
    lastDayAllocated = daysOfWeekAllocated[-1] #em python, indice -1 retorna o ultimo elemento
    for index, block in enumerate(list(zip(*concatenatedAllocationTable))[lastDayAllocated]): # zip(*matrix) = transposed of matrix
        if block == None:
            continue
        penaltiesTablesDict[block.classData][index % NUMBER_OF_BLOCKS_IN_SHIFT][lastDayAllocated] += SPARSE_DAYS_PENALTY

#Concatena as tabelas de alocação do verticalmente
def __concatenateShiftsAllocationTables(allocatedTeacher):
    concatenedTable = None
    #Para cada turno
    for shift, allocationTableByShift in allocatedTeacher.allocationsTables.items():
        if (numpy.array(allocationTableByShift) == None).all():  #Se não há alocação no turno, não concatena a tabela
            continue
        if concatenedTable is None:
            concatenedTable = allocationTableByShift
        else:
            concatenedTable = numpy.concatenate((concatenedTable, allocationTableByShift), axis=0) #axis=0 -> conc. vertical
    return numpy.array(concatenedTable)

#VERIFICACAO DE DISCIPLINA COM 3 BLOCOS SEGUIDOS DO MESMO PROFESSOR NO MESMO TURNO
def __hasConsecutivesBlocks(blocks, timeTable, penaltyTable):
    hasConsecutivesBlocks = False
    for dayOfWeek in range(5):
        if((timeTable[0][dayOfWeek] != None) and (timeTable[1][dayOfWeek] != None) and (timeTable[2][dayOfWeek] != None)):
            firstBlockIndex =  timeTable[0][dayOfWeek]
            firstTeacher = blocks[firstBlockIndex].teacher.name
            secondBlockIndex = timeTable[1][dayOfWeek]
            secondTeacher = blocks[secondBlockIndex].teacher.name
            thirdBlockIndex = timeTable[2][dayOfWeek]
            thirdTeacher = blocks[thirdBlockIndex].teacher.name
            if(firstTeacher == secondTeacher == thirdTeacher):
                #disciplina de 3 blocos está no mesmo dia
                penaltyTable[0][dayOfWeek] += CONSECUTIVE_BLOCKS_PENALTY/2 #marca penalidade na primeira aula do turno
                penaltyTable[2][dayOfWeek] += CONSECUTIVE_BLOCKS_PENALTY/2 #marca penalidade na u aula do turno
                hasConsecutivesBlocks = True
    return hasConsecutivesBlocks

# VERIFICACAO DE CONFLITO e ATUALIZA TABELA DE ALOCACAO DO PROFESSOR
def __hasConflict(penaltyTable, indexesPair, block, allocationTable):
    hasConflict = False
    if (allocationTable[indexesPair[0]][indexesPair[1]] != None):  #conflito: horário já alocado para o professor!
        penaltyTable[indexesPair[0]][indexesPair[1]] += CONFLICT_PENALTY
        hasConflict = True
    else: #aloca bloco na allocationTable do professor
        allocationTable[indexesPair[0]][indexesPair[1]] = block
    return hasConflict

# VERIFICACAO DE ALOCACAO FORA DA DISPONIBILIDADE DO PROFESSOR
def __hasUnavailableDay(penaltyTable, indexesPair, teacher):
    hasUnavailableDay = False
    dayOfWeekAllocated = indexesPair[1]
    if (dayOfWeekAllocated not in teacher.getAvailabilitiesCopy()):
        penaltyTable[indexesPair[0]][indexesPair[1]] += AVAILABILITY_PENALTY
        hasUnavailableDay = True
    return hasUnavailableDay

def __returnEmptyAllocatedTeachersDict():
    empytAllocatedTeachers = {}
    teachers =  dataLoader.getTeachersCopy()
    for teacherName, teacher in teachers.items():
        empytAllocatedTeachers[teacher.name] = AllocatedTeacher(teacherName, teacher.getAvailabilitiesCopy())
    return empytAllocatedTeachers

def __penaltiesSum(penaltiesTablesDict):
    penaltiesTotalValue = 0
    for timeTable in penaltiesTablesDict.values():
        penaltiesTotalValue += numpy.sum(timeTable)
    return penaltiesTotalValue
