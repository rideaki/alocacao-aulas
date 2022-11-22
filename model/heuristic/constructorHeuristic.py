import copy
import model.loader.dataLoader as dataLoader
import numpy
import random
import warnings
from model.business import filter
from model.business.tableFactory import constructClassTable


def constructHeusristicSolution():
    timeTables = {}
    filteredBlocksIndexesByClass = {}
    __constructTeachersAvailabilitiesBlocks()

    # Para cada turma
    classes = dataLoader.getClassesCopy()
    while len(classes) > 0:
        classData = random.choice(classes)
        classes.remove(classData)
        timeTables[classData] = copy.deepcopy(constructClassTable(None))
        filteredBlocksIndexesByClass[classData] = copy.deepcopy(
            filter.filterBlocksIndexesByClassData(dataLoader.getBlocks(), classData)
        )
        __allocateTeachersBlocks(timeTables, filteredBlocksIndexesByClass, classData)
    return timeTables

def __allocateTeachersBlocks(timeTables, filteredBlocksIndexesByClass, classData):
    teachers = dataLoader.getTeachersCopy()
    # Para cada professor
    while len(teachers) > 0:
        teacher = teachers.pop(random.choice(list(teachers)))
        teacherBlocksToBeAllocated = copy.deepcopy(
                filter.filterBlocksIndexesByTeacher(filteredBlocksIndexesByClass[classData], teacher.name)
            )
        availableTeacherBlocksByShift = teacher.getAllSortedBlocksCopy()[classData.shift]
        while len(teacherBlocksToBeAllocated) > 0:
            allocated = False
            classTimeTable = timeTables[classData]
            for teacherAvailableBlock in availableTeacherBlocksByShift:
                if(classTimeTable[teacherAvailableBlock[0]][teacherAvailableBlock[1]] == None):
                        #alocar aula
                    classTimeTable[teacherAvailableBlock[0]][teacherAvailableBlock[1]] = teacherBlocksToBeAllocated.pop(0)
                    availableTeacherBlocksByShift.remove(teacherAvailableBlock)
                    allocated = True
                    break  # sai do laco -> for teacherAvailableBlock in availableTeacherBlocksByShift:

            __allocateBlocksWithConflicts(classData, teacherBlocksToBeAllocated, allocated, classTimeTable)

# constroi as disponibilidades (por blocos) do professor
def __constructTeachersAvailabilitiesBlocks():
    for teacher in dataLoader.getTeachersCopy().values():
        teacher.constructSortedBlocks()  

def __allocateBlocksWithConflicts(classData, teacherBlocksToBeAllocated, allocated, classTimeTable):
    if not allocated:
        # Se chegar neste ponto, não será possível alocar o bloco sem conflito de horário.
        # pois o professor não tem disponibilidade, nos horários disponíveis da turma.
        # Portanto, alocar a aula em qualquer horário disponível da turma.
        try:
            availableIndex = numpy.where(numpy.array(classTimeTable) == None)
            classTimeTable[int(availableIndex[0][0])][
                            int(availableIndex[1][0])
                        ] = teacherBlocksToBeAllocated.pop(0)
        except:
            # Quantidade de disciplinas, excede CH da turma! 
            # Sugestão ao usuário: configurar aula no contraturno 
            teacherBlocksToBeAllocated.pop(0)
            warnings.warn(
                            "Não foi possível alocar todas as aulas na turma: "
                            + str(classData.periodNumber)
                            + " "
                            + str(classData.shift)
                            + " - "
                            + str(classData.courseName)
                            + "\n Sugestão: CONFIGURAR AULAS PARA SEREM ALOCADAS NO CONTRATURNO."
                        )
            exit()
