import dataLoader
from model.exporter.csvCsjmExporter import exportToCSJMCsvFile
from model.heuristic.heuristicConstructor import heusristicConstruct

globalSolution = {}   #dicionario: dicionario[dataClass] = tabela horária de cada turma (dataClass)
globalSolutionPenalty = float('inf')  # penalidades positivas. Objetivo: MINIMIZAR penalty


if __name__ == "__main__":
    dataLoader.loadAllData()
    globalSolution = heusristicConstruct().copy()

    exportToCSJMCsvFile(globalSolution)  # Export para o arquiv outputTimeTable.csv na pasta raiz do projeto.

