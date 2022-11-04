import copy
import dataLoader
import random
from model.business import filter
from model.business.tableFactory import constructClassTable

def constructHeusristicSolution():
    timeTables = {}
    filteredBlocksIndexesByClass = {}
    
    # Para cada turma
    classes = dataLoader.getClassesCopy()
    while (len(classes) > 0):
        classData = random.choice(classes)
        classes.remove(classData) 
        timeTables[classData] = copy.deepcopy(constructClassTable(None))
        filteredBlocksIndexesByClass[classData] = copy.deepcopy(filter.filterBlocksIndexesByClassData(
            dataLoader.getBlocks(), classData))
        
        #Para cada professor
        teachers =  dataLoader.getTeachersCopy()
        while (len(teachers) > 0):
            teacher = teachers.pop(random.choice(list(teachers)))
            teacherBlocksToBeAllocated = copy.deepcopy(filter.filterBlocksIndexesByTeacher(filteredBlocksIndexesByClass[classData], teacher.name))
            while(len(teacherBlocksToBeAllocated) > 0):
                availableTeacherBlocksByShift = teacher.getAllSortedBlocksCopy()[classData.shift]
                for teacherAvailableBlock in availableTeacherBlocksByShift:
                    if(timeTables[classData][teacherAvailableBlock[0]][teacherAvailableBlock[1]] == None):
                        #alocar aula
                        timeTables[classData][teacherAvailableBlock[0]][teacherAvailableBlock[1]] = teacherBlocksToBeAllocated.pop(0)
                        availableTeacherBlocksByShift.remove(teacherAvailableBlock)
                        break  #sai do laco -> teacherAvailableBlock in availableTeacherBlocksByShift:
    return timeTables    