from array import array
from numpy import *
import dataLoader
from model.business import tableFactory, filter
from dataLoader import loadBlocksOfCurricularComponentWithTeachers, loadClasses, loadTeachers
from model.entity.teacher import Teacher
from model.utils.daysOfWeek import FRIDAY, MONDAY, SATURDAY, THURSDAY, TUESDAY, WEDNESDAY
from model.utils.shifts import AFTERNOON, MORNING

if __name__ == "__main__":
    loadClasses()
    loadTeachers()
    loadBlocksOfCurricularComponentWithTeachers()

    blocksIndexesOf1Morning = filter.filterBlocksIndexesBySemesterAndShift(dataLoader.getBlocks(), 1, MORNING)
    blocksIndexesOf1Afternoon = filter.filterBlocksIndexesBySemesterAndShift(dataLoader.getBlocks(), 1, AFTERNOON)
    blocksIndexesOf2Morning = filter.filterBlocksIndexesBySemesterAndShift(dataLoader.getBlocks(), 2, MORNING)
    blocksIndexesOf2Afternoon = filter.filterBlocksIndexesBySemesterAndShift(dataLoader.getBlocks(), 2, AFTERNOON)
    blocksIndexesOf3Morning = filter.filterBlocksIndexesBySemesterAndShift(dataLoader.getBlocks(), 3, MORNING)
    blocksIndexesOf2Afternoon = filter.filterBlocksIndexesBySemesterAndShift(dataLoader.getBlocks(), 3, AFTERNOON)
    print(blocksIndexesOf1Morning)

    blocksOfGilvan1Morning = filter.filterBlocksIndexesByTeacher(blocksIndexesOf1Morning, "Gilvan")
    print(blocksOfGilvan1Morning)

    # alocando aulas
    # period1MorningTimeTable = dataLoader.getClassesCopy()[0].timeTable.copy()
    period1MorningTimeTable = [
        [None, None, None, None, None],
        [10, None, None, None, None],
        [0, None, None, None, None],
    ]
