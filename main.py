from unittest import skip
import csv
import dataLoader
import random
from model.business import filter
from model.business.tableFactory import constructClassTable

globalSolution = {}   #dicionario: dicionario[dataClass] = tabela horária de cada turma (dataClass)
globalSolutionPenalty = float('inf')  # penalidades positivas. Objetivo: MINIMIZAR penalty

def heusristicConstruct():
    timeTables = {}
    filteredBlocksIndexesByClass = {}
    # Para cada turma
    for classData in dataLoader.getClassesCopy():
        timeTables[classData] = constructClassTable()
        filteredBlocksIndexesByClass[classData] = filter.filterBlocksIndexesByClassData(
            dataLoader.getBlocks(), classData)
        
        #Para cada professor
        teachers =  dataLoader.getTeachersCopy()
        while (len(teachers) > 0):
            teacher = teachers.pop(random.choice(list(teachers)))
            teacherBlocksToBeAllocated = filter.filterBlocksIndexesByTeacher(filteredBlocksIndexesByClass[classData], teacher.name)
            while(len(teacherBlocksToBeAllocated) > 0):
                availableTeacherBlocksByShift = teacher.getAllSortedBlocksCopy()[classData.shift]
                for teacherAvailableBlock in availableTeacherBlocksByShift:
                    if(timeTables[classData][teacherAvailableBlock[0]][teacherAvailableBlock[1]] == None):
                        #alocar aula
                        timeTables[classData][teacherAvailableBlock[0]][teacherAvailableBlock[1]] = teacherBlocksToBeAllocated.pop(0)
                        availableTeacherBlocksByShift.remove(teacherAvailableBlock)
                        break  #sai do laco -> teacherAvailableBlock in availableTeacherBlocksByShift:
    return timeTables    

def exportToCSJMCsvFile(timeTables):
    csvString = ",Primeiro Período ,,,,,,Segundo Período ,,,,,,Terceiro Período ,,,,\n"
    csvString += ",Segunda,Terça,Quarta,Quinta,Sexta,,Segunda,Terça,Quarta,Quinta,Sexta,,Segunda,Terça,Quarta,Quinta,Sexta\n"

    classes = dataLoader.getClassesCopy()
    period1MorningTimeTable = timeTables[classes[0]].copy()
    period1AfternoonTimeTable = timeTables[classes[1]].copy()
    period2MorningTimeTable = timeTables[classes[2]].copy()
    period2AfternoonTimeTable = timeTables[classes[3]].copy()
    period3MorningTimeTable = timeTables[classes[4]].copy()
    period3AfternoonTimeTable = timeTables[classes[5]].copy()

    csvString += "07:00 - 07:45,"
    rowString = ""
    rowString += blockIndexToString(period1AfternoonTimeTable[0][0])
    rowString += "\n"

    csvString += rowString

    outputFileName = "outputTimeTable.csv"
    file = open(outputFileName, "w")
    file.write(csvString)
    file.close()

    print("Alocação de aulas salva na planilha: " + outputFileName)

def blockIndexToString(index):
    blocks = dataLoader.getBlocksCopy()
    if((index == None) or (index >= len(blocks)) or (blocks[index] == None)):
        return "TV / TV"  # Tempo Vago
    else:
        return blocks[index].curricularComponentName + " / " + blocks[index].teacher.name


if __name__ == "__main__":
    dataLoader.loadAllData()
    globalSolution = heusristicConstruct().copy()

    exportToCSJMCsvFile(globalSolution)

