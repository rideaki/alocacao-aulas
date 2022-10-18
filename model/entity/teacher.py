import numpy

from model.utils.daysOfWeek import FRIDAY, MONDAY, THURSDAY, TUESDAY, WEDNESDAY
from model.utils.shifts import AFTERNOON, MORNING, NIGHT, NUMBER_OF_BLOCKS_IN_SHIFT


class Teacher:

    def __construct_all_sorted_blocks(self):
        all_sorted_blocks = {}
        shifts = [MORNING, AFTERNOON, NIGHT]
        for shift in shifts:
            all_sorted_blocks[shift] = self.__construct_sorted_blocks_by_shift(shift == MORNING)
        return all_sorted_blocks

    def __construct_sorted_blocks_by_shift(self, is_morning):
        sorted_blocks_by_shift = []

        # Se professor tem disponibilidade a segunda-feira, então percorre disponibilidade em ordem crescente
        # caso contrário em ordem decrescente
        ascending_sort = MONDAY in self.__availabilities
        sorted_availabilities_days = sorted(self.get_availabilities_copy(), reverse=not ascending_sort)

        days_of_week_to_be_included = sorted([MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY], reverse=not ascending_sort)

        # Dias disponibilizados pelo professor
        for availableDayOfWeek in sorted_availabilities_days:
            days_of_week_to_be_included.remove(availableDayOfWeek)
            self.__include_blocks(is_morning, sorted_blocks_by_shift, availableDayOfWeek)

        # Dias NÃO disponibilizados pelo professor -> ficará no final da lista de blocos disponíveis
        # Necessário, caso a alocação não seja possível
        while len(days_of_week_to_be_included) > 0:
            day_of_week_to_be_included = days_of_week_to_be_included.pop(0)
            self.__include_blocks(is_morning, sorted_blocks_by_shift, day_of_week_to_be_included)
        return sorted_blocks_by_shift

    @staticmethod
    def __include_blocks(is_morning, sorted_blocks, day_of_week):
        if is_morning:
            for i in range(NUMBER_OF_BLOCKS_IN_SHIFT - 1, -1, -1):  # 2, 1, 0
                sorted_blocks.append([i, day_of_week])
        else:
            for i in range(NUMBER_OF_BLOCKS_IN_SHIFT):  # 0, 1, 2
                sorted_blocks.append([i, day_of_week])

    # Constructor
    def __init__(self, name_arg, availabilities_arg):
        self.name = name_arg
        self.__availabilities = availabilities_arg
        self.__sortedBlocks = self.__construct_all_sorted_blocks()
        print(self.name)
        print(self.__availabilities)
        print(self.__sortedBlocks)

    def get_availabilities_copy(self):
        return numpy.array(self.__availabilities).copy()

    def get_all_sorted_blocks_copy(self):
        return self.__sortedBlocks.copy()  # cópia do dicionário para evitar efeito colateral
