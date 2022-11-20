import numpy

from model.business.solutionAnalyzer import getGlobalSolution
from model.constraints.teacherConstrainsts import calculatePenalties

#Utiliza algoritmos geneticos na meta heuristica
def searchGeneticHeuristicSolution(solution):
    father = getGlobalSolution().copy()
    mother = solution.copy()
    fatherPenalties, _ = calculatePenalties(father)
    #O cromossomo é a classData cujo total de penalidades é a maior
    chromosome = __searchMaxSumClassPenalty(fatherPenalties)
    son = father.copy()
    son[chromosome] = mother[chromosome]
    return son

def __searchMaxSumClassPenalty(penaltiesTablesDict):
    maxSumPenalty = -1
    # Para cada turma
    for classData, penaltyTable in penaltiesTablesDict.copy().items():
        localSumValue = numpy.sum(penaltyTable)
        if localSumValue <= maxSumPenalty:
            continue #maior penalidade da tabela não é o maximo de todas -> pula iteracao
        maxSumPenalty = localSumValue
        maxClassData = classData
    return maxClassData
