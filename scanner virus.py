# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 22:25:09 2021

@author: gaurav
"""

import glob, re
#scan for signatures just like semantec or other ant virus
def checkForSignatures () :
    print ("*### Checking for virus signatures *##")
# get all programs in the directory
    programs = glob.glob("* .py")
    for P in programs:
        thisFileInfected = False
        file = open (p,"r")
        lines=file. readlines ()
        file.close ()
        
        for line in lines:
            if (re.search ("^# Start virus code", line)):
# found the virus
            print ("!!!! virus found in file"+p)
            thisFileInfected=True
        if (thisFileInfected == False) :
            print (p +" appears to be clean")
    print ("#### end section ####")
checkForSignatures()