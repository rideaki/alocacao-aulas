import numpy

def printPenaltiesTablesDict(penaltiesTablesDict):
    for classData, penaltyTable in penaltiesTablesDict.items():
        print(", Turma: " + str(classData.periodNumber) + " - Curso: " + classData.courseName + " - " + classData.shift)
        print(numpy.matrix(penaltyTable))