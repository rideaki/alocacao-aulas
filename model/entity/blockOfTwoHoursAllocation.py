class BlockOfTwoHoursAllocation():

    #Constructor
    def __init__(self, classDataArg, curricularComponentNameArg, teacherArg):
        self.classData = classDataArg
        self.curricularComponentName = curricularComponentNameArg
        self.teacher = teacherArg

    def __str__ (self):
        return str(self.curricularComponentName) + " / " + self.teacher.name
    
        