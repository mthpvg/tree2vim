#!/usr/bin/python
#------------------------------------------------------------------------------
#                                                                        IMPORT
#------------------------------------------------------------------------------
from aeo_inputOutput            import DEBUG
from aeo_parameters             import *
#------------------------------------------------------------------------------
#                                                                     FUNCTIONS
#------------------------------------------------------------------------------
def repeat(nTimes, pattern):
    #It returns nTimes the pattern
    string = ""
    for i in range(nTimes):
        string += pattern
    return string
#------------------------------------------------------------------------------
def delimiter():
    print repeat(delimiterSize, delimiterPattern)
    return
#------------------------------------------------------------------------------
def prompt():
    delimiter()
    print "[e]xit [h]idden [c]ompact [b]ack"
    delimiter()
    answer = raw_input("> ")
    if (isDebugging): DEBUG(__file__, "answer=" + answer)
    return answer
#------------------------------------------------------------------------------
#                                                                           END
#------------------------------------------------------------------------------
