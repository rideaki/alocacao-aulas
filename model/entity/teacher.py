import numpy

from copyreg import constructor

from model.utils.daysOfWeek import FRIDAY, MONDAY
from model.utils.shifts import NUMBER_OF_BLOCKS_IN_SHIFT


class Teacher:
    
    def constructAvailabilitiesBlocks(self, isMorning):
        availabilitiesBlocks = []
        sortedAvailabilitiesDays = sorted(self.getAvailabilitiesCopy(), reverse=not(MONDAY in self.__availabilities))
            
        for dayOfWeek in sortedAvailabilitiesDays:
            if isMorning: 
                for i in range(NUMBER_OF_BLOCKS_IN_SHIFT-1, -1, -1):   #2, 1, 0
                    availabilitiesBlocks.append([i, dayOfWeek])
            else: 
                for i in range(NUMBER_OF_BLOCKS_IN_SHIFT):   #0, 1, 2
                    availabilitiesBlocks.append([i, dayOfWeek])    
        return availabilitiesBlocks

    #Constructor
    def __init__(self, nameArg, availabilitiesArg):
        self.name = nameArg
        self.__availabilities = availabilitiesArg
        self.__morningAvailabilitiesBlocks = self.constructAvailabilitiesBlocks(True)
        self.__afternoonAvailabilitiesBlocks = self.constructAvailabilitiesBlocks(False)
        self.__nightAvailabilitiesBlocks = self.__afternoonAvailabilitiesBlocks.copy()
        print(self.name)
        print(self.__availabilities)
        print(self.__morningAvailabilitiesBlocks)
        print(self.__afternoonAvailabilitiesBlocks)
        print(self.__nightAvailabilitiesBlocks)

    def getAvailabilitiesCopy(self):
        return numpy.array(self.__availabilities).copy()

    def getMorningAvailabilitiesBlocksCopy(self):
        return numpy.array(self.__morningAvailabilitiesBlocks).copy()
    
    def getAfternoonAvailabilitiesBlocksCopy(self):
        return numpy.array(self.__afternoonAvailabilitiesBlocks).copy()

    def getNightAvailabilitiesBlocksCopy(self):
        return numpy.array(self.__nightAvailabilitiesBlocks).copy()