from model.entity.classData import ClassData
from model.entity.teacher import Teacher
from model.entity.blockOfTwoHoursAllocation import BlockOfTwoHoursAllocation
from model.utils.daysOfWeek import FRIDAY, MONDAY, THURSDAY, TUESDAY, WEDNESDAY
from model.utils.shifts import AFTERNOON, MORNING

classes = []

def loadClasses():
    classes.append(ClassData(1, MORNING))
    classes.append(ClassData(1, AFTERNOON))
    classes.append(ClassData(2, MORNING))
    classes.append(ClassData(2, AFTERNOON))
    classes.append(ClassData(3, MORNING))
    classes.append(ClassData(3, AFTERNOON))

def addTeacher(teacherNameArg, availabilitiesArg):
    teachers[teacherNameArg] = Teacher(teacherNameArg, availabilitiesArg)

teachers = {}

def loadTeachers():
    addTeacher("Albertina", [MONDAY, TUESDAY, THURSDAY])	
    addTeacher("Bruno", [WEDNESDAY, THURSDAY,FRIDAY])	
    addTeacher("Edival", [WEDNESDAY, THURSDAY])	
    addTeacher("Eluã", [MONDAY, WEDNESDAY, FRIDAY]) 	
    addTeacher("Ely", [WEDNESDAY, THURSDAY, FRIDAY])	
    addTeacher("Erivelton", [WEDNESDAY])	
    addTeacher("Fabiano", [WEDNESDAY, THURSDAY, FRIDAY])	
    addTeacher("Gabriela", [WEDNESDAY, THURSDAY, FRIDAY])	
    addTeacher("Gilvan", [MONDAY, TUESDAY, WEDNESDAY])	
    addTeacher("Leonardo", [MONDAY, TUESDAY, WEDNESDAY])	
    addTeacher("Patrícia", [MONDAY, WEDNESDAY])	
    addTeacher("Paulo", [TUESDAY, WEDNESDAY, THURSDAY])	
    addTeacher("Reginaldo", [WEDNESDAY, THURSDAY, FRIDAY])	
    addTeacher("Verônica", [WEDNESDAY, THURSDAY])	


def searchTeacher(teacherNameArg):
    if (teacherNameArg not in teachers):
        print("ERRO! Professor(a) " + teacherNameArg +
              " não cadastrado(a)!!!!!!!!!!!!!!!!!!!!!!!!!")
        input("Digite a tecla <ENTER> para encerrar.")
        exit()
    else:
        return teachers[teacherNameArg];

def constructBlockOfTwoHours(curricularComponentNameArg, semesterNumberArg, shiftArg, teacherNameArg):
    teacher = searchTeacher(teacherNameArg)
    return BlockOfTwoHoursAllocation(curricularComponentNameArg, semesterNumberArg, shiftArg, teacher)

blocksOfCCsWithTeachers = []
def loadBlocksOfCurricularComponentWithTeachers():
    
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("APC", 1, MORNING, "Gilvan"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("APC", 1, MORNING, "Gilvan"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("APC", 1, AFTERNOON, "Gilvan"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("APC", 1, AFTERNOON, "Gilvan"))

    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("MDCOO", 1, MORNING, "Bruno"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("MDCOO", 1, MORNING, "Bruno"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("MDCOO", 1, MORNING, "Bruno"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("MDCOO", 1, AFTERNOON, "Bruno"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("MDCOO", 1, AFTERNOON, "Bruno"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("MDCOO", 1, AFTERNOON, "Bruno"))

    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("OC", 1, MORNING, "Gilvan"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("OC", 1, MORNING, "Gilvan"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("OC", 1, AFTERNOON, "Gilvan"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("OC", 1, AFTERNOON, "Gilvan"))

    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("RC1", 1, MORNING, "Fabiano"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("RC1", 1, MORNING, "Fabiano"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("RC1", 1, MORNING, "Fabiano"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("RC1", 1, AFTERNOON, "Fabiano"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("RC1", 1, AFTERNOON, "Fabiano"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("RC1", 1, AFTERNOON, "Fabiano"))

    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("MPCCD", 1, MORNING, "Patrícia"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("MPCCD", 1, MORNING, "Patrícia"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("MPCCD", 1, AFTERNOON, "Patrícia"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("MPCCD", 1, AFTERNOON, "Patrícia"))

    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("EI", 1, MORNING, "Verônica"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("EI", 1, MORNING, "Verônica"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("EI", 1, AFTERNOON, "Verônica"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("EI", 1, AFTERNOON, "Verônica"))
    
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("PIBD", 2, MORNING, "Ely"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("PIBD", 2, MORNING, "Ely"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("PIBD", 2, AFTERNOON, "Ely"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("PIBD", 2, AFTERNOON, "Ely"))

    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("ISI", 2, MORNING, "Bruno"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("ISI", 2, MORNING, "Bruno"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("ISI", 2, AFTERNOON, "Bruno"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("ISI", 2, AFTERNOON, "Bruno"))    

    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("RC2", 2, MORNING, "Edival"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("RC2", 2, MORNING, "Edival"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("RC2", 2, AFTERNOON, "Edival"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("RC2", 2, AFTERNOON, "Edival")) 

    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("PBE1", 2, MORNING, "Leonardo"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("PBE1", 2, MORNING, "Leonardo"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("PBE1", 2, AFTERNOON, "Leonardo"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("PBE1", 2, AFTERNOON, "Leonardo"))

    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("PFE1", 2, MORNING, "Reginaldo"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("PFE1", 2, MORNING, "Reginaldo"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("PFE1", 2, AFTERNOON, "Reginaldo"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("PFE1", 2, AFTERNOON, "Reginaldo"))

    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("IFEI", 2, MORNING, "Gabriela"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("IFEI", 2, AFTERNOON, "Gabriela"))

    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("PFE2", 3, MORNING, "Reginaldo"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("PFE2", 3, MORNING, "Reginaldo"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("PFE2", 3, AFTERNOON, "Reginaldo"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("PFE2", 3, AFTERNOON, "Reginaldo"))

    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("PBE2", 3, MORNING, "Eluã"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("PBE2", 3, MORNING, "Eluã"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("PBE2", 3, AFTERNOON, "Eluã"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("PBE2", 3, AFTERNOON, "Eluã"))

    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("RC3", 3, MORNING, "Eluã"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("RC3", 3, MORNING, "Eluã"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("RC3", 3, AFTERNOON, "Eluã"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("RC3", 3, AFTERNOON, "Eluã"))

    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("GSTI", 3, MORNING, "Paulo"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("GSTI", 3, MORNING, "Paulo"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("GSTI", 3, AFTERNOON, "Paulo"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("GSTI", 3, AFTERNOON, "Paulo"))

    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("SI", 3, MORNING, "Verônica"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("SI", 3, MORNING, "Verônica"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("SI", 3, AFTERNOON, "Verônica"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("SI", 3, AFTERNOON, "Verônica"))
    
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("IFE2", 3, MORNING, "Gabriela"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("IFE2", 3, AFTERNOON, "Gabriela"))

    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("EPF", 3, MORNING, "Albertina"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("EPF", 3, MORNING, "Albertina"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("EPF", 3, AFTERNOON, "Albertina"))
    blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("EPF", 3, AFTERNOON, "Albertina"))

