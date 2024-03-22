import re

def solution(files):
    return sorted(files, key = sort)


def sort(file):
    head, number, *tail = re.split(r"(\d+)", file)
    return head.lower(), int(number)
