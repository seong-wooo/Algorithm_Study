import re

def solution(files):
    files = [re.split(r"(\d+)",file) for file in files]
    
    files.sort(key = lambda x : (x[0].lower(), int(x[1])))
    
    return [file[0] + str(file[1]) + "".join(file[2:]) for file in files]
        
        