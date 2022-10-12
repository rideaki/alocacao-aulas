from dataLoader import loadClasses, loadTeachers
from model.entity.teacher import Teacher
from model.utils.daysOfWeek import FRIDAY, MONDAY, SATURDAY, THURSDAY, TUESDAY, WEDNESDAY

if __name__ == '__main__':
    teachers = loadTeachers()
    print(teachers)
    classes = loadClasses()
    print(classes)
    #input("Digite enter para finalizar.")