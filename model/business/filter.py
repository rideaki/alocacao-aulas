import dataLoader
from model.utils.shifts import *

def filterBlocksIndexesBySemesterAndShift(blocksArg, semesterNumberArg=1, shiftArg = MORNING):
    filteredIndexes = []
    blocksCopy = blocksArg.copy()
    for i in range(len(blocksCopy)):
        if blocksCopy[i].semesterNumber == semesterNumberArg and blocksCopy[i].shift == shiftArg:
            filteredIndexes.append(i)
    return filteredIndexes

def filterBlocksIndexesByTeacher(blocksIndexesArg, teacherNameArg):
    filteredIndexes = []
    for blockIndex in blocksIndexesArg:
        if dataLoader.getBlocksCopy()[blockIndex].teacher.name == teacherNameArg:
            filteredIndexes.append(blockIndex)
    return filteredIndexes
