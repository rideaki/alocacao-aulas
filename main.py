import dataLoader
from model.constraints.teacherConstrainsts import calculatePenalties
from model.exporter.csvCsjmExporter import exportToCSJMCsvFile
from model.constraints.auxi.auxiPrinter import printPenaltiesTablesDict
from model.exporter.csvGenericExporter import exportToGenericCsvFile
from model.heuristic.constructorHeuristic import constructHeusristicSolution
from model.heuristic.metaHeuristic import searchMetaHeuristicSolution

globalSolution = {}   #dicionario: dicionario[dataClass] = tabela horária de cada turma (dataClass)
globalSolutionPenalty = float('inf')  # penalidades positivas. Objetivo: MINIMIZAR penalty


if __name__ == "__main__":
    dataLoader.loadAllData()

    if(True):
        solution = constructHeusristicSolution().copy()
        penaltiesTablesDict, solutionPenalty = calculatePenalties(solution)
        if(solutionPenalty <= globalSolutionPenalty):    
            globalSolution = solution
            globalSolutionPenalty = solutionPenalty
            print("Uma solução viável foi encontrada.")
            printPenaltiesTablesDict(penaltiesTablesDict)
            exportToGenericCsvFile(globalSolution)  # Export para o arquiv outputTimeTable.csv na pasta raiz do projeto.
            print("Aguarde para procurar soluções melhores ou tecle CTRL + C para finalizar.")

        solution = searchMetaHeuristicSolution(solution.copy(), penaltiesTablesDict.copy())