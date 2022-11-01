from http.client import CONFLICT
import numpy
import dataLoader
from model.business.tableFactory import constructClassTable
from model.constraints.entity.allocatedTeacher import AllocatedTeacher

CONFLICT_PENALTY = 1000
THREE_CONSECUTIVE_BLOCKS_PENALTY = 30
AVAILABILITY_PENALTY = 10

def calculatePenalties(timeTablesDict): #recebe dicionario[dataClass] = tabela horária de cada turma (dataClass)
    penaltiesTablesDict = {} #retorna dicionario[dataClass] = tabela de penalidades de cada turma (dataClass)
    penaltiesTotalValue = 0 

    allocatedTeachers = __returnEmptyAllocationsTeachersDict()
    blocks = dataLoader.getBlocksCopy()

    #para cada timeTable de cada turma
    for dataClass, timeTable in timeTablesDict.items():
        penaltiesTablesDict[dataClass] = constructClassTable(0)
        penaltyTable = penaltiesTablesDict[dataClass]

        #VERIFICACAO DE DISCIPLINA COM 3 BLOCOS SEGUIDOS NO MESMO DIA
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
                    penaltiesTotalValue += THREE_CONSECUTIVE_BLOCKS_PENALTY

        #para cada bloco de cada do timeTable da turma
        for indexesPair, blockAllocation in numpy.ndenumerate(timeTable):
            if(blockAllocation == None):
                continue #pula a iteração atual
            block = blocks[blockAllocation]
            teacher = block.teacher
            teacherName = teacher.name
            allocatedTeacher = allocatedTeachers[teacherName]
            allocationTable = allocatedTeacher.allocationsTables[block.classData.shift]
            
            # VERIFICACAO DE CONFLITO
            if (allocationTable[indexesPair[0]][indexesPair[1]] != None):  #conflito: horário já alocado para o professor!
                penaltyTable[indexesPair[0]][indexesPair[1]] += CONFLICT_PENALTY
                penaltiesTotalValue += CONFLICT_PENALTY
            else:
                allocationTable[indexesPair[0]][indexesPair[1]] = block
            
            # VERIFICACAO DE ALOCACAO FORA DA DISPONIBILIDADE DO PROFESSOR
            dayOfWeekAllocated = indexesPair[1]
            if (dayOfWeekAllocated not in teacher.getAvailabilitiesCopy()):
                print(teacherName)
                print(dayOfWeekAllocated)
                penaltyTable[indexesPair[0]][indexesPair[1]] += AVAILABILITY_PENALTY
                penaltiesTotalValue += AVAILABILITY_PENALTY
    
    print(penaltiesTablesDict)
    print(penaltiesTotalValue)

    return penaltiesTablesDict, penaltiesTotalValue


def __returnEmptyAllocationsTeachersDict():
    empytAllocatedTeachers = {}
    teachers =  dataLoader.getTeachersCopy()
    for teacherName, teacher in teachers.items():
        empytAllocatedTeachers[teacher.name] = AllocatedTeacher(teacherName, teacher.getAvailabilitiesCopy())
    return empytAllocatedTeachers