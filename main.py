import dataLoader

from model.business.solutionAnalyzer import globalSolutionPenalty
from model.constraints.teacherConstrainsts import SPARSE_DAYS_PENALTY
from model.heuristic.constructorHeuristic import constructHeusristicSolution
from model.heuristic.metaheuristic.tabuMetaHeuristic import searchTabuHeuristicSolution
from model.heuristic.metaheuristic.geneticHeuristic import searchGeneticHeuristicSolution

def __searchHeuristicSolution():
    initialSolution = constructHeusristicSolution().copy()
    searchTabuHeuristicSolution(initialSolution)

    initialSolution = constructHeusristicSolution().copy()
    geneticSolution = searchGeneticHeuristicSolution(initialSolution)
    searchTabuHeuristicSolution(geneticSolution)

if __name__ == "__main__":
    dataLoader.loadAllData()
    while globalSolutionPenalty > 0:
        __searchHeuristicSolution()