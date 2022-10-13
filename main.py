import dataLoader
from dataLoader import loadBlocksOfCurricularComponentWithTeachers, loadClasses, loadTeachers
from model.entity.teacher import Teacher
from model.utils.daysOfWeek import FRIDAY, MONDAY, SATURDAY, THURSDAY, TUESDAY, WEDNESDAY

if __name__ == '__main__':
    loadClasses()
    print(dataLoader.classes)
    loadTeachers()
    print(dataLoader.teachers["Reginaldo"].availabilities)
    loadBlocksOfCurricularComponentWithTeachers()
    print(dataLoader.blocksOfCCsWithTeachers[0].teacher.name)
    print(dataLoader.blocksOfCCsWithTeachers[0].teacher == dataLoader.blocksOfCCsWithTeachers[1].teacher)
    #input("Digite enter para finalizar.")