import random

import dataLoader
from model.business import filter
from model.business.tableFactory import construct_class_table

globalSolution = {}  # dicionario: dicionario[dataClass] = tabela horária de cada turma (dataClass)
globalSolutionPenalty = float('inf')  # penalidades positivas. Objetivo: MINIMIZAR penalty


def heusristic_construct():
    time_tables = {}
    filtered_blocks_indexes_by_class = {}
    # Para cada turma
    for dataClass in dataLoader.get_classes_copy():
        time_tables[dataClass] = construct_class_table()
        filtered_blocks_indexes_by_class[dataClass] = filter.filter_blocks_indexes_by_semester_and_shift(
            dataLoader.get_blocks(), dataClass.semesterNumber, dataClass.shift)

        # Para cada professor
        teachers = dataLoader.get_teachers_copy()
        while len(teachers) > 0:
            teacher = teachers.pop(random.choice(list(teachers)))
            teacher_blocks_to_be_allocated = filter.filter_blocks_indexes_by_teacher(
                filtered_blocks_indexes_by_class[dataClass], teacher.name)
            while len(teacher_blocks_to_be_allocated) > 0:
                print(teacher.name)
                print(teacher_blocks_to_be_allocated)
                available_teacher_blocks_by_shift = teacher.get_all_sorted_blocks_copy()[dataClass.shift]
                print(available_teacher_blocks_by_shift)
                for teacherAvailableBlock in available_teacher_blocks_by_shift:
                    print(teacherAvailableBlock)
                    print(filtered_blocks_indexes_by_class[dataClass])
                    print(time_tables[dataClass])
                    if time_tables[dataClass][teacherAvailableBlock[0]][teacherAvailableBlock[1]] is None:
                        # alocar aula
                        time_tables[dataClass][teacherAvailableBlock[0]][
                            teacherAvailableBlock[1]] = teacher_blocks_to_be_allocated.pop(0)
                        available_teacher_blocks_by_shift.remove(teacherAvailableBlock)
                        break  # sai do laco -> teacherAvailableBlock in available_teacher_blocks_by_shift:


if __name__ == "__main__":
    dataLoader.load_alldata()
    heusristic_construct()
