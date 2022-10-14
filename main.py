from numpy import *
import dataLoader
from model.business import filter
from dataLoader import loadBlocksOfCurricularComponentWithTeachers, loadClasses, loadTeachers
from model.utils.shifts import AFTERNOON, MORNING

if __name__ == "__main__":
    loadClasses()
    loadTeachers()
    loadBlocksOfCurricularComponentWithTeachers()

    blocksIndexesByClass = {}
    for dataClass in dataLoader.getClassesCopy():
        blocksIndexesByClass[dataClass] = filter.filterBlocksIndexesBySemesterAndShift(
            dataLoader.getBlocks(), dataClass.semesterNumber, dataClass.shift)
        blocksOfGilvan1Morning = filter.filterBlocksIndexesByTeacher(blocksIndexesByClass[dataClass], "Gilvan")

    # alocando aulas
    # period1MorningTimeTable = dataLoader.getClassesCopy()[0].timeTable.copy()
    period1MorningTimeTable = [
        [None, None, None, None, None],
        [10, None, None, None, None],
        [0, None, None, None, None],
    ]
