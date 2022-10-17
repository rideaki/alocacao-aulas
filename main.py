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
    for dataClass in dataLoader.getClassesCopy():
        timeTables[dataClass] = constructClassTable()
        filteredBlocksIndexesByClass[dataClass] = filter.filterBlocksIndexesBySemesterAndShift(
            dataLoader.getBlocks(), dataClass.semesterNumber, dataClass.shift)
        
        #Para cada professor
        teachers =  dataLoader.getTeachersCopy()
        while (len(teachers) > 0):
            teacher = teachers.pop(random.choice(list(teachers)))
            teacherBlocksToBeAllocated = filter.filterBlocksIndexesByTeacher(filteredBlocksIndexesByClass[dataClass], teacher.name)
            while(len(teacherBlocksToBeAllocated) > 0):
                print(teacher.name)
                print(teacherBlocksToBeAllocated)
                availableTeacherBlocksByShift = teacher.getAllSortedBlocksCopy()[dataClass.shift]
                print(availableTeacherBlocksByShift)
                for teacherAvailableBlock in availableTeacherBlocksByShift:
                    print(teacherAvailableBlock)
                    print(filteredBlocksIndexesByClass[dataClass])
                    print(timeTables[dataClass])
                    if(timeTables[dataClass][teacherAvailableBlock[0]][teacherAvailableBlock[1]] == None):
                        #alocar aula
                        timeTables[dataClass][teacherAvailableBlock[0]][teacherAvailableBlock[1]] = teacherBlocksToBeAllocated.pop(0)
                        availableTeacherBlocksByShift.remove(teacherAvailableBlock)


if __name__ == "__main__":
    dataLoader.loadAllData()
    heusristicConstruct()

