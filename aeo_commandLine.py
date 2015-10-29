#!/usr/bin/python
#------------------------------------------------------------------------------
#                                                                        IMPORT
#------------------------------------------------------------------------------
import readline
import atexit
#------------------------------------------------------------------------------
from aeo_parameters import historyLength, historyPath, isDebugging
#------------------------------------------------------------------------------
#                                                                     FUNCTIONS
#------------------------------------------------------------------------------
def setCommandLine():
    try:
        readline.read_history_file(historyPath)
    except IOError:
        pass
    readline.set_history_length(historyLength)
    atexit.register(readline.write_history_file, historyPath)
    return
#------------------------------------------------------------------------------
#                                                                           END
#------------------------------------------------------------------------------
