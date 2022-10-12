from model.entity.classData import ClassData
from model.entity.teacher import Teacher
from model.entity.blockOfTwoHoursAllocation import BlockOfTwoHoursAllocation
from model.utils.daysOfWeek import FRIDAY, MONDAY, THURSDAY, TUESDAY, WEDNESDAY
from model.utils.periods import AFTERNOON_PERIOD, MORNING_PERIOD

def loadClasses():
    classes = []
    classes.append(ClassData(1, MORNING_PERIOD))
    classes.append(ClassData(1, AFTERNOON_PERIOD))
    classes.append(ClassData(2, MORNING_PERIOD))
    classes.append(ClassData(2, AFTERNOON_PERIOD))
    classes.append(ClassData(3, MORNING_PERIOD))
    classes.append(ClassData(3, AFTERNOON_PERIOD))
    return classes

def loadTeachers():
    teachers = []
    teachers.append(Teacher ("Albertina", [MONDAY, TUESDAY, THURSDAY]))	
    teachers.append(Teacher ("Bruno", [WEDNESDAY, THURSDAY,FRIDAY]))	
    teachers.append(Teacher ("Edival", [WEDNESDAY, THURSDAY]))	
    teachers.append(Teacher ("Eluã", [MONDAY, WEDNESDAY, FRIDAY])) 	
    teachers.append(Teacher ("Ely", [WEDNESDAY, THURSDAY, FRIDAY]))	
    teachers.append(Teacher ("Erivelton", [WEDNESDAY]))	
    teachers.append(Teacher ("Fabiano", [WEDNESDAY, THURSDAY, FRIDAY]))	
    teachers.append(Teacher ("Gabriela", [WEDNESDAY, THURSDAY, FRIDAY]))	
    teachers.append(Teacher ("Gilvan", [MONDAY, TUESDAY, WEDNESDAY]))	
    teachers.append(Teacher ("Leonardo", [MONDAY, TUESDAY, WEDNESDAY]))	
    teachers.append(Teacher ("Patrícia", [MONDAY, WEDNESDAY]))	
    teachers.append(Teacher ("Paulo", [TUESDAY, WEDNESDAY, THURSDAY]))	
    teachers.append(Teacher ("Reginaldo", [WEDNESDAY, THURSDAY, FRIDAY]))	
    teachers.append(Teacher ("Verônica", [WEDNESDAY, THURSDAY]))	
    return teachers

def loadBlocksOfCurricularComponentWithTeachers():
    blocksOfCCsWithTeachers = []
    
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("APC", 1, MORNING_PERIOD, "Gilvan"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("APC", 1, MORNING_PERIOD, "Gilvan"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("APC", 1, AFTERNOON_PERIOD, "Gilvan"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("APC", 1, AFTERNOON_PERIOD, "Gilvan"))

    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("MDCOO", 1, MORNING_PERIOD, "Bruno"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("MDCOO", 1, MORNING_PERIOD, "Bruno"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("MDCOO", 1, MORNING_PERIOD, "Bruno"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("MDCOO", 1, AFTERNOON_PERIOD, "Bruno"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("MDCOO", 1, AFTERNOON_PERIOD, "Bruno"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("MDCOO", 1, AFTERNOON_PERIOD, "Bruno"))

    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("OC", 1, MORNING_PERIOD, "Gilvan"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("OC", 1, MORNING_PERIOD, "Gilvan"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("OC", 1, AFTERNOON_PERIOD, "Gilvan"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("OC", 1, AFTERNOON_PERIOD, "Gilvan"))

    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("RC1", 1, MORNING_PERIOD, "Fabiano"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("RC1", 1, MORNING_PERIOD, "Fabiano"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("RC1", 1, MORNING_PERIOD, "Fabiano"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("RC1", 1, AFTERNOON_PERIOD, "Fabiano"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("RC1", 1, AFTERNOON_PERIOD, "Fabiano"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("RC1", 1, AFTERNOON_PERIOD, "Fabiano"))

    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("MPCCD", 1, MORNING_PERIOD, "Patrícia"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("MPCCD", 1, MORNING_PERIOD, "Patrícia"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("MPCCD", 1, AFTERNOON_PERIOD, "Patrícia"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("MPCCD", 1, AFTERNOON_PERIOD, "Patrícia"))

    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("EI", 1, MORNING_PERIOD, "Verônica"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("EI", 1, MORNING_PERIOD, "Verônica"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("EI", 1, AFTERNOON_PERIOD, "Verônica"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("EI", 1, AFTERNOON_PERIOD, "Verônica"))
    
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("PIBD", 2, MORNING_PERIOD, "Ely"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("PIBD", 2, MORNING_PERIOD, "Ely"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("PIBD", 2, AFTERNOON_PERIOD, "Ely"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("PIBD", 2, AFTERNOON_PERIOD, "Ely"))

    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("ISI", 2, MORNING_PERIOD, "Bruno"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("ISI", 2, MORNING_PERIOD, "Bruno"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("ISI", 2, AFTERNOON_PERIOD, "Bruno"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("ISI", 2, AFTERNOON_PERIOD, "Bruno"))    

    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("RC2", 2, MORNING_PERIOD, "Edival"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("RC2", 2, MORNING_PERIOD, "Edival"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("RC2", 2, AFTERNOON_PERIOD, "Edival"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("RC2", 2, AFTERNOON_PERIOD, "Edival")) 

    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("PBE1", 2, MORNING_PERIOD, "Leonardo"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("PBE1", 2, MORNING_PERIOD, "Leonardo"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("PBE1", 2, AFTERNOON_PERIOD, "Leonardo"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("PBE1", 2, AFTERNOON_PERIOD, "Leonardo"))

    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("PFE1", 2, MORNING_PERIOD, "Reginaldo"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("PFE1", 2, MORNING_PERIOD, "Reginaldo"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("PFE1", 2, AFTERNOON_PERIOD, "Reginaldo"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("PFE1", 2, AFTERNOON_PERIOD, "Reginaldo"))

    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("IFEI", 2, MORNING_PERIOD, "Gabriela"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("IFEI", 2, AFTERNOON_PERIOD, "Gabriela"))

    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("PFE2", 3, MORNING_PERIOD, "Reginaldo"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("PFE2", 3, MORNING_PERIOD, "Reginaldo"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("PFE2", 3, AFTERNOON_PERIOD, "Reginaldo"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("PFE2", 3, AFTERNOON_PERIOD, "Reginaldo"))

    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("PBE2", 3, MORNING_PERIOD, "Eluã"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("PBE2", 3, MORNING_PERIOD, "Eluã"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("PBE2", 3, AFTERNOON_PERIOD, "Eluã"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("PBE2", 3, AFTERNOON_PERIOD, "Eluã"))

    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("RC3", 3, MORNING_PERIOD, "Eluã"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("RC3", 3, MORNING_PERIOD, "Eluã"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("RC3", 3, AFTERNOON_PERIOD, "Eluã"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("RC3", 3, AFTERNOON_PERIOD, "Eluã"))

    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("GSTI", 3, MORNING_PERIOD, "Paulo"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("GSTI", 3, MORNING_PERIOD, "Paulo"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("GSTI", 3, AFTERNOON_PERIOD, "Paulo"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("GSTI", 3, AFTERNOON_PERIOD, "Paulo"))

    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("SI", 3, MORNING_PERIOD, "Verônica"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("SI", 3, MORNING_PERIOD, "Verônica"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("SI", 3, AFTERNOON_PERIOD, "Verônica"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("SI", 3, AFTERNOON_PERIOD, "Verônica"))
    
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("IFE2", 3, MORNING_PERIOD, "Gabriela"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("IFE2", 3, AFTERNOON_PERIOD, "Gabriela"))

    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("EPF", 3, MORNING_PERIOD, "Albertina"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("EPF", 3, MORNING_PERIOD, "Albertina"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("EPF", 3, AFTERNOON_PERIOD, "Albertina"))
    blocksOfCCsWithTeachers.append(BlockOfTwoHoursAllocation("EPF", 3, AFTERNOON_PERIOD, "Albertina"))

    return blocksOfCCsWithTeachers
