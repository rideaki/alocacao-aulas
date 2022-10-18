class BlockOfTwoHoursAllocation():

    # Constructor
    def __init__(self, curricular_component_name_arg, semester_number_arg, shift_arg, teacher_arg):
        self.curricularComponentName = curricular_component_name_arg
        self.semesterNumber = semester_number_arg
        self.shift = shift_arg       # turno: MORNING, AFTERNOON ou NIGHT
        self.teacher = teacher_arg

    
        