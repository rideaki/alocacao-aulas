import dataLoader
from model.heuristic.heuristicConstructor import heusristicConstruct

globalSolution = {}   #dicionario: dicionario[dataClass] = tabela horária de cada turma (dataClass)
globalSolutionPenalty = float('inf')  # penalidades positivas. Objetivo: MINIMIZAR penalty

def exportToCSJMCsvFile(timeTables):

    classes = dataLoader.getClassesCopy()
    period1MorningTimeTable = timeTables[classes[0]].copy()
    period1AfternoonTimeTable = timeTables[classes[1]].copy()
    period2MorningTimeTable = timeTables[classes[2]].copy()
    period2AfternoonTimeTable = timeTables[classes[3]].copy()
    period3MorningTimeTable = timeTables[classes[4]].copy()
    period3AfternoonTimeTable = timeTables[classes[5]].copy()

    # MATUTINO ###############################################################################
    csvString = "," + str(classes[0].semesterNumber) + " Período - " + classes[0].courseName + " - " + classes[0].shift + ",,,,,," 
    csvString +=      str(classes[2].semesterNumber) + " Período - " + classes[2].courseName + " - " + classes[2].shift + ",,,,,," 
    csvString +=      str(classes[4].semesterNumber) + " Período - " + classes[4].courseName + " - " + classes[4].shift + " ,,,,\n"
    csvString += ",Segunda,Terça,Quarta,Quinta,Sexta,,Segunda,Terça,Quarta,Quinta,Sexta,,Segunda,Terça,Quarta,Quinta,Sexta\n"

    ##########################################################################################
    csvString += "07:00 - 07:45,"
    rowString = ""
    for i in range(5):
        rowString += blockIndexToString(period1MorningTimeTable[0][i])
    rowString += ","
    for i in range(5):
        rowString += blockIndexToString(period2MorningTimeTable[0][i])
    rowString += ","
    for i in range(5):
        rowString += blockIndexToString(period3MorningTimeTable[0][i])
    rowString += "\n"
    csvString += rowString

    csvString += "07:45 - 08:30,"
    csvString += rowString      #aulas duplas

    ##########################################################################################
    csvString += "08:30 - 09:15,"
    rowString = ""
    for i in range(5):
        rowString += blockIndexToString(period1MorningTimeTable[1][i])
    rowString += ","
    for i in range(5):
        rowString += blockIndexToString(period2MorningTimeTable[1][i])
    rowString += ","
    for i in range(5):
        rowString += blockIndexToString(period3MorningTimeTable[1][i])
    rowString += "\n"
    csvString += rowString

    csvString += "09:15 - 10:00,"
    csvString += rowString     #aulas duplas 

    ##########################################################################################
    csvString += "10:00 - 10:15,,,,,,,,,,,,,,,,,\n"  #intervalo

    ##########################################################################################
    csvString += "10:15 - 11:00,"
    rowString = ""
    for i in range(5):
        rowString += blockIndexToString(period1MorningTimeTable[2][i])
    rowString += ","
    for i in range(5):
        rowString += blockIndexToString(period2MorningTimeTable[2][i])
    rowString += ","
    for i in range(5):
        rowString += blockIndexToString(period3MorningTimeTable[2][i])
    rowString += "\n"
    csvString += rowString

    csvString += "11:00 - 11:45,"
    csvString += rowString     #aulas duplas

    # VESPERTINO ###############################################################################
    csvString +="\n"
    csvString +="," + str(classes[1].semesterNumber) + " Período - " + classes[1].courseName + " - " + classes[1].shift + ",,,,,," 
    csvString +=      str(classes[3].semesterNumber) + " Período - " + classes[3].courseName + " - " + classes[3].shift + ",,,,,," 
    csvString +=      str(classes[5].semesterNumber) + " Período - " + classes[5].courseName + " - " + classes[5].shift + " ,,,,\n"
    csvString += ",Segunda,Terça,Quarta,Quinta,Sexta,,Segunda,Terça,Quarta,Quinta,Sexta,,Segunda,Terça,Quarta,Quinta,Sexta\n"

    ##########################################################################################
    csvString += "13:15 - 14:00,"
    rowString = ""
    for i in range(5):
        rowString += blockIndexToString(period1AfternoonTimeTable[0][i])
    rowString += ","
    for i in range(5):
        rowString += blockIndexToString(period2AfternoonTimeTable[0][i])
    rowString += ","
    for i in range(5):
        rowString += blockIndexToString(period3AfternoonTimeTable[0][i])
    rowString += "\n"
    csvString += rowString

    csvString += "14:00 - 14:45,"
    csvString += rowString      #aulas duplas

    ##########################################################################################
    csvString += "14:45 - 15:30,"
    rowString = ""
    for i in range(5):
        rowString += blockIndexToString(period1AfternoonTimeTable[1][i])
    rowString += ","
    for i in range(5):
        rowString += blockIndexToString(period2AfternoonTimeTable[1][i])
    rowString += ","
    for i in range(5):
        rowString += blockIndexToString(period3AfternoonTimeTable[1][i])
    rowString += "\n"
    csvString += rowString

    csvString += "15:30 - 16:15,"
    csvString += rowString     #aulas duplas 

    ##########################################################################################
    csvString += "16:15 - 16:30,,,,,,,,,,,,,,,,,\n"  #intervalo

    ##########################################################################################
    csvString += "16:30 - 17:15,"
    rowString = ""
    for i in range(5):
        rowString += blockIndexToString(period1AfternoonTimeTable[2][i])
    rowString += ","
    for i in range(5):
        rowString += blockIndexToString(period2AfternoonTimeTable[2][i])
    rowString += ","
    for i in range(5):
        rowString += blockIndexToString(period3AfternoonTimeTable[2][i])
    rowString += "\n"
    csvString += rowString

    csvString += "17:15 - 18:00,"
    csvString += rowString     #aulas duplas


    ##########################################################################################
    outputFileName = "outputTimeTable.csv"
    file = open(outputFileName, "w")
    file.write(csvString)
    file.close()

    print("Alocação de aulas salva na planilha: " + outputFileName)

def blockIndexToString(index):
    blocks = dataLoader.getBlocksCopy()
    if((index == None) or (index >= len(blocks)) or (blocks[index] == None)):
        return "TV / TV, "  # Tempo Vago
    else:
        return blocks[index].curricularComponentName + " / " + blocks[index].teacher.name + ","


if __name__ == "__main__":
    dataLoader.loadAllData()
    globalSolution = heusristicConstruct().copy()

    exportToCSJMCsvFile(globalSolution)  # Export para o arquiv outputTimeTable.csv na pasta raiz do projeto.

