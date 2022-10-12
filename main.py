from model.entity.teacher import Teacher
from model.utils.daysOfWeek import FRIDAY, MONDAY, SATURDAY, THURSDAY, TUESDAY, WEDNESDAY

def main():
    print ("Olá mundo!")

if __name__ == '__main__':
    teachers = []
    teachers.append(Teacher ("Albertina", [MONDAY, TUESDAY, THURSDAY]))	
    teachers.append(Teacher ("Gilvan", [MONDAY, TUESDAY, WEDNESDAY]))	
    teachers.append(Teacher ("Bruno", [WEDNESDAY, THURSDAY,FRIDAY]))	
    teachers.append(Teacher ("Fabiano", [WEDNESDAY, THURSDAY, FRIDAY]))	
    teachers.append(Teacher ("Patrícia", [MONDAY, WEDNESDAY]))	
    teachers.append(Teacher ("Verônica", [WEDNESDAY, THURSDAY]))	
    teachers.append(Teacher ("Ely", [WEDNESDAY, THURSDAY, FRIDAY]))	
    teachers.append(Teacher ("Edival", [WEDNESDAY, THURSDAY]))	
    teachers.append(Teacher ("Leonardo", [MONDAY, TUESDAY, WEDNESDAY]))	
    teachers.append(Teacher ("Erivelton", [WEDNESDAY]))	
    teachers.append(Teacher ("Gabriela", [WEDNESDAY, THURSDAY, FRIDAY]))	
    teachers.append(Teacher ("Reginaldo", [WEDNESDAY, THURSDAY, FRIDAY]))	
    teachers.append(Teacher ("Eluã", [MONDAY, WEDNESDAY, FRIDAY])) 	
    teachers.append(Teacher ("Paulo", [TUESDAY, WEDNESDAY, THURSDAY]))	
    print(teachers)
    #input("Digite enter para finalizar.")