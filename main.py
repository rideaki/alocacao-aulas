from unicodedata import name
import dataLoader
import random
from model.business import filter
from dataLoader import _loadCurricularComponentTeachers, _loadClasses, _loadTeachers, loadAllData
from model.utils.shifts import AFTERNOON, MORNING

globalSolution = {}   #dicionario: blocksIndexesByClass[dataClass] = indices dos blocos na tabela horária de cada turma (class)
globalSolutionPenalty = float('inf')  # penalidades positivas. Objetivo: MINIMIZAR penalty

def heusristicConstruct():
    blocksIndexesByClass = {}
    # Para cada turma
    for dataClass in dataLoader.getClassesCopy():
        blocksIndexesByClass[dataClass] = filter.filterBlocksIndexesBySemesterAndShift(
            dataLoader.getBlocks(), dataClass.semesterNumber, dataClass.shift)
        
        #Para cada professor
        teachers =  dataLoader.getTeachersCopy()
        while (len(teachers) > 0):
            print(blocksIndexesByClass[dataClass])
            teacher = teachers.pop(random.choice(list(teachers)))
            teacherBlocks = filter.filterBlocksIndexesByTeacher(blocksIndexesByClass[dataClass], teacher.name)
            if(len(teacherBlocks) > 0):
                #teacher to be alocated

                print(teacher.name)
                print(teacherBlocks)
                print("--------------------------------------------------------------------")

if __name__ == "__main__":
    dataLoader.loadAllData()
    heusristicConstruct()

