import numpy

from model.business.solutionAnalyzer import getGlobalSolution
from model.constraints.teacherConstrainsts import calculatePenalties
from model.constraints.teacherConstrainsts import SPARSE_DAYS_PENALTY
from model.exporter.csvGenericExporter import exportToGenericCsvFile

#Utiliza algoritmos geneticos na meta heuristica
def searchGeneticHeuristicSolution(solution):
    father = getGlobalSolution().copy()
    mother = solution.copy()
    fatherPenalties, _ = calculatePenalties(father)
    son = father.copy()
    hasSparseDays = False
    
    exportToGenericCsvFile(father, "log.csv")
    exportToGenericCsvFile(mother, "log.csv")
    
    #O cromossomo é a classData cujo timeTable será permutado
    for chromosome, penaltyTable in fatherPenalties.copy().items():
        localSumValue = numpy.sum(penaltyTable)
        if localSumValue >= SPARSE_DAYS_PENALTY:
            son[chromosome] = mother[chromosome]
            hasSparseDays = True
    
    if not hasSparseDays:
        for chromosome, penaltyTable in fatherPenalties.copy().items():
            localSumValue = numpy.sum(penaltyTable)
            if localSumValue > 0:
                son[chromosome] = mother[chromosome]

    exportToGenericCsvFile(son, "log.csv")

    return son

