from model.utils.periods import MORNING_PERIOD

#Classe relativa aos dados de cada turma
class ClassData:

    # Constructor
    def __init__(
        self,
        semesterNumberArg,
        periodArg,
        timeTableArg=[[None, None, None, None, None],
                      [None, None, None, None, None],
                      [None, None, None, None, None]],
    ):
        self.semesterNumber = semesterNumberArg
        self.period = periodArg
        self.timeTable = timeTableArg
