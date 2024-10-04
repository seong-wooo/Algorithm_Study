import re

def solution(files):

    files.sort(key = change)

    return files

def change(file):
    
    file = re.findall("([^\d]+)(\d+)(.*)", file)[0]

    return [file[0].lower(), int(file[1])]
    