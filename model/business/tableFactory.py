import numpy 

########################################################################
# BlockOf2Hours  MONDAY=0, TUESDAY=1, WEDNESDAY=2, THURSDAY=3, FRIDAY=4
########################################################################
#      0
#      1
#      2
########################################################################
def constructClassTable(initialValue = None):                      
    return [[initialValue, initialValue, initialValue, initialValue, initialValue],     
            [initialValue, initialValue, initialValue, initialValue, initialValue],     
            [initialValue, initialValue, initialValue, initialValue, initialValue]]     
