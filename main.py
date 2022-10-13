from array import array
from numpy import *
import dataLoader
from dataLoader import (loadBlocksOfCurricularComponentWithTeachers,
                        loadClasses, loadTeachers)
from model.entity.teacher import Teacher
from model.utils.daysOfWeek import (FRIDAY, MONDAY, SATURDAY, THURSDAY,
                                    TUESDAY, WEDNESDAY)

if __name__ == '__main__':
    loadClasses()
    print(dataLoader.getClassesCopy())
    loadTeachers()
    print(dataLoader.getTeachersCopy()["Reginaldo"].availabilities)
    loadBlocksOfCurricularComponentWithTeachers()
    print(dataLoader.getBlocksOfCCsWithTeachersCopy()[0].teacher.name)
    print(dataLoader.getBlocksOfCCsWithTeachersCopy()[0].teacher == dataLoader.__blocksOfCCsWithTeachers[1].teacher)
    
    #Teste efeito colateral para matriz
    period1MorningTimeTable = dataLoader.getClassesCopy()[0].timeTable.copy()
    period1MorningTimeTable[0][0] = 1
    print(period1MorningTimeTable) 
    print(dataLoader.getClassesCopy()[0].timeTable) 

    #teste de indice do vetor de blocos do dataLoader
    firstBlock = dataLoader.getBlocksOfCCsWithTeachersCopy()[0]
    indexOfBlock = dataLoader.getBlocksOfCCsWithTeachersCopy().index(firstBlock)
    print(indexOfBlock)

    secondBlock = dataLoader.getBlocksOfCCsWithTeachersCopy()[1]
    indexOfBlock = dataLoader.getBlocksOfCCsWithTeachersCopy().index(secondBlock)
    print(indexOfBlock)
    
    print(firstBlock == secondBlock)
    print(firstBlock is secondBlock)
    print(firstBlock == dataLoader.getBlocksOfCCsWithTeachersCopy()[0])
    print(firstBlock is dataLoader.getBlocksOfCCsWithTeachersCopy()[0])