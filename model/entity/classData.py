from model.business.tableFactory import constructClassTable

# Classe relativa aos dados de cada turma
class ClassData:

    # Constructor
    def __init__(
        self,
        courseNameArg,
        periodNumberArg,
        shiftArg,  # turno: MORNING, AFTERNOON ou NIGHT
        timeTableArg=constructClassTable(),
    ):
        self.courseName = courseNameArg
        self.periodNumber = periodNumberArg
        self.shift = shiftArg  # turno: MORNING, AFTERNOON ou NIGHT
        self.timeTable = timeTableArg

    def __hash__(self):
        return id(self)

    def __str__ (self):
        return str(self.periodNumber) + " " + self.shift + " - " + self.courseName

    def __lt__(self, other):
        return str(self) < str(other)

    def __eq__(self, other):
        return (
            self.courseName == other.courseName
            and self.periodNumber == other.periodNumber
            and self.shift == other.shift
        )
    
