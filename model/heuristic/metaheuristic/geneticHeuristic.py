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
    
    #Permuta de cromossomos para dias esparsos
    hasSparseDays = permuteChromosomes(mother, fatherPenalties, son, SPARSE_DAYS_PENALTY -1)
    if not hasSparseDays:
        #Permuta de cromosssomos para horários esparsos (horários vagos)
        permuteChromosomes(mother, fatherPenalties, son, 0)

    return son

def permuteChromosomes(mother, fatherPenalties, son, penaltySumCriteria):
    #O cromossomo é a classData cujo timeTable será permutado
    for chromosome, penaltyTable in fatherPenalties.copy().items():
        classPenaltySum = numpy.sum(penaltyTable)
        if classPenaltySum > penaltySumCriteria :
            son[chromosome] = mother[chromosome]
            hasSparseDays = True
    return hasSparseDays

