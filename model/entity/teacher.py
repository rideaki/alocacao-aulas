import numpy

from copyreg import constructor

from model.utils.daysOfWeek import FRIDAY, MONDAY, THURSDAY, TUESDAY, WEDNESDAY
from model.utils.shifts import AFTERNOON, MORNING, NIGHT, NUMBER_OF_BLOCKS_IN_SHIFT


class Teacher:
    
    def __constructAllSortedBlocks(self):
        allSortedBlocks = {}
        shifts = [MORNING, AFTERNOON, NIGHT]
        for shift in shifts:
            allSortedBlocks[shift] = self.__constructSortedBlocksByShift(shift == MORNING)
        return allSortedBlocks

    def __constructSortedBlocksByShift(self, isMorning):
        sortedBlocksByShift = []

        #Se professor tem disponibilidade a segunda-feira, então percorre disponibilidade em ordem crescente
        # caso contrário em ordem decrescente
        ascendingSort = MONDAY in self.__availabilities
        sortedAvailabilitiesDays = sorted(self.getAvailabilitiesCopy(), reverse=not(ascendingSort))

        daysOfWeekToBeIncluded = sorted([MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY], reverse=not(ascendingSort)) 

        #Dias disponibilizados pelo professor   
        for availableDayOfWeek in sortedAvailabilitiesDays:
            daysOfWeekToBeIncluded.remove(availableDayOfWeek)
            self.__includeBlocks(isMorning, sortedBlocksByShift, availableDayOfWeek)

        #Dias NÃO disponibilizados pelo professor -> ficará no final da lista de blocos disponíveis 
        #Necessário, caso a alocação não seja possível
        while(len(daysOfWeekToBeIncluded) > 0):
            dayOfWeekToBeIncluded = daysOfWeekToBeIncluded.pop(0)
            self.__includeBlocks(isMorning, sortedBlocksByShift, dayOfWeekToBeIncluded)
        return sortedBlocksByShift

    def __includeBlocks(self, isMorning, sortedBlocks, dayOfWeek):
        if isMorning: 
            for i in range(NUMBER_OF_BLOCKS_IN_SHIFT-1, -1, -1):   #2, 1, 0
                sortedBlocks.append([i, dayOfWeek])
        else: 
            for i in range(NUMBER_OF_BLOCKS_IN_SHIFT):   #0, 1, 2
                sortedBlocks.append([i, dayOfWeek])

    #Constructor
    def __init__(self, nameArg, availabilitiesArg):
        self.name = nameArg
        self.__availabilities = availabilitiesArg
        self.__sortedBlocks = self.__constructAllSortedBlocks()
        print(self.name)
        print(self.__availabilities)
        print(self.__sortedBlocks)

    def getAvailabilitiesCopy(self):
        return numpy.array(self.__availabilities).copy()

    def getAllSortedBlocksCopy(self):
        return self.__sortedBlocks.copy()    #cópia do dicionário para evitar efeito colateral
    