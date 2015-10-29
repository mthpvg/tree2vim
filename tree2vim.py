#!/usr/bin/python

#   aeo_parameters
#   tree2vim
#       aeo_inputOutput
#           aeo_parameters
#       aeo_commandLine
#           aeo_parameters
#       aeo_userInterface
#           aeo_parameters
#           aeo_inputOutput
#       aeo_parameters

#------------------------------------------------------------------------------
#                                                                        IMPORT
#------------------------------------------------------------------------------
import os
import tarfile
from itertools import chain
#------------------------------------------------------------------------------------------------------------------------
from aeo_inputOutput import setTheEnvironment
from aeo_inputOutput import humanRead
from aeo_commandLine import setCommandLine
from aeo_userInterface import prompt
from aeo_userInterface import repeat
from aeo_parameters import *
#------------------------------------------------------------------------------
#                                                                    PARAMETERS
#------------------------------------------------------------------------------
answer = 0
minDepthOfRoots = 0
showHidden = False
compact = False
#------------------------------------------------------------------------------
#                                                                     FUNCTIONS
#------------------------------------------------------------------------------
def minDepth(roots):
    m = len(roots[0][0].split("/"))
    for e in roots:
        do = len(e[0].split("/"))
        if (do < m):
            m = do
            print m
    return m

def fillList(mList,mIp):
    #It appends elements of an input to a list, it also strip the trailing whitespaces
    for e in mIp.readlines():
        mList.append(e.rstrip())
    return
#------------------------------------------------------------------------------
#                                                                       CLASSES
#------------------------------------------------------------------------------
class File:
    def __init__(self, path, alias, status, fileType):
        self.path =  path
        self.depth = len(path.split("/")) - minDepthOfRoots
        self.alias = alias
        self.hiddenFile = not self.alias.find(".") != 0
        self.status = status
        self.fileType = fileType
        self.parentPath = os.path.dirname(path)
        self.parentName = os.path.basename(self.parentPath)
        if (fileType == "directory"):
            self.isDirectory = True
            self.getChildrenAndContent()
        else:
            self.isDirectory = False
        self.color = color[self.fileType]
        return

    def refresh(self):
#        del self.children       [:]
#        del self.content        [:]
        toCreate                =       []
        childrenCopy            =       self.children[:]
        contentCopy             =       self.content[:]
        self.getChildrenAndContent()
        for i, val in enumerate(self.children):
            if (childrenCopy[i] != val):
                childrenCopy.insert(i, val)
                toCreate.append(i)
        return toCreate

    def getChildrenAndContent(self):
        osWalk = os.walk(self.path).next()
        self.children = osWalk[1]
        self.content = osWalk[2]
        self.nbChildren =       len(self.children)
        self.nbContent = len(self.content)
        self.children.sort()
        self.content.sort()
        for i in range(self.nbChildren):
            self.children[i] = self.path + "/" + self.children[i]
        for i in range(self.nbContent):
            self.content[i] = self.path + "/" + self.content[i]
        return
#------------------------------------------------------------------------------
class FileBox:
    def __init__(self, roots):
        global minDepthOfRoots
        minDepthOfRoots = minDepth(roots)
        self.files = []
        self.nbFiles = 0
        self.currentDirectory = 0
        self.currentPath = roots[0][0]
        for i in range(len(roots)):
            self.addAFile(i, roots[i][0], roots[i][1], roots[i][2])
        return

    def addAFile(self, n, path, alias, status = "close"):
        self.files.insert(n, File(path, alias, status, self.fileType(path)))
        self.nbFiles += 1
        return

    def removeAFile(self, n):
        self.files.pop(n)
        self.nbFiles -= 1
        return

    def fileType(self, path):
        if (os.path.isdir(path)):
            return "directory"
        else:
            return "file"

    def display(self, n):
        for i in range(self.nbFiles):
            if (not self.files[i].hiddenFile or (self.files[i].hiddenFile and showHidden)):
                relatedToCurrentDirectory = (self.files[n].path.find(self.files[i].path) != -1 or self.files[i].path.find(self.files[n].path) != -1)
                if (relatedToCurrentDirectory or (not compact)):
                    tempString = str(i)
                    number = color['yellow'] + repeat( 4 - len(tempString), " ") + tempString
                    print repeat(self.files[i].depth, "    ") + number + " " + self.files[i].color + self.files[i].alias + color['void']
        return

    def goto(self, n):
        self.currentDirectory = n
        self.currentPath = self.files[n].path
        if (self.files[n].status == "close"):
            self.files[n].status = "open"
            insertionPosition = n + 1
            for e in chain(self.files[n].children, self.files[n].content):
                self.addAFile(insertionPosition, e, os.path.basename(e))
                insertionPosition += 1
        else :
            self.files[n].status = "close"
            for e in self.findChildrenAndContent(n):
                self.removeAFile(e)
        return

    def findChildrenAndContent(self, n):
        toDelete = []
        for i, val in enumerate(self.files):
            if (val.path.find(self.files[n].path + "/") != -1):
                toDelete.append(i)
        toDelete.sort(reverse = True)
        return toDelete

    def fileNumberByPath(self, path):
        for i, val in enumerate(self.files):
            if (val.path == path):
                return i
        return -1

    def refresh(self):
        toDelete = []
        for i, val in enumerate(self.files):
            if (not os.path.exists(val.path)):
                toDelete.append(i)
        toDelete.sort(reverse = True)
        for e in toDelete:
            self.removeAFile(e)
        for i, val in enumerate(self.files):
            if (val.isDirectory and val.status == "open"):
                print "refresh=", val.refresh()
        return

    def fileIsATar(self, path):
        #BUILDING LIST OF THE FILES INSIDE THE TAR
        tarList = []
        tarAnswer=""
        os.system("clear")
        cmd = "tar -tvf " + path + " | sed 's/.* //'"
        cmdRslt = os.popen(cmd)
        fillList(tarList,cmdRslt)
        #DISPLAYING THE FILES INSIDE THE TAR
        print color['green'] + path + color['void'], "contains :"
        for i in range(len(tarList)):
            print color['yellow'] + str(i) + color['void'], tarList[i]
        #PROMPT USER LOOP
        while (tarAnswer != "e"):
            tarAnswer = raw_input("Go to (e to exit) : ")
            if (tarAnswer.isdigit() and int(tarAnswer) < len(tarList) and int(tarAnswer)>-1):
                #USER INPUT IS MATCHING WITH A FILE
		tarAnswer2 = raw_input("[e]xtract [o]pen : ")
                os.chdir(os.path.dirname(path))
                os.system("tar -xvf " + path + " " + tarList[int(tarAnswer)])
		if (tarAnswer2=="o"):
                	os.system("vim " + tarList[int(tarAnswer)])
                	os.system("rm -rf " + tarList[int(tarAnswer)])
            elif (tarAnswer2 == "e"):
                #USER WANTS TO EXIT
                break
        return

    def goToAFile(self, n):
        path = self.files[n].path
        if (tarfile.is_tarfile(path)):
            self.fileIsATar(path)
        else:
            os.system("vim " + path)
        return
#------------------------------------------------------------------------------
#                                                                       PROGRAM
#------------------------------------------------------------------------------
oldAnswer = 0

setTheEnvironment()
fileBox =  FileBox(humanRead(rootsPath, " "))
setCommandLine()
while (answer != "e"):
    os.system("clear")
    fileBox.display(oldAnswer)
    answer = prompt()
    if (answer=="b"):
        answer = str(oldAnswer)
    
    if (answer == "e"):
        break
    elif (answer == "h"):
        showHidden = not showHidden
    elif (answer == "c"):
        compact = not compact
    elif (answer.isdigit()):
        if (int(answer) < fileBox.nbFiles and int(answer) >= 0):
            if (fileBox.files[int(answer)].isDirectory):
                if (not fileBox.files[int(answer)].hiddenFile or (fileBox.files[int(answer)].hiddenFile and showHidden)):
                    fileBox.goto(int(answer))
                    oldAnswer = int(answer)
            else:
                fileBox.goToAFile(int(answer))
            fileBox.refresh()
        #fileBox.goto(fileBox.fileNumberByPath(os.getcwd()))
        #fileBox.goto(fileBox.fileNumberByPath(os.getcwd()))
print os.getcwd()
#------------------------------------------------------------------------------
#                                                                           END
#------------------------------------------------------------------------------
