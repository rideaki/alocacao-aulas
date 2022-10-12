from model.entity.teacher import Teacher
from model.utils.daysOfWeek import FRIDAY, MONDAY, SATURDAY, THURSDAY, TUESDAY, WEDNESDAY

def main():
    print ("Olá mundo!")

if __name__ == '__main__':
    teacherReginaldo = Teacher ("Reginaldo R.K.", [MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY])
    print(teacherReginaldo.name)
    print(teacherReginaldo.availabilities)
    input("Digite enter para finalizar.")