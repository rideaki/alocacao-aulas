import random
import dataLoader
from model.business import filter
from model.business.tableFactory import constructClassTable

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
                availableTeacherBlocksByShift = teacher.getAllSortedBlocksCopy()[classData.shift]
                for teacherAvailableBlock in availableTeacherBlocksByShift:
                    if(timeTables[classData][teacherAvailableBlock[0]][teacherAvailableBlock[1]] == None):
                        #alocar aula
                        timeTables[classData][teacherAvailableBlock[0]][teacherAvailableBlock[1]] = teacherBlocksToBeAllocated.pop(0)
                        availableTeacherBlocksByShift.remove(teacherAvailableBlock)
                        break  #sai do laco -> teacherAvailableBlock in availableTeacherBlocksByShift:
    return timeTables    