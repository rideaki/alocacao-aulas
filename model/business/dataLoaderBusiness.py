
import dataLoader
from model.entity.blockOfTwoHoursAllocation import BlockOfTwoHoursAllocation
from model.entity.teacher import Teacher

def addTeacher(teacherNameArg, availabilitiesArg):
    dataLoader.__teachers[teacherNameArg] = Teacher(teacherNameArg, availabilitiesArg)

def searchTeacher(teacherNameArg):
    if (teacherNameArg not in dataLoader.__teachers):
        print("ERRO! Professor(a) " + teacherNameArg +
              " não cadastrado(a)!!!!!!!!!!!!!!!!!!!!!!!!!")
        input("Digite a tecla <ENTER> para encerrar.")
        exit()
    else:
        return dataLoader.__teachers[teacherNameArg]

def constructBlockOfTwoHours(curricularComponentNameArg, semesterNumberArg, shiftArg, teacherNameArg):
    teacher = searchTeacher(teacherNameArg)
    return BlockOfTwoHoursAllocation(curricularComponentNameArg, semesterNumberArg, shiftArg, teacher)
