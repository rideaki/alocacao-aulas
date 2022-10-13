import dataLoader
from dataLoader import loadBlocksOfCurricularComponentWithTeachers, loadClasses, loadTeachers
from model.entity.teacher import Teacher
from model.utils.daysOfWeek import FRIDAY, MONDAY, SATURDAY, THURSDAY, TUESDAY, WEDNESDAY

if __name__ == '__main__':
    loadClasses()
    print(dataLoader.__classes)
    loadTeachers()
    print(dataLoader.__teachers["Reginaldo"].availabilities)
    loadBlocksOfCurricularComponentWithTeachers()
    print(dataLoader.__blocksOfCCsWithTeachers[0].teacher.name)
    print(dataLoader.__blocksOfCCsWithTeachers[0].teacher == dataLoader.__blocksOfCCsWithTeachers[1].teacher)
    #input("Digite enter para finalizar.")