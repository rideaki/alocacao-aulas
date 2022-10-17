import dataLoader
import random
from model.business import filter
from dataLoader import _loadCurricularComponentTeachers, _loadClasses, _loadTeachers, loadData
from model.utils.shifts import AFTERNOON, MORNING

if __name__ == "__main__":
    loadData()

    blocksIndexesByClass = {}
    # Para cada turma
    for dataClass in dataLoader.getClassesCopy():
        blocksIndexesByClass[dataClass] = filter.filterBlocksIndexesBySemesterAndShift(
            dataLoader.getBlocks(), dataClass.semesterNumber, dataClass.shift)
        
        #Para cada professor
        teachers =  dataLoader.getTeachersCopy()
        while (len(teachers) > 0):    
            teacher = teachers.pop(random.choice(list(teachers)))
            print(teacher.name)
        
        blocksOfGilvan1Morning = filter.filterBlocksIndexesByTeacher(blocksIndexesByClass[dataClass], "Gilvan")

