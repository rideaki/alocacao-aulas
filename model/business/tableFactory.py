from numpy import *

def constructClassTable():                      
    return array(                               # BlockOf2Hours  MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY
           [[None, None, None, None, None],     #      0
            [None, None, None, None, None],     #      1
            [None, None, None, None, None]]     #      2
    )    
                                                       
def constructTeacherTable():                          #                MORNING     |    AFTERNOON 
    return array(                                     #              0    1     2  |  3     4     5
           [[None, None, None, None, None, None],     #   MONDAY                   
            [None, None, None, None, None, None],     #   TUESDAY
            [None, None, None, None, None, None],     #   WEDNESDAY
            [None, None, None, None, None, None],     #   THURSDAY
            [None, None, None, None, None, None]]     #   FRIDAY
    )