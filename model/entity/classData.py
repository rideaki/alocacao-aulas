from model.business.tableFactory import constructClassTable

#Classe relativa aos dados de cada turma
class ClassData:

    # Constructor
    def __init__(
        self,
        courseNameArg,
        periodNumberArg,
        shiftArg,  #turno: MORNING, AFTERNOON ou NIGHT
        timeTableArg = constructClassTable(),
    ):
        self.courseName = courseNameArg    
        self.periodNumber = periodNumberArg
        self.shift = shiftArg    #turno: MORNING, AFTERNOON ou NIGHT
        self.timeTable = timeTableArg

    
