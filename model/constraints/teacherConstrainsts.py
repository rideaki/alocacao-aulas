from http.client import CONFLICT
import numpy
import dataLoader
from model.business.tableFactory import constructClassTable
from model.constraints.entity.allocatedTeacher import AllocatedTeacher

CONFLICT_PENALTY = 1000
AVAILABILITY_PENALTY = 10

def calculatePenalties(timeTablesDict): #recebe dicionario[dataClass] = tabela horária de cada turma (dataClass)
    penaltiesTablesDict = {} #retorna dicionario[dataClass] = tabela de penalidades de cada turma (dataClass)
    penaltiesTotalValue = 0 

    allocatedTeachers = returnEmptyAllocationsTeachersDict()
    blocks = dataLoader.getBlocksCopy()

    for dataClass, timeTable in timeTablesDict.items():
        penaltiesTablesDict[dataClass] = constructClassTable(0)
        penaltyTable = penaltiesTablesDict[dataClass]

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

    return penaltiesTotalValue, penaltiesTotalValue


def returnEmptyAllocationsTeachersDict():
    empytAllocatedTeachers = {}
    teachers =  dataLoader.getTeachersCopy()
    for teacherName, teacher in teachers.items():
        empytAllocatedTeachers[teacher.name] = AllocatedTeacher(teacherName, teacher.getAvailabilitiesCopy())
    return empytAllocatedTeachers