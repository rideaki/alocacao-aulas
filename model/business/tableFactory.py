import numpy 

########################################################################
# BlockOf2Hours  MONDAY=0, TUESDAY=1, WEDNESDAY=2, THURSDAY=3, FRIDAY=4
########################################################################
#      0
#      1
#      2
########################################################################
def constructClassTable():                      
    return [[None, None, None, None, None],     
            [None, None, None, None, None],     
            [None, None, None, None, None]]     

########################################################################
# BlockOf2Hours  MONDAY=0, TUESDAY=1, WEDNESDAY=2, THURSDAY=3, FRIDAY=4
########################################################################
#          0
#MORNING   1
#          2
#-----------------------------------------------------------------------
#          3
#AFTERNNON 4
#          5                                                      
########################################################################
def constructTeacherTable():
    #axis=0 -> contatenação vertical                          
    return numpy.concatenate((constructClassTable(), constructClassTable()), axis=0) 