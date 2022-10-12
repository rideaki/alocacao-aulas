
from copyreg import constructor


class Teacher:

    #Constructor
    def __init__(self, nameArg, availabilitiesArg):
        self.name = nameArg
        self.availabilities = availabilitiesArg