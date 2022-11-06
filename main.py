import dataLoader
from model.constraints.teacherConstrainsts import calculatePenalties
from model.exporter.csvCsjmExporter import exportToCSJMCsvFile
from model.constraints.auxi.auxiPrinter import printPenaltiesTablesDict
from model.exporter.csvGenericExporter import exportToGenericCsvFile
from model.heuristic.constructorHeuristic import constructHeusristicSolution
from model.heuristic.metaheuristic.tabuMetaHeuristic import searchTabuHeuristicSolution

globalSolution = {}   #dicionario: dicionario[dataClass] = tabela horária de cada turma (dataClass)
globalSolutionPenalty = float('inf')  # penalidades positivas. Objetivo: MINIMIZAR penalty

def analyzeSolution(solution):
    penaltiesTablesDict, solutionPenalty = calculatePenalties(solution)
    print(int(solutionPenalty))
    global globalSolutionPenalty
    if(solutionPenalty < globalSolutionPenalty):    
        globalSolution = solution
        globalSolutionPenalty = solutionPenalty
        print("Uma solução viável foi encontrada.")
        printPenaltiesTablesDict(penaltiesTablesDict)
        exportToGenericCsvFile(globalSolution)  # Export para o arquivo outputTimeTable.csv na pasta raiz do projeto.
        print("Aguarde para procurar soluções melhores ou tecle CTRL + C para finalizar.")
    return penaltiesTablesDict

if __name__ == "__main__":
    dataLoader.loadAllData()

    if(globalSolutionPenalty > 0):
        solution = constructHeusristicSolution().copy()
        penaltiesTablesDict = analyzeSolution(solution)

        for i in range(400):
            solution = searchTabuHeuristicSolution(solution.copy(), penaltiesTablesDict.copy())
            penaltiesTablesDict = analyzeSolution(solution)