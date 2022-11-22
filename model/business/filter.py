import model.loader.dataLoader as dataLoader
from model.utils.shifts import *

def filterBlocksIndexesByClassData(blocksArg, classDataArg):
    filteredIndexes = []
    blocksCopy = blocksArg.copy()
    for i in range(len(blocksCopy)):
        if blocksCopy[i].classData == classDataArg:
            filteredIndexes.append(i)
    return filteredIndexes.copy()

def filterBlocksIndexesByTeacher(blocksIndexesArg, teacherNameArg):
    filteredIndexes = []
    for blockIndex in blocksIndexesArg:
        if dataLoader.getBlocksCopy()[blockIndex].teacher.name == teacherNameArg:
            filteredIndexes.append(blockIndex)
    return filteredIndexes.copy()
