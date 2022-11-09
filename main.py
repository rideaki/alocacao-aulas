import dataLoader

from model.business.solutionAnalyzer import analyzeSolution, globalSolutionPenalty
from model.constraints.teacherConstrainsts import SPARSE_DAYS_PENALTY
from model.heuristic.constructorHeuristic import constructHeusristicSolution
from model.heuristic.metaheuristic.tabuMetaHeuristic import searchTabuHeuristicSolution

def searchHeuristicSolution():
    solution = constructHeusristicSolution().copy()
    penaltiesTablesDict = analyzeSolution(solution)

    searchTabuHeuristicSolution(solution, penaltiesTablesDict)

if __name__ == "__main__":
    dataLoader.loadAllData()
    while globalSolutionPenalty > 0:
        searchHeuristicSolution()