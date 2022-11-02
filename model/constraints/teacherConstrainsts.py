from http.client import CONFLICT
from math import ceil
import numpy
import dataLoader
from model.business.tableFactory import constructClassTable
from model.constraints.entity.allocatedTeacher import AllocatedTeacher
from model.utils.shifts import NUMBER_OF_BLOCKS_IN_SHIFT

CONFLICT_PENALTY = 1000000
THREE_CONSECUTIVE_BLOCKS_PENALTY = 300
AVAILABILITY_PENALTY = 100
SPARSE_DAYS_PENALTY = 2

def calculatePenalties(timeTablesDict): #recebe dicionario[dataClass] = tabela horária de cada turma (dataClass)
    penaltiesTablesDict = {} #retorna dicionario[dataClass] = tabela de penalidades de cada turma (dataClass)
    penaltiesTotalValue = 0 

    allocatedTeachers = __returnEmptyAllocationsTeachersDict()
    blocks = dataLoader.getBlocksCopy()

    #para cada timeTable de cada turma
    for dataClass, timeTable in timeTablesDict.items():
        penaltiesTablesDict[dataClass] = constructClassTable(0)
        penaltyTable = penaltiesTablesDict[dataClass]

        penaltiesTotalValue += __returnConsecutivesThreeBlocksPenalty(blocks, timeTable, penaltyTable)

        #para cada bloco de cada do timeTable da turma
        for indexesPair, blockAllocation in numpy.ndenumerate(timeTable):
            if(blockAllocation == None):
                continue #pula a iteração atual
            block = blocks[blockAllocation]
            teacher = block.teacher
            teacherName = teacher.name
            allocatedTeacher = allocatedTeachers[teacherName]
            allocationTable = allocatedTeacher.allocationsTables[block.classData.shift]
            
            penaltiesTotalValue += __returnConflictPenalty(penaltyTable, indexesPair, block, allocationTable)
            penaltiesTotalValue += __returnUnavailableDayPenalty(penaltyTable, indexesPair, teacher, teacherName)
    
    #para cada professor alocado
    penaltiesTotalValue += __returnSparseDaysPenalty(penaltyTable, allocatedTeachers) 
        
    print(penaltiesTablesDict)
    print(penaltiesTotalValue)

    return penaltiesTablesDict, penaltiesTotalValue

#VERIFICA SE A DISTRIBUIÇÃO DE ALOCAÇÕES SE ESPALHOU POR MUITOS DIAS PARA O PROFESSOR
def __returnSparseDaysPenalty(penaltyTable, allocatedTeachers):
    #para cada professor alocado
    for teacherName, allocatedTeacher in allocatedTeachers.items():
        concatenatedAllocationTable = __concatenateShiftsAllocationTables(allocatedTeacher)
        numberOfBlocksAllocated = numpy.where(concatenatedAllocationTable != None, 1, 0).sum() 
        daysOfWeekAllocatedBoolean = ~numpy.all(concatenatedAllocationTable == None, axis = 0)
        numberOfDaysAllocated = daysOfWeekAllocatedBoolean.sum()
        if numberOfDaysAllocated <= ceil(numberOfBlocksAllocated/len(concatenatedAllocationTable)):
            return 0  #número de dias alocado já é mínimo, portanto não há penalidade
        daysOfWeekAllocated = numpy.where(daysOfWeekAllocatedBoolean == True)[0]
        firstDayAllocated = daysOfWeekAllocated[0]
        lastDayAllocated = daysOfWeekAllocated[-1] #em python, indice -1 retorna o ultimo elemento

        print(teacherName)
        print(daysOfWeekAllocated)
        print(firstDayAllocated)
        print(lastDayAllocated)

#Concatena as tabelas de alocação por turno
def __concatenateShiftsAllocationTables(allocatedTeacher):
    returnConcatenedTable = None
    #Para cada turno
    for shift, allocationTableByShift in allocatedTeacher.allocationsTables.items():
        if (numpy.array(allocationTableByShift) == None).all():  #Se não há alocação no turno, não concatena a tabela
            continue
        if returnConcatenedTable is None:
            returnConcatenedTable = allocationTableByShift
        else:
            returnConcatenedTable = numpy.concatenate((returnConcatenedTable, allocationTableByShift), axis=0) #axis=0 -> conc. vertical
    return numpy.array(returnConcatenedTable)

#VERIFICACAO DE DISCIPLINA COM 3 BLOCOS SEGUIDOS NO MESMO TURNO
def __returnConsecutivesThreeBlocksPenalty(blocks, timeTable, penaltyTable):
    penaltiesLocalValue = 0
    for dayOfWeek in range(5):
        if((timeTable[0][dayOfWeek] != None) and (timeTable[1][dayOfWeek] != None) and (timeTable[2][dayOfWeek] != None)):
            firstBlockIndex =  timeTable[0][dayOfWeek]
            firstCurricularComponentName = blocks[firstBlockIndex].curricularComponentName
            secondBlockIndex = timeTable[1][dayOfWeek]
            secondCurricularComponentName = blocks[secondBlockIndex].curricularComponentName
            thirdBlockIndex = timeTable[2][dayOfWeek]
            thirdCurricularComponentName = blocks[thirdBlockIndex].curricularComponentName
            if(firstCurricularComponentName == secondCurricularComponentName == thirdCurricularComponentName):
                    #disciplina de 3 blocos está no mesmo dia
                penaltyTable[0][dayOfWeek] += THREE_CONSECUTIVE_BLOCKS_PENALTY//2 #trunca o resultado
                penaltyTable[2][dayOfWeek] += THREE_CONSECUTIVE_BLOCKS_PENALTY//2
                penaltiesLocalValue += THREE_CONSECUTIVE_BLOCKS_PENALTY
    return penaltiesLocalValue

# VERIFICACAO DE CONFLITO e ATUALIZA TABELA DE ALOCACAO DO PROFESSOR
def __returnConflictPenalty(penaltyTable, indexesPair, block, allocationTable):
    if (allocationTable[indexesPair[0]][indexesPair[1]] != None):  #conflito: horário já alocado para o professor!
        penaltyTable[indexesPair[0]][indexesPair[1]] += CONFLICT_PENALTY
        return CONFLICT_PENALTY
    else: #aloca bloco na allocationTable do professor
        allocationTable[indexesPair[0]][indexesPair[1]] = block
        return 0

# VERIFICACAO DE ALOCACAO FORA DA DISPONIBILIDADE DO PROFESSOR
def __returnUnavailableDayPenalty(penaltyTable, indexesPair, teacher, teacherName):
    dayOfWeekAllocated = indexesPair[1]
    if (dayOfWeekAllocated in teacher.getAvailabilitiesCopy()):
        return 0    
    penaltyTable[indexesPair[0]][indexesPair[1]] += AVAILABILITY_PENALTY
    return AVAILABILITY_PENALTY



def __returnEmptyAllocationsTeachersDict():
    empytAllocatedTeachers = {}
    teachers =  dataLoader.getTeachersCopy()
    for teacherName, teacher in teachers.items():
        empytAllocatedTeachers[teacher.name] = AllocatedTeacher(teacherName, teacher.getAvailabilitiesCopy())
    return empytAllocatedTeachers