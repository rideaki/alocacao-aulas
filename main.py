import dataLoader

from model.business.solutionAnalyzer import analyzeSolution, globalSolutionPenalty
from model.heuristic.constructorHeuristic import constructHeusristicSolution
from model.heuristic.metaheuristic.tabuMetaHeuristic import searchTabuHeuristicSolution

META_HEURISTIC_CYCLES = 180

def searchHeuristicSolution():
    solution = constructHeusristicSolution().copy()
    penaltiesTablesDict = analyzeSolution(solution)

    for i in range(META_HEURISTIC_CYCLES):
        print("\n %d° Ciclo: " % i)
        solution = searchTabuHeuristicSolution(solution.copy(), penaltiesTablesDict.copy())
        penaltiesTablesDict = analyzeSolution(solution)

if __name__ == "__main__":
    dataLoader.loadAllData()
    while(globalSolutionPenalty > 0):
        searchHeuristicSolution()