import copy
import numpy

def printPenaltiesTablesDict(penaltiesTablesDictArg):
    penaltiesTablesDict = dict(sorted(copy.deepcopy(penaltiesTablesDictArg).items()))
    for classData, penaltyTable in penaltiesTablesDict.items():
        print(", Turma: " + str(classData.periodNumber) + " " + classData.shift + " - Curso: " + classData.courseName)
        print(numpy.matrix(penaltyTable))