import dataLoader
import numpy
from model.utils.shifts import MORNING

def filterBlocksIndexesBySemesterAndShift(blocksArg, semesterNumberArg=1, shiftArg = MORNING):
    filteredIndexes = []
    for i in range(len(blocksArg)):
        if blocksArg[i].semesterNumber == semesterNumberArg and blocksArg[i].shift == shiftArg:
            filteredIndexes.append(i)
    return filteredIndexes

def filterBlocksIndexesByTeacher(blocksArg, teacherNameArg):
    filteredIndexes = []
    for i in range(len(blocksArg)):
        if blocksArg[i].teacher.name == teacherNameArg:
            filteredIndexes.append(i)
    return filteredIndexes
