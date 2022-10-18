from model.entity.classData import ClassData
from model.entity.teacher import Teacher
from model.entity.blockOfTwoHoursAllocation import BlockOfTwoHoursAllocation
from model.utils.daysOfWeek import *
from model.utils.periods import *
from model.utils.shifts import *

# TURMAS ###############################################################################################################
__classes = []       

def _loadClasses():   # semestre (1, 2, ...) e turno (MORNING, AFTERNOON, NIGHT)
    __classes.append(ClassData(PERIOD_1, MORNING))
    __classes.append(ClassData(PERIOD_1, AFTERNOON))
    __classes.append(ClassData(PERIOD_2, MORNING))
    __classes.append(ClassData(PERIOD_2, AFTERNOON))
    __classes.append(ClassData(PERIOD_3, MORNING))
    __classes.append(ClassData(PERIOD_3, AFTERNOON))

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

# COMPONENTES CURRICULARES ####################################################################################
__blocksOfCCsWithTeachers = []

def _loadCurricularComponentTeachers():  
    # semestre, nome_da_disciplina, turno(MORNING, AFTERNOON, NIGHT), carga_horaria_semanal e nome_do_professor         
    __addBlock(PERIOD_1, "APC", MORNING, 4, "Gilvan")
    __addBlock(PERIOD_1, "APC", AFTERNOON, 4, "Gilvan")

    __addBlock(PERIOD_1, "MDCOO", MORNING, 4, "Bruno")
    __addBlock(PERIOD_1, "MDCOO", AFTERNOON, 4, "Bruno")

    __addBlock(PERIOD_1, "OC", MORNING, 4, "Gilvan")
    __addBlock(PERIOD_1, "OC", AFTERNOON, 4, "Gilvan")

    __addBlock(PERIOD_1, "RC1", MORNING, 6, "Fabiano")
    __addBlock(PERIOD_1, "RC1", AFTERNOON, 6, "Fabiano")

    __addBlock(PERIOD_1, "MPCCD", MORNING, 4, "Patrícia")
    __addBlock(PERIOD_1, "MPCCD", AFTERNOON, 4, "Patrícia")

    __addBlock(PERIOD_1, "EI", MORNING, 2, "Verônica")
    __addBlock(PERIOD_1, "EI", AFTERNOON, 2, "Verônica")
    
    __addBlock(PERIOD_2, "PIBD", MORNING, 4, "Ely")
    __addBlock(PERIOD_2, "PIBD", AFTERNOON, 4, "Ely")

    __addBlock(PERIOD_2, "ISI", MORNING, 4, "Bruno")
    __addBlock(PERIOD_2, "ISI", AFTERNOON, 4, "Bruno")

    __addBlock(PERIOD_2, "RC2", MORNING, 4, "Edival")
    __addBlock(PERIOD_2, "RC2", AFTERNOON, 4, "Edival")

    __addBlock(PERIOD_2, "PBE1", MORNING, 6, "Leonardo")
    __addBlock(PERIOD_2, "PBE1", AFTERNOON, 6, "Leonardo")

    __addBlock(PERIOD_2, "PFE1", MORNING, 4, "Reginaldo")
    __addBlock(PERIOD_2, "PFE1", AFTERNOON, 4, "Reginaldo")

    __addBlock(PERIOD_2, "IFEI", MORNING, 2, "Gabriela")
    __addBlock(PERIOD_2, "IFEI", AFTERNOON, 2, "Gabriela")

    __addBlock(PERIOD_3, "PFE2",MORNING, 4, "Reginaldo")
    __addBlock(PERIOD_3, "PFE2",AFTERNOON, 4, "Reginaldo")

    __addBlock(PERIOD_3, "PBE2", MORNING, 4, "Eluã")
    __addBlock(PERIOD_3, "PBE2", AFTERNOON, 4, "Eluã")

    __addBlock(PERIOD_3, "RC3", MORNING, 4, "Eluã")
    __addBlock(PERIOD_3, "RC3", AFTERNOON, 4, "Eluã")

    __addBlock(PERIOD_3, "GSTI", MORNING, 4, "Paulo")
    __addBlock(PERIOD_3, "GSTI", AFTERNOON, 4, "Paulo")

    __addBlock(PERIOD_3, "SI", MORNING, 4, "Verônica")
    __addBlock(PERIOD_3, "SI", AFTERNOON, 4, "Verônica")
    
    __addBlock(PERIOD_3, "IFE2", MORNING, 2, "Gabriela")
    __addBlock(PERIOD_3, "IFE2", AFTERNOON, 2, "Gabriela")

    __addBlock(PERIOD_3, "EPF", MORNING, 6, "Albertina")
    __addBlock(PERIOD_3, "EPF", AFTERNOON, 6, "Albertina")

#####################################################################################################
#### AUXILIAR FUNCTIONS #############################################################################
#####################################################################################################
def loadAllData():
    _loadClasses()
    _loadTeachers()
    _loadCurricularComponentTeachers()

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

def __addBlock(semesterNumberArg, curricularComponentNameArg, shiftArg, weeklyHoursArg, teacherNameArg):
    if(weeklyHoursArg % 2 != 0):
        print ("Carga horária da disciplina " + curricularComponentNameArg + " do " + str(semesterNumberArg) + " não é par.")
        exit()
    blocksPerWeek = weeklyHoursArg // 2    #divisão inteira (trunca)
    for i in range(blocksPerWeek):
        __blocksOfCCsWithTeachers.append(__constructBlockOfTwoHours(semesterNumberArg, curricularComponentNameArg, shiftArg, teacherNameArg))


def __constructBlockOfTwoHours(semesterNumberArg, curricularComponentNameArg, shiftArg, teacherNameArg):
    teacher = __searchTeacher(teacherNameArg)
    return BlockOfTwoHoursAllocation(curricularComponentNameArg, semesterNumberArg, shiftArg, teacher)

def __searchTeacher(teacherNameArg):
    if (teacherNameArg not in __teachers):
        print("ERRO! Professor(a) " + teacherNameArg +
              " não cadastrado(a)!!!!!!!!!!!!!!!!!!!!!!!!!")
        input("Digite a tecla <ENTER> para encerrar.")
        exit()
    else:
        return __teachers[teacherNameArg]
