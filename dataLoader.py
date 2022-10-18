from model.entity.classData import ClassData
from model.entity.teacher import Teacher
from model.entity.blockOfTwoHoursAllocation import BlockOfTwoHoursAllocation
from model.utils.daysOfWeek import *
from model.utils.periods import *
from model.utils.shifts import *

# TURMAS ###############################################################################################################
__classes = []


def _load_classes():  # semestre (1, 2, ...) e turno (MORNING, AFTERNOON, NIGHT)
    __classes.append(ClassData(PERIOD_1, MORNING))
    __classes.append(ClassData(PERIOD_1, AFTERNOON))
    __classes.append(ClassData(PERIOD_2, MORNING))
    __classes.append(ClassData(PERIOD_2, AFTERNOON))
    __classes.append(ClassData(PERIOD_3, MORNING))
    __classes.append(ClassData(PERIOD_3, AFTERNOON))


# PROFESSORES ##########################################################################################################
__teachers = {}


def _load_teachers():  # nome e disponibilidade [MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY]
    __add_teacher("Albertina", [MONDAY, TUESDAY, THURSDAY])
    __add_teacher("Bruno", [WEDNESDAY, THURSDAY, FRIDAY])
    __add_teacher("Edival", [WEDNESDAY, THURSDAY])
    __add_teacher("Eluã", [MONDAY, WEDNESDAY, FRIDAY])
    __add_teacher("Ely", [WEDNESDAY, THURSDAY, FRIDAY])
    __add_teacher("Erivelton", [WEDNESDAY])
    __add_teacher("Fabiano", [WEDNESDAY, THURSDAY, FRIDAY])
    __add_teacher("Gabriela", [WEDNESDAY, THURSDAY, FRIDAY])
    __add_teacher("Gilvan", [MONDAY, TUESDAY, WEDNESDAY])
    __add_teacher("Leonardo", [MONDAY, TUESDAY, WEDNESDAY])
    __add_teacher("Patrícia", [MONDAY, WEDNESDAY])
    __add_teacher("Paulo", [TUESDAY, WEDNESDAY, THURSDAY])
    __add_teacher("Reginaldo", [WEDNESDAY, THURSDAY, FRIDAY])
    __add_teacher("Verônica", [WEDNESDAY, THURSDAY])


# COMPONENTES CURRICULARES ####################################################################################
__blocksOfCCsWithTeachers = []


def _load_curricular_component_teachers():
    # semestre, nome_da_disciplina, turno(MORNING, AFTERNOON, NIGHT), carga_horaria_semanal e nome_do_professor         
    __add_block(PERIOD_1, "APC", MORNING, 4, "Gilvan")
    __add_block(PERIOD_1, "APC", AFTERNOON, 4, "Gilvan")

    __add_block(PERIOD_1, "MDCOO", MORNING, 4, "Bruno")
    __add_block(PERIOD_1, "MDCOO", AFTERNOON, 4, "Bruno")

    __add_block(PERIOD_1, "OC", MORNING, 4, "Gilvan")
    __add_block(PERIOD_1, "OC", AFTERNOON, 4, "Gilvan")

    __add_block(PERIOD_1, "RC1", MORNING, 6, "Fabiano")
    __add_block(PERIOD_1, "RC1", AFTERNOON, 6, "Fabiano")

    __add_block(PERIOD_1, "MPCCD", MORNING, 4, "Patrícia")
    __add_block(PERIOD_1, "MPCCD", AFTERNOON, 4, "Patrícia")

    __add_block(PERIOD_1, "EI", MORNING, 2, "Verônica")
    __add_block(PERIOD_1, "EI", AFTERNOON, 2, "Verônica")

    __add_block(PERIOD_2, "PIBD", MORNING, 4, "Ely")
    __add_block(PERIOD_2, "PIBD", AFTERNOON, 4, "Ely")

    __add_block(PERIOD_2, "ISI", MORNING, 4, "Bruno")
    __add_block(PERIOD_2, "ISI", AFTERNOON, 4, "Bruno")

    __add_block(PERIOD_2, "RC2", MORNING, 4, "Edival")
    __add_block(PERIOD_2, "RC2", AFTERNOON, 4, "Edival")

    __add_block(PERIOD_2, "PBE1", MORNING, 6, "Leonardo")
    __add_block(PERIOD_2, "PBE1", AFTERNOON, 6, "Leonardo")

    __add_block(PERIOD_2, "PFE1", MORNING, 4, "Reginaldo")
    __add_block(PERIOD_2, "PFE1", AFTERNOON, 4, "Reginaldo")

    __add_block(PERIOD_2, "IFEI", MORNING, 2, "Gabriela")
    __add_block(PERIOD_2, "IFEI", AFTERNOON, 2, "Gabriela")

    __add_block(PERIOD_3, "PFE2", MORNING, 4, "Reginaldo")
    __add_block(PERIOD_3, "PFE2", AFTERNOON, 4, "Reginaldo")

    __add_block(PERIOD_3, "PBE2", MORNING, 4, "Eluã")
    __add_block(PERIOD_3, "PBE2", AFTERNOON, 4, "Eluã")

    __add_block(PERIOD_3, "RC3", MORNING, 4, "Eluã")
    __add_block(PERIOD_3, "RC3", AFTERNOON, 4, "Eluã")

    __add_block(PERIOD_3, "GSTI", MORNING, 4, "Paulo")
    __add_block(PERIOD_3, "GSTI", AFTERNOON, 4, "Paulo")

    __add_block(PERIOD_3, "SI", MORNING, 4, "Verônica")
    __add_block(PERIOD_3, "SI", AFTERNOON, 4, "Verônica")

    __add_block(PERIOD_3, "IFE2", MORNING, 2, "Gabriela")
    __add_block(PERIOD_3, "IFE2", AFTERNOON, 2, "Gabriela")

    __add_block(PERIOD_3, "EPF", MORNING, 6, "Albertina")
    __add_block(PERIOD_3, "EPF", AFTERNOON, 6, "Albertina")


#####################################################################################################
# ## AUXILIAR FUNCTIONS #############################################################################
#####################################################################################################
def load_alldata():
    _load_classes()
    _load_teachers()
    _load_curricular_component_teachers()


def get_classes_copy():
    return __classes.copy()


def get_classes():  # cuidado com efeito colateral!
    return __classes


def get_teachers_copy():
    return __teachers.copy()


def get_teachers():  # cuidado com efeito colateral!
    return __teachers


def get_blocks_copy():
    return __blocksOfCCsWithTeachers.copy()


def get_blocks():  # cuidado com efeito colateral!
    return __blocksOfCCsWithTeachers


def __add_teacher(teacher_name_arg, availabilities_arg):
    __teachers[teacher_name_arg] = Teacher(teacher_name_arg, availabilities_arg)


def __add_block(semester_number_arg, curricular_component_name_arg, shift_arg, weekly_hours_arg, teacher_name_arg):
    if weekly_hours_arg % 2 != 0:
        print("Carga horária da disciplina " + curricular_component_name_arg + " do " + str(
            semester_number_arg) + " não é par.")
        exit()
    blocks_per_week = weekly_hours_arg // 2  # divisão inteira (trunca)
    for i in range(blocks_per_week):
        __blocksOfCCsWithTeachers.append(
            __construct_block_of_two_hours(semester_number_arg, curricular_component_name_arg,
                                           shift_arg, teacher_name_arg))


def __construct_block_of_two_hours(semester_number_arg, curricular_component_name_arg, shift_arg, teacher_name_arg):
    teacher = __search_teacher(teacher_name_arg)
    return BlockOfTwoHoursAllocation(curricular_component_name_arg, semester_number_arg, shift_arg, teacher)


def __search_teacher(teacher_name_arg):
    if teacher_name_arg not in __teachers:
        print("ERRO! Professor(a) " + teacher_name_arg +
              " não cadastrado(a)!!!!!!!!!!!!!!!!!!!!!!!!!")
        input("Digite a tecla <ENTER> para encerrar.")
        exit()
    else:
        return __teachers[teacher_name_arg]
