import re

import heapq
def solution(m, musicinfos):
    m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
    
    pattern = re.compile(m)
    answer = []
    
    for i in range(len(musicinfos)):
        s = musicinfos[i].split(",")
        minute = changeMinute(s[0], s[1])
        name = s[2]
        music = s[3].replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
        
        if (pattern.search(music * (minute // len(music)) + music[:minute % len(music)])):
            answer.append([minute, name])
    
    return "(None)" if not answer else max(answer, key = lambda x: x[0])[1]
        
    
        
        
        
def changeMinute(start, end):

    s_h, s_m = map(int, start.split(":"))
    e_h, e_m = map(int, end.split(":"))
    
    return (e_h - s_h) * 60 + (e_m - s_m)
    
    
    
        
        