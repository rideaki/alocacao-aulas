from unittest import skip
import dataLoader
import random
from model.business import filter
from model.business.tableFactory import constructClassTable

globalSolution = {}   #dicionario: dicionario[dataClass] = tabela horária de cada turma (dataClass)
globalSolutionPenalty = float('inf')  # penalidades positivas. Objetivo: MINIMIZAR penalty

def heusristicConstruct():
    timeTables = {}
    filteredBlocksIndexesByClass = {}
    # Para cada turma
    for classData in dataLoader.getClassesCopy():
        timeTables[classData] = constructClassTable()
        filteredBlocksIndexesByClass[classData] = filter.filterBlocksIndexesByClassData(
            dataLoader.getBlocks(), classData)
        
        #Para cada professor
        teachers =  dataLoader.getTeachersCopy()
        while (len(teachers) > 0):
            teacher = teachers.pop(random.choice(list(teachers)))
            teacherBlocksToBeAllocated = filter.filterBlocksIndexesByTeacher(filteredBlocksIndexesByClass[classData], teacher.name)
            while(len(teacherBlocksToBeAllocated) > 0):
                print(teacher.name)
                print(teacherBlocksToBeAllocated)
                availableTeacherBlocksByShift = teacher.getAllSortedBlocksCopy()[classData.shift]
                print(availableTeacherBlocksByShift)
                for teacherAvailableBlock in availableTeacherBlocksByShift:
                    print(teacherAvailableBlock)
                    print(filteredBlocksIndexesByClass[classData])
                    print(timeTables[classData])
                    if(timeTables[classData][teacherAvailableBlock[0]][teacherAvailableBlock[1]] == None):
                        #alocar aula
                        timeTables[classData][teacherAvailableBlock[0]][teacherAvailableBlock[1]] = teacherBlocksToBeAllocated.pop(0)
                        availableTeacherBlocksByShift.remove(teacherAvailableBlock)
                        break  #sai do laco -> teacherAvailableBlock in availableTeacherBlocksByShift:


if __name__ == "__main__":
    dataLoader.loadAllData()
    heusristicConstruct()

