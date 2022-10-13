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
    print(dataLoader.__classes)
    loadTeachers()
    print(dataLoader.__teachers["Reginaldo"].availabilities)
    loadBlocksOfCurricularComponentWithTeachers()
    print(dataLoader.__blocksOfCCsWithTeachers[0].teacher.name)
    print(dataLoader.__blocksOfCCsWithTeachers[0].teacher == dataLoader.__blocksOfCCsWithTeachers[1].teacher)
    
    period1MorningTimeTable = dataLoader.__classes[0].timeTable.copy()
    period1MorningTimeTable[0][0] = 1
    print(period1MorningTimeTable) 
    print(dataLoader.__classes[0].timeTable) 
    #input("Digite enter para finalizar.")
