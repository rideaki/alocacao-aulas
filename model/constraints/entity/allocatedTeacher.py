from model.entity.teacher import Teacher 

from model.utils.daysOfWeek import FRIDAY, MONDAY, THURSDAY, TUESDAY, WEDNESDAY
from model.utils.shifts import AFTERNOON, MORNING, NIGHT, NUMBER_OF_BLOCKS_IN_SHIFT
from model.business.tableFactory import constructClassTable

class AllocatedTeacher(Teacher):

    #Constructor
    def __init__(self, nameArg, availabilitiesArg):
        super().__init__(nameArg, availabilitiesArg)
        self.allocationsTables = self.__constructAllocationsTablesDictByShift()

    def __constructAllocationsTablesDictByShift(self):
        allocationsTablesDict = {}
        shifts = [MORNING, AFTERNOON, NIGHT]
        for shift in shifts:
            allocationsTablesDict[shift] = constructClassTable()
        return allocationsTablesDict