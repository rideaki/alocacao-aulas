from numpy import array
from model.entity.classData import ClassData
from model.entity.teacher import Teacher
from model.entity.blockOfTwoHoursAllocation import BlockOfTwoHoursAllocation
from model.utils.daysOfWeek import FRIDAY, MONDAY, THURSDAY, TUESDAY, WEDNESDAY
from model.utils.shifts import AFTERNOON, MORNING

__classes = []

def loadClasses():
    __classes.append(ClassData(1, MORNING))
    __classes.append(ClassData(1, AFTERNOON))
    __classes.append(ClassData(2, MORNING))
    __classes.append(ClassData(2, AFTERNOON))
    __classes.append(ClassData(3, MORNING))
    __classes.append(ClassData(3, AFTERNOON))


__teachers = {}

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

__blocksOfCCsWithTeachers = []

def loadBlocksOfCurricularComponentWithTeachers():
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("APC", 1, MORNING, "Gilvan"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("APC", 1, MORNING, "Gilvan"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("APC", 1, AFTERNOON, "Gilvan"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("APC", 1, AFTERNOON, "Gilvan"))

    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("MDCOO", 1, MORNING, "Bruno"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("MDCOO", 1, MORNING, "Bruno"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("MDCOO", 1, MORNING, "Bruno"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("MDCOO", 1, AFTERNOON, "Bruno"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("MDCOO", 1, AFTERNOON, "Bruno"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("MDCOO", 1, AFTERNOON, "Bruno"))

    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("OC", 1, MORNING, "Gilvan"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("OC", 1, MORNING, "Gilvan"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("OC", 1, AFTERNOON, "Gilvan"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("OC", 1, AFTERNOON, "Gilvan"))

    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("RC1", 1, MORNING, "Fabiano"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("RC1", 1, MORNING, "Fabiano"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("RC1", 1, MORNING, "Fabiano"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("RC1", 1, AFTERNOON, "Fabiano"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("RC1", 1, AFTERNOON, "Fabiano"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("RC1", 1, AFTERNOON, "Fabiano"))

    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("MPCCD", 1, MORNING, "Patrícia"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("MPCCD", 1, MORNING, "Patrícia"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("MPCCD", 1, AFTERNOON, "Patrícia"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("MPCCD", 1, AFTERNOON, "Patrícia"))

    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("EI", 1, MORNING, "Verônica"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("EI", 1, MORNING, "Verônica"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("EI", 1, AFTERNOON, "Verônica"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("EI", 1, AFTERNOON, "Verônica"))
    
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("PIBD", 2, MORNING, "Ely"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("PIBD", 2, MORNING, "Ely"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("PIBD", 2, AFTERNOON, "Ely"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("PIBD", 2, AFTERNOON, "Ely"))

    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("ISI", 2, MORNING, "Bruno"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("ISI", 2, MORNING, "Bruno"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("ISI", 2, AFTERNOON, "Bruno"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("ISI", 2, AFTERNOON, "Bruno"))    

    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("RC2", 2, MORNING, "Edival"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("RC2", 2, MORNING, "Edival"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("RC2", 2, AFTERNOON, "Edival"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("RC2", 2, AFTERNOON, "Edival")) 

    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("PBE1", 2, MORNING, "Leonardo"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("PBE1", 2, MORNING, "Leonardo"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("PBE1", 2, AFTERNOON, "Leonardo"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("PBE1", 2, AFTERNOON, "Leonardo"))

    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("PFE1", 2, MORNING, "Reginaldo"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("PFE1", 2, MORNING, "Reginaldo"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("PFE1", 2, AFTERNOON, "Reginaldo"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("PFE1", 2, AFTERNOON, "Reginaldo"))

    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("IFEI", 2, MORNING, "Gabriela"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("IFEI", 2, AFTERNOON, "Gabriela"))

    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("PFE2", 3, MORNING, "Reginaldo"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("PFE2", 3, MORNING, "Reginaldo"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("PFE2", 3, AFTERNOON, "Reginaldo"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("PFE2", 3, AFTERNOON, "Reginaldo"))

    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("PBE2", 3, MORNING, "Eluã"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("PBE2", 3, MORNING, "Eluã"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("PBE2", 3, AFTERNOON, "Eluã"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("PBE2", 3, AFTERNOON, "Eluã"))

    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("RC3", 3, MORNING, "Eluã"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("RC3", 3, MORNING, "Eluã"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("RC3", 3, AFTERNOON, "Eluã"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("RC3", 3, AFTERNOON, "Eluã"))

    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("GSTI", 3, MORNING, "Paulo"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("GSTI", 3, MORNING, "Paulo"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("GSTI", 3, AFTERNOON, "Paulo"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("GSTI", 3, AFTERNOON, "Paulo"))

    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("SI", 3, MORNING, "Verônica"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("SI", 3, MORNING, "Verônica"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("SI", 3, AFTERNOON, "Verônica"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("SI", 3, AFTERNOON, "Verônica"))
    
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("IFE2", 3, MORNING, "Gabriela"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("IFE2", 3, AFTERNOON, "Gabriela"))

    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("EPF", 3, MORNING, "Albertina"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("EPF", 3, MORNING, "Albertina"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("EPF", 3, AFTERNOON, "Albertina"))
    __blocksOfCCsWithTeachers.append(constructBlockOfTwoHours("EPF", 3, AFTERNOON, "Albertina"))

#####################################################################################################
#### AUXILIAR FUNCTIONS #############################################################################
#####################################################################################################

def getClassesCopy():
    return __classes.copy()

def getClasses():     #cuidado com efeito colateral!
    return __classes

def getTeachersCopy():
    return __teachers.copy()

def getTeachers():    #cuidado com efeito colateral!
    return __teachers

def getBlocksOfCCsWithTeachersCopy():
    return __blocksOfCCsWithTeachers.copy()

def getBlocksOfCCsWithTeachers():     #cuidado com efeito colateral!
    return __blocksOfCCsWithTeachers

def addTeacher(teacherNameArg, availabilitiesArg):
    __teachers[teacherNameArg] = Teacher(teacherNameArg, availabilitiesArg)

def searchTeacher(teacherNameArg):
    if (teacherNameArg not in __teachers):
        print("ERRO! Professor(a) " + teacherNameArg +
              " não cadastrado(a)!!!!!!!!!!!!!!!!!!!!!!!!!")
        input("Digite a tecla <ENTER> para encerrar.")
        exit()
    else:
        return __teachers[teacherNameArg]

def constructBlockOfTwoHours(curricularComponentNameArg, semesterNumberArg, shiftArg, teacherNameArg):
    teacher = searchTeacher(teacherNameArg)
    return BlockOfTwoHoursAllocation(curricularComponentNameArg, semesterNumberArg, shiftArg, teacher)