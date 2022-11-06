import dataLoader

from model.business.solutionAnalyzer import analyzeSolution
from model.heuristic.constructorHeuristic import constructHeusristicSolution
from model.heuristic.metaheuristic.tabuMetaHeuristic import searchTabuHeuristicSolution

META_HEURISTIC_CYCLES = 60

if __name__ == "__main__":
    dataLoader.loadAllData()
    while(True):
        solution = constructHeusristicSolution().copy()
        penaltiesTablesDict = analyzeSolution(solution)

        for i in range(META_HEURISTIC_CYCLES):
            solution = searchTabuHeuristicSolution(solution.copy(), penaltiesTablesDict.copy())
            penaltiesTablesDict = analyzeSolution(solution)