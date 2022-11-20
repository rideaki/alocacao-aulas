from model.constraints.teacherConstrainsts import calculatePenalties
from model.exporter.csvCsjmExporter import exportToCSJMCsvFile
from model.constraints.auxi.auxiPrinter import printPenaltiesTablesDict
from model.exporter.csvGenericExporter import exportToGenericCsvFile

globalSolution = {}   #dicionario: dicionario[dataClass] = tabela horária de cada turma (dataClass)
globalSolutionPenalty = float('inf')  # penalidades positivas. Objetivo: MINIMIZAR penalty

OUTPUT_FILE_NAME = "melhor-solucao.csv"

def analyzeSolution(solution):
    penaltiesTablesDict, solutionPenalty = calculatePenalties(solution)
    print("%dpontos de penalty " % int(solutionPenalty))
    if solutionPenalty == 0:
        print("A solução ótima global foi encontrada!!!!!!")
        exportToGenericCsvFile(solution, OUTPUT_FILE_NAME)
        print("Finalizando programa.")
        exit() #finaliza programa
    
    global globalSolution
    global globalSolutionPenalty
    if(solutionPenalty < globalSolutionPenalty):    
        globalSolution = solution
        globalSolutionPenalty = solutionPenalty
        print("Uma solução viável foi encontrada.")
        printPenaltiesTablesDict(penaltiesTablesDict)
        exportToGenericCsvFile(globalSolution, OUTPUT_FILE_NAME)
        print("Aguarde para procurar soluções melhores ou tecle CTRL + C para finalizar.")
    return penaltiesTablesDict, solutionPenalty

def getGlobalSolution():
    return globalSolution