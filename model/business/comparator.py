import dataLoader
import numpy

#Verifica se duas timeTables são iguais ou equivalentes, ou seja, cuja alocação de blocos são as mesmas
def areEquivalentTables(timeTable1, timeTable2):
    if numpy.array_equal(timeTable1, timeTable2):  #se as duas tabelas são iguais
        return True
    for i in range(len(timeTable1)):
        for j in range(len(timeTable1[i])):
            if __areDifferentBlocks(timeTable1[i][j], timeTable2[i][j]):
                return False
    return True

#Recebe indices de dois blocos, e retorna: 
# False: se os indices são iguais, ou se são blocos do mesmo componente curricular e mesmo professor
# True: caso contrário
def __areDifferentBlocks(block1Index, block2Index):
    if block1Index == block2Index:
        return False
    if (block1Index == None and block2Index != None) or (block1Index != None and block2Index == None):
        return True
    blocks = dataLoader.getBlocksCopy()
    block1 = blocks[block1Index]
    block2 = blocks[block2Index]
    return (block1.curricularComponentName != block2.curricularComponentName) or (
        block1.teacher.name != block2.teacher.name
    )       