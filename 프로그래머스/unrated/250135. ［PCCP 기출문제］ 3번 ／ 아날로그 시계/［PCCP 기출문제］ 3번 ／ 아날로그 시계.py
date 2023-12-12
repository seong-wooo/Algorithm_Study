def solution(h1, m1, s1, h2, m2, s2):
    start = h1 * 3600 + m1 * 60 + s1
    end = h2 * 3600 + m2 * 60 + s2
    
    cnt = 0
    
    if start == 0 or start == 43200:
        cnt += 1
    
    # 시침 : 1/120 * (t % 43200)
    # 분 : 1/10 * (t % 3600)
    # 초 : 6 * (t % 60)
    
    while start < end:
        rad_h =  1/120 * (start % 43200)
        rad_m = 1/10 * (start % 3600)
        rad_s = 6 * (start % 60)
        
        next = start + 1
        next_rad_h =  1/120 * (next % 43200)
        next_rad_m = 1/10 * (next % 3600)
        next_rad_s = 6 * (next % 60)
      
        if next_rad_h == 0:
            next_rad_h = 360
        if next_rad_m == 0:
            next_rad_m = 360
        if next_rad_s == 0:
            next_rad_s = 360
        
        if next_rad_h == next_rad_m == next_rad_s:
            cnt += 1
            start +=1
            continue
            
        
        if rad_h > rad_s and next_rad_h <= next_rad_s:
            cnt += 1
        if rad_m > rad_s and next_rad_m <= next_rad_s:
            cnt += 1
            
        start += 1
    
    
    
    return cnt