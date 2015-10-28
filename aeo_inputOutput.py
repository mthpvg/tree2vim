#!/usr/bin/python

#========================================================================================================================
#=                                                                                                                      =
#=                                                                                                                      =
#=                                                                                                                      =
#=                                                                                                                      =
#=                                                                                                                      =
#=                                                                                                                      =
#========================================================================================================================
#=                                                                                                                      =
#=                                                        IMPORT                                                        =
#=                                                                                                                      =
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import cPickle
import os
import sys
import inspect
#------------------------------------------------------------------------------------------------------------------------
from aeo_parameters             import *
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#========================================================================================================================
#=                                                                                                                      =
#=                                                                                                                      =
#=                                                                                                                      =
#=                                                                                                                      =
#=                                                                                                                      =
#=                                                                                                                      =
#========================================================================================================================
#=                                                                                                                      =
#=                                                       FUNCTION                                                       =
#=                                                                                                                      =
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def existence(pathName):
    if (isDebugging): DEBUG(__file__, "pathName=" + pathName)
    if (not os.path.exists(pathName)):
        print "ERROR in a reading functions from the file mp_IO.py : " + pathName + " does not exist."
        sys.exit()
    return
#------------------------------------------------------------------------------------------------------------------------
def humanRead(pathName, separator = "NONE", option = "r"):
    existence(pathName)
    with open(pathName, option) as tempFile:
        if (separator != "NONE"):
        #matrix
            tensor = [row.strip().split(separator) for row in tempFile]
        else:
        #array
            tensor = [row.strip() for row in tempFile]
    return tensor
#------------------------------------------------------------------------------------------------------------------------
def humanWrite(pathName, data, option = "w"):
    with open(pathName, option) as tempFile:
        if (isinstance(data, list)):
        #data is a list
            for e in data:
                if (isinstance(e, list)):
                #e is a list of list
                    tempFile.write("%s\n" % " ".join(e))
                else:
                #e is considered as a string
                    tempFile.write("%s\n" % e)
        elif (isinstance(data, str)):
        #data is a string
            tempFile.write(data)
    return
#------------------------------------------------------------------------------------------------------------------------
def read(pathName, option = "rb"):
    existence(pathName)
    with open(pathName, option) as tempFile:
        data = cPickle.load(tempFile)
    return data
#------------------------------------------------------------------------------------------------------------------------
def write(pathName, data, option = "wb"):
    with open(pathName, option) as tempFile:
        cPickle.dump(data, tempFile)
    return
#------------------------------------------------------------------------------------------------------------------------
def setTheEnvironment():
    if (isDebugging): DEBUG(__file__, "homePath=" + homePath)
    os.chdir(homePath)
    if (not os.path.exists(mthpvgPath)):
        os.makedirs(mthpvgDir)
    os.chdir(mthpvgPath)
    if (not os.path.exists(configPath)):
        os.makedirs(configDir)
    os.chdir(configPath)
    if (os.path.exists(debugPath)):
        os.remove(debugPath)
    if (not os.path.exists(rootsPath)):
        os.system("clear")
        print "This script needs the paths of the places you want to browse."
        print "By default your $HOME has been added, if you want to add a path just add a new"
        print "line to this file : ", rootsPath
        humanWrite(rootsPath, homePath + " HOME" + " close")
        raw_input("Type any key to continue : ")
        os.system("clear")
    return
#------------------------------------------------------------------------------------------------------------------------
def DEBUG(name, strng, strngOpt = ""):
    humanWrite(debugPath, os.path.basename(name) + " >> " + str(inspect.stack()[1][3]) + " >> " + strng + "\n", "a")
    if (strngOpt != ""):
        humanWrite(debugPath, "        " + strngOpt + "\n", "a")
    return
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#========================================================================================================================
#=                                                                                                                      =
#=                                                                                                                      =
#=                                                                                                                      =
#=                                                                                                                      =
#=                                                                                                                      =
#=                                                                                                                      =
#========================================================================================================================
