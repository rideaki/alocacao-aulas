from model.utils.periods import MORNING_PERIOD

class classData:

    # Constructor
    def __init__(
        self,
        courseNameArg,
        semesterNumberArg=1,
        periodArg=MORNING_PERIOD,
        timeTableArg = [[None, None, None, None, None], 
                        [None, None, None, None, None], 
                        [None, None, None, None, None]],
    ):
        self.courseName = courseNameArg
        self.semesterNumber = semesterNumberArg
        self.period = periodArg
        self.timeTable = timeTableArg
