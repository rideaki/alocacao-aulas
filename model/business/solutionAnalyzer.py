from model.constraints.teacherConstrainsts import calculatePenalties
from model.exporter.csvCsjmExporter import exportToCSJMCsvFile
from model.constraints.auxi.auxiPrinter import printPenaltiesTablesDict
from model.exporter.csvGenericExporter import exportToGenericCsvFile

globalSolution = {}   #dicionario: dicionario[dataClass] = tabela horária de cada turma (dataClass)
globalSolutionPenalty = float('inf')  # penalidades positivas. Objetivo: MINIMIZAR penalty

def analyzeSolution(solution):
    penaltiesTablesDict, solutionPenalty = calculatePenalties(solution)
    print(int(solutionPenalty))
    if solutionPenalty == 0:
        print("A solução ótima global foi encontrada!!!!!!")
        exportToGenericCsvFile(solution)  # Export para o arquivo outputTimeTable.csv na pasta raiz do projeto.
        print("Finalizando programa.")
        exit()
    
    global globalSolutionPenalty
    if(solutionPenalty < globalSolutionPenalty):    
        globalSolution = solution
        globalSolutionPenalty = solutionPenalty
        print("Uma solução viável foi encontrada.")
        printPenaltiesTablesDict(penaltiesTablesDict)
        exportToGenericCsvFile(globalSolution)  # Export para o arquivo outputTimeTable.csv na pasta raiz do projeto.
        print("Aguarde para procurar soluções melhores ou tecle CTRL + C para finalizar.")
    return penaltiesTablesDict