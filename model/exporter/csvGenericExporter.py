import dataLoader
from model.utils.shifts import NUMBER_OF_BLOCKS_IN_SHIFT
from typing import Final

MAX_CELL_SIZE: Final = 20

# Exporter que pode ser utilizado por qualquer campus
def exportToGenericCsvFile(timeTables):

    classes = dataLoader.getClassesCopy()

    csvString = ""
    for classData in classes:     
        # Para cada Turma (class)
        csvString += ", Turma: " + str(classData.semesterNumber) + " - Curso: " + classData.courseName + " - " + classData.shift + "\n"
        classTimeTable = timeTables[classData]
        for blockNumber in range(NUMBER_OF_BLOCKS_IN_SHIFT): #3 blocos por periodo
            csvString += "Aula " + str(blockNumber) + ", "
            for dayOfWeek in range(5):  #5 dias uteis por semana (segunda a sexta)
                csvString += blockIndexToString(classTimeTable[blockNumber][dayOfWeek])
            csvString += " \n"
        csvString += " \n"

    outputFileName = "outputTimeTable.csv"  #grava na raiz do projeto
    file = open(outputFileName, "w")
    file.write(csvString)
    file.close()

    print("Alocação de aulas salva na planilha: " + outputFileName)

def blockIndexToString(index):
    blocks = dataLoader.getBlocksCopy()
    if((index == None) or (index >= len(blocks)) or (blocks[index] == None)):
        return ("TV / TV").ljust(MAX_CELL_SIZE) + ", "  # Tempo Vago
    else:
        return (blocks[index].curricularComponentName + " / " + blocks[index].teacher.name).ljust(MAX_CELL_SIZE) + ", "

