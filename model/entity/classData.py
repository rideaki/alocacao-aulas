from model.utils.shifts import MORNING

#Classe relativa aos dados de cada turma
class ClassData:

    # Constructor
    def __init__(
        self,
        semesterNumberArg,
        shiftArg,  #turno: MORNING, AFTERNOON ou NIGHT
        timeTableArg=[[None, None, None, None, None],
                      [None, None, None, None, None],
                      [None, None, None, None, None]],
    ):
        self.semesterNumber = semesterNumberArg
        self.shift = shiftArg    #turno: MORNING, AFTERNOON ou NIGHT
        self.timeTable = timeTableArg
