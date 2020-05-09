import glob 

progs = glob.glob('**/*.py', recursive=True)
print ("hello" + progs)