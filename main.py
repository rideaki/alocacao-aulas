import dataLoader
from model.constraints.teacherConstrainsts import calculatePenalties
from model.exporter.csvCsjmExporter import exportToCSJMCsvFile
from model.constraints.auxi.auxiPrinter import printPenaltiesTablesDict
from model.exporter.csvGenericExporter import exportToGenericCsvFile
from model.heuristic.heuristicConstructor import heusristicConstruct

globalSolution = {}   #dicionario: dicionario[dataClass] = tabela horária de cada turma (dataClass)
globalSolutionPenalty = float('inf')  # penalidades positivas. Objetivo: MINIMIZAR penalty


if __name__ == "__main__":
    dataLoader.loadAllData()

    while(True):
        solution = heusristicConstruct()
        penaltiesTablesDict, solutionPenalty = calculatePenalties(solution)
        print(solutionPenalty)
        if(solutionPenalty <= globalSolutionPenalty):    
            globalSolution = solution
            globalSolutionPenalty = solutionPenalty
            print("Uma solução viável foi encontrada. Aguarde para procurar soluções melhores.")
            printPenaltiesTablesDict(penaltiesTablesDict)
            exportToGenericCsvFile(globalSolution)  # Export para o arquiv outputTimeTable.csv na pasta raiz do projeto.

