from model.business.tableFactory import constructClassTable

#Classe relativa aos dados de cada turma
class ClassData:

    # Constructor
    def __init__(
        self,
        courseNameArg,
        semesterNumberArg,
        shiftArg,  #turno: MORNING, AFTERNOON ou NIGHT
        timeTableArg = constructClassTable(),
    ):
        self.courseName = courseNameArg    
        self.semesterNumber = semesterNumberArg
        self.shift = shiftArg    #turno: MORNING, AFTERNOON ou NIGHT
        self.timeTable = timeTableArg

    
