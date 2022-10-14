from array import array
from numpy import *
import dataLoader
from model.business import tableFactory
from dataLoader import (loadBlocksOfCurricularComponentWithTeachers,
                        loadClasses, loadTeachers)
from model.entity.teacher import Teacher
from model.utils.daysOfWeek import (FRIDAY, MONDAY, SATURDAY, THURSDAY,
                                    TUESDAY, WEDNESDAY)

if __name__ == '__main__':
    loadClasses()
    loadTeachers()
    loadBlocksOfCurricularComponentWithTeachers()
    
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

    #alocando aulas
    #period1MorningTimeTable = dataLoader.getClassesCopy()[0].timeTable.copy()
    period1MorningTimeTable = [[None, None, None, None, None],     
                               [  10, None, None, None, None],     
                               [   0, None, None, None, None]]