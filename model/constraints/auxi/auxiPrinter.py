import numpy

def printPenaltiesTablesDict(penaltiesTablesDict):
    for classData, penaltyTable in penaltiesTablesDict.items():
        print(", Turma: " + str(classData.semesterNumber) + " - Curso: " + classData.courseName + " - " + classData.shift)
        print(numpy.matrix(penaltyTable))