import dataLoader
from model.utils.shifts import *


def filter_blocks_indexes_by_semester_and_shift(blocks_arg, semester_number_arg=1, shift_arg=MORNING):
    filtered_indexes = []
    blocks_copy = blocks_arg.copy()
    for i in range(len(blocks_copy)):
        if blocks_copy[i].semesterNumber == semester_number_arg and blocks_copy[i].shift == shift_arg:
            filtered_indexes.append(i)
    return filtered_indexes


def filter_blocks_indexes_by_teacher(blocks_indexes_arg, teacher_name_arg):
    filtered_indexes = []
    for blockIndex in blocks_indexes_arg:
        if dataLoader.get_blocks_copy()[blockIndex].teacher.name == teacher_name_arg:
            filtered_indexes.append(blockIndex)
    return filtered_indexes
