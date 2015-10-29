#!/usr/bin/python
#------------------------------------------------------------------------------
#                                                                        IMPORT
#------------------------------------------------------------------------------
from os import path
#------------------------------------------------------------------------------
#                                                                    PARAMETERS
#------------------------------------------------------------------------------
color = {
    'bold': '\033[30m', \
    'void': '\033[0m' , \
    'darkGray': '\033[90m', \
    'salmon': '\033[91m', \
    'lightGreen': '\033[92m', \
    'yellow': '\033[93m', \
    'violet': '\033[94m', \
    'pink': '\033[95m', \
    'lightCyan': '\033[96m', \
    'white': '\033[97m', \
    'red': '\033[31m', \
    'green': '\033[32m', \
    'brown': '\033[33m', \
    'darkBlue': '\033[34m', \
    'magenta': '\033[35m', \
    'indigo': '\033[36m', \
    'lightGrey': '\033[37m', \
    
    'file': '\033[95m', \
    'hiddenFile': '\033[35m', \
    'directory': '\033[94m', \
    'hiddenDirectory': '\033[34m', \
    
    'superGreen': '\033[1;42m' + '\033[1;37m'
}
#------------------------------------------------------------------------------
isDebugging =       False
#------------------------------------------------------------------------------
delimiterSize =       120
delimiterPattern =       "="
historyLength =       1000
#------------------------------------------------------------------------------
homePath = path.expanduser("~")
mthpvgDir = ".mthpvg2"
mthpvgPath = homePath    + "/" + mthpvgDir
configDir = "config"
configPath = mthpvgPath  + "/" + configDir
saveFile = "mFileBox.pkl"
savePath = configPath  + "/" + saveFile
rootsFile = "roots.cfg"
rootsPath = configPath  + "/" + rootsFile
debugFile = "trace.dbg"
debugPath = configPath  + "/" + debugFile
historyFile = "history.txt"
historyPath = configPath  + "/" + historyFile
#------------------------------------------------------------------------------
#                                                                           END
#------------------------------------------------------------------------------
