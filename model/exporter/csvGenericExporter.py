import model.loader.dataLoader as dataLoader
import model.constraints.teacherConstrainsts as teacherConstrainsts
from model.utils.shifts import NUMBER_OF_BLOCKS_IN_SHIFT
from typing import Final
from model.constraints.teacherConstrainsts import calculatePenalties

MAX_CELL_SIZE: Final = 20
REPORT_CELL_SIZE: Final = 40
RESOLVED_CELL_SIZE: Final = 12

# Exporter que pode ser utilizado por qualquer campus
def exportToGenericCsvFile(timeTables, outputFileName):

    classes = dataLoader.getClassesCopy()

    csvString = ""
    penaltiesTablesDict, solutionPenalty = calculatePenalties(timeTables)
    for classData in classes:     
        # Para cada Turma (class)
        csvString += ", Turma: " + str(classData.periodNumber) + " - Curso: " + classData.courseName + " - " + classData.shift + "\n"
        classTimeTable = timeTables[classData]
        for blockNumber in range(NUMBER_OF_BLOCKS_IN_SHIFT): 
            csvString += "Aula " + str(blockNumber) + ", "
            for dayOfWeek in range(len(classTimeTable[0])):  #dias da semana alocadas na classTimeTable
                csvString += blockIndexToString(classTimeTable[blockNumber][dayOfWeek])
            csvString += " \n"
        csvString += " \n"

    csvString += "\n" +  ("RELATORIO: ").ljust(REPORT_CELL_SIZE) + ", " + ("% Resolvido").rjust(RESOLVED_CELL_SIZE) + " \n"

#CONFLICT_PENALTY =        9999999999
#AVAILABILITY_PENALTY =       3000000
#CONSECUTIVE_BLOCKS_PENALTY = 2000000
#SPARSE_DAYS_PENALTY =            100
#SPARSE_HOURS_PENALTY =             1

    solutionPercent = 0.0
    if solutionPenalty > teacherConstrainsts.SPARSE_DAYS_PENALTY:
        solutionPercent = 0.0
    else:
        solutionPercent = round(solutionPenalty/teacherConstrainsts.SPARSE_DAYS_PENALTY, 1)
 
    csvString += ("Tempo Vago").ljust(REPORT_CELL_SIZE) + ", " + (str(solutionPercent) + "%").rjust(RESOLVED_CELL_SIZE) + " \n"

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

