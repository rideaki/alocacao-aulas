import numpy

from copyreg import constructor

from model.utils.daysOfWeek import FRIDAY, MONDAY, THURSDAY, TUESDAY, WEDNESDAY
from model.utils.shifts import NUMBER_OF_BLOCKS_IN_SHIFT


class Teacher:
    
    def constructSortedBlocks(self, isMorning):
        sortedBlocks = []

        #Se professor tem disponibilidade a segunda-feira, então percorre disponibilidade em ordem crescente
        # caso contrário em ordem decrescente
        ascendingSort = MONDAY in self.__availabilities
        sortedAvailabilitiesDays = sorted(self.getAvailabilitiesCopy(), reverse=not(ascendingSort))

        daysOfWeekToBeIncluded = sorted([MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY], reverse=not(ascendingSort)) 

        #Dias disponibilizados pelo professor   
        for availableDayOfWeek in sortedAvailabilitiesDays:
            daysOfWeekToBeIncluded.remove(availableDayOfWeek)
            self.includeBlocks(isMorning, sortedBlocks, availableDayOfWeek)

        #Dias NÃO disponibilizados pelo professor -> ficará no final da lista de blocos disponíveis 
        #Necessário, caso a alocação não seja possível
        while(len(daysOfWeekToBeIncluded) > 0):
            dayOfWeekToBeIncluded = daysOfWeekToBeIncluded.pop(0)
            self.includeBlocks(isMorning, sortedBlocks, dayOfWeekToBeIncluded)
        return sortedBlocks

    def includeBlocks(self, isMorning, sortedBlocks, dayOfWeek):
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
        self.__morningSortedBlocks = self.constructSortedBlocks(True)
        self.__afternoonSortedBlocks = self.constructSortedBlocks(False)
        self.__nightSortedBlocks = self.__afternoonSortedBlocks.copy()
        print(self.name)
        print(self.__availabilities)
        print(self.__morningSortedBlocks)
        print(self.__afternoonSortedBlocks)
        print(self.__nightSortedBlocks)

    def getAvailabilitiesCopy(self):
        return numpy.array(self.__availabilities).copy()

    def getMorningSortedBlocksCopy(self):
        return numpy.array(self.__morningSortedBlocks).copy()
    
    def getAfternoonSortedBlocksCopy(self):
        return numpy.array(self.__afternoonSortedBlocks).copy()

    def getNightSortedBlocksCopy(self):
        return numpy.array(self.__nightSortedBlocks).copy()