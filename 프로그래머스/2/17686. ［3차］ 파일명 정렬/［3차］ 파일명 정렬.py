import re

def solution(files):
    return [file[0] + str(file[1]) + "".join(file[2:]) for file in sorted([re.split(r"(\d+)",file) for file in files], key = lambda x : (x[0].lower(), int(x[1])))]
        
        