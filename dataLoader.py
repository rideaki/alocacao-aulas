from model.entity.classData import ClassData
from model.entity.teacher import Teacher
from model.entity.blockOfTwoHoursAllocation import BlockOfTwoHoursAllocation
from model.utils.daysOfWeek import *
from model.utils.periods import *
from model.utils.shifts import *

# PROFESSORES ##########################################################################################################
__teachers = {}

def _loadTeachers():  # nome e disponibilidade [MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY] 
    __addTeacher("Albertina", [MONDAY, TUESDAY, THURSDAY])	
    __addTeacher("Bruno", [WEDNESDAY, THURSDAY, FRIDAY])	
    __addTeacher("Edival", [WEDNESDAY, THURSDAY])	
    __addTeacher("Eluã", [MONDAY, WEDNESDAY, FRIDAY]) 	
    __addTeacher("Ely", [WEDNESDAY, THURSDAY, FRIDAY])	
    __addTeacher("Erivelton", [WEDNESDAY])	
    __addTeacher("Fabiano", [WEDNESDAY, THURSDAY, FRIDAY])	
    __addTeacher("Gabriela", [WEDNESDAY, THURSDAY, FRIDAY])	
    __addTeacher("Gilvan", [MONDAY, TUESDAY, WEDNESDAY])	
    __addTeacher("Leonardo", [MONDAY, TUESDAY, WEDNESDAY])	
    __addTeacher("Patrícia", [MONDAY, WEDNESDAY])	
    __addTeacher("Paulo", [TUESDAY, WEDNESDAY, THURSDAY])	
    __addTeacher("Reginaldo", [WEDNESDAY, THURSDAY, FRIDAY])	
    __addTeacher("Verônica", [WEDNESDAY, THURSDAY])	

# TURMAS ###############################################################################################################
__classes = []       
# COMPONENTES CURRICULARES ####################################################################################
__blocksOfCCsWithTeachers = []

def _loadClassesAndBlocks():
    # 1° PERIODO ###############################################################################################
    classTecinfoPeriod1Morning = ClassData("Técnico em Informática para Internet", PERIOD_1, MORNING)
    __classes.append(classTecinfoPeriod1Morning)
    classTecinfoPeriod1Afternoon = ClassData("Técnico em Informática para Internet", PERIOD_1, AFTERNOON)
    __classes.append(classTecinfoPeriod1Afternoon)
    
    # turma(dataClass), nome_da_disciplina, carga_horaria_semanal e nome_do_professor         
    __addBlock(classTecinfoPeriod1Morning, "APC", 4, "Gilvan")
    __addBlock(classTecinfoPeriod1Afternoon, "APC", 4, "Gilvan")

    __addBlock(classTecinfoPeriod1Morning, "MDCOO", 4, "Bruno")
    __addBlock(classTecinfoPeriod1Afternoon, "MDCOO", 4, "Bruno")

    __addBlock(classTecinfoPeriod1Morning, "OC", 4, "Gilvan")
    __addBlock(classTecinfoPeriod1Afternoon, "OC", 4, "Gilvan")

    __addBlock(classTecinfoPeriod1Morning, "RC1", 6, "Fabiano")
    __addBlock(classTecinfoPeriod1Afternoon, "RC1", 6, "Fabiano")

    __addBlock(classTecinfoPeriod1Morning, "MPCCD", 4, "Patrícia")
    __addBlock(classTecinfoPeriod1Afternoon, "MPCCD", 4, "Patrícia")

    __addBlock(classTecinfoPeriod1Morning, "EI", 2, "Verônica")
    __addBlock(classTecinfoPeriod1Afternoon, "EI", 2, "Verônica")
    
    # 2° PERIODO ##############################################################################################    
    classTecinfoPeriod2Morning = ClassData("Técnico em Informática para Internet", PERIOD_2, MORNING)
    __classes.append(classTecinfoPeriod2Morning)
    classTecinfoPeriod2Afternoon = ClassData("Técnico em Informática para Internet", PERIOD_2, AFTERNOON)
    __classes.append(classTecinfoPeriod2Afternoon)

    __addBlock(classTecinfoPeriod2Morning, "PIBD", 4, "Ely")
    __addBlock(classTecinfoPeriod2Afternoon, "PIBD", 4, "Ely")

    __addBlock(classTecinfoPeriod2Morning, "ISI", 4, "Bruno")
    __addBlock(classTecinfoPeriod2Afternoon, "ISI", 4, "Bruno")

    __addBlock(classTecinfoPeriod2Morning, "RC2", 4, "Edival")
    __addBlock(classTecinfoPeriod2Afternoon, "RC2", 4, "Edival")

    __addBlock(classTecinfoPeriod2Morning, "PBE1", 6, "Leonardo")
    __addBlock(classTecinfoPeriod2Afternoon, "PBE1", 6, "Leonardo")

    __addBlock(classTecinfoPeriod2Morning, "PFE1", 4, "Reginaldo")
    __addBlock(classTecinfoPeriod2Afternoon, "PFE1", 4, "Reginaldo")

    __addBlock(classTecinfoPeriod2Morning, "IFEI", 2, "Gabriela")
    __addBlock(classTecinfoPeriod2Afternoon, "IFEI", 2, "Gabriela")

    # 3° PERIODO ########################################################################################
    classTecinfoPeriod3Morning = ClassData("Técnico em Informática para Internet", PERIOD_3, MORNING)
    __classes.append(classTecinfoPeriod3Morning)
    classTecinfoPeriod3Afternoon = ClassData("Técnico em Informática para Internet", PERIOD_3, AFTERNOON)
    __classes.append(classTecinfoPeriod3Afternoon)

    __addBlock(classTecinfoPeriod3Morning, "PFE2", 4, "Reginaldo")
    __addBlock(classTecinfoPeriod3Afternoon, "PFE2", 4, "Reginaldo")

    __addBlock(classTecinfoPeriod3Morning, "PBE2", 4, "Eluã")
    __addBlock(classTecinfoPeriod3Afternoon, "PBE2", 4, "Eluã")

    __addBlock(classTecinfoPeriod3Morning, "RC3", 4, "Eluã")
    __addBlock(classTecinfoPeriod3Afternoon, "RC3", 4, "Eluã")

    __addBlock(classTecinfoPeriod3Morning, "GSTI", 4, "Paulo")
    __addBlock(classTecinfoPeriod3Afternoon, "GSTI", 4, "Paulo")

    __addBlock(classTecinfoPeriod3Morning, "SI", 4, "Verônica")
    __addBlock(classTecinfoPeriod3Afternoon, "SI", 4, "Verônica")
    
    __addBlock(classTecinfoPeriod3Morning, "IFE2", 2, "Gabriela")
    __addBlock(classTecinfoPeriod3Afternoon, "IFE2", 2, "Gabriela")

    __addBlock(classTecinfoPeriod3Morning, "EPF", 6, "Albertina")
    __addBlock(classTecinfoPeriod3Afternoon, "EPF", 6, "Albertina")

#####################################################################################################
#### AUXILIAR FUNCTIONS #############################################################################
#####################################################################################################
def loadAllData():
    _loadTeachers()
    _loadClassesAndBlocks()

def getClassesCopy():
    return __classes.copy()

def getClasses():     #cuidado com efeito colateral!
    return __classes

def getTeachersCopy():
    return __teachers.copy()

def getTeachers():    #cuidado com efeito colateral!
    return __teachers

def getBlocksCopy():
    return __blocksOfCCsWithTeachers.copy()

def getBlocks():     #cuidado com efeito colateral!
    return __blocksOfCCsWithTeachers

def __addTeacher(teacherNameArg, availabilitiesArg):
    __teachers[teacherNameArg] = Teacher(teacherNameArg, availabilitiesArg)

def __addBlock(classDataArg, curricularComponentNameArg, weeklyHoursArg, teacherNameArg):
    if(weeklyHoursArg % 2 != 0):
        print ("Carga horária da disciplina " + curricularComponentNameArg + " não é par.")
        exit()
    blocksPerWeek = weeklyHoursArg // 2    #divisão inteira (trunca)
    for i in range(blocksPerWeek):
        __blocksOfCCsWithTeachers.append(__constructBlockOfTwoHours(classDataArg, curricularComponentNameArg, teacherNameArg))

def __constructBlockOfTwoHours(classDataArg, curricularComponentNameArg, teacherNameArg):
    teacher = __searchTeacher(teacherNameArg)
    return BlockOfTwoHoursAllocation(classDataArg, curricularComponentNameArg, teacher)

def __searchTeacher(teacherNameArg):
    if (teacherNameArg not in __teachers):
        print("ERRO! Professor(a) " + teacherNameArg +
              " não cadastrado(a)!!!!!!!!!!!!!!!!!!!!!!!!!")
        input("Digite a tecla <ENTER> para encerrar.")
        exit()
    else:
        return __teachers[teacherNameArg]
