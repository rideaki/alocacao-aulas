import random
import dataLoader
from model.business import filter
from model.business.tableFactory import constructClassTable

def constructHeusristic():
    timeTables = {}
    filteredBlocksIndexesByClass = {}
    
    # Para cada turma
    classes = dataLoader.getClassesCopy()
    while (len(classes) > 0):
        classData = random.choice(classes)
        classes.remove(classData) 
        timeTables[classData] = constructClassTable(None).copy()
        filteredBlocksIndexesByClass[classData] = filter.filterBlocksIndexesByClassData(
            dataLoader.getBlocks(), classData).copy()
        
        #Para cada professor
        teachers =  dataLoader.getTeachersCopy()
        while (len(teachers) > 0):
            teacher = teachers.pop(random.choice(list(teachers)))
            teacherBlocksToBeAllocated = filter.filterBlocksIndexesByTeacher(filteredBlocksIndexesByClass[classData], teacher.name).copy()
            while(len(teacherBlocksToBeAllocated) > 0):
                availableTeacherBlocksByShift = teacher.getAllSortedBlocksCopy()[classData.shift].copy()
                for teacherAvailableBlock in availableTeacherBlocksByShift:
                    if(timeTables[classData][teacherAvailableBlock[0]][teacherAvailableBlock[1]] == None):
                        #alocar aula
                        timeTables[classData][teacherAvailableBlock[0]][teacherAvailableBlock[1]] = teacherBlocksToBeAllocated.pop(0)
                        availableTeacherBlocksByShift.remove(teacherAvailableBlock)
                        break  #sai do laco -> teacherAvailableBlock in availableTeacherBlocksByShift:
    return timeTables    