axis = 0
q = [0,0,0,0]
for _ in range(int(input())):
    x, y = map(int,input().split())
    if x == 0 or y == 0:
        axis +=1
    elif x>0 and y>0:
        q[0] += 1
    elif x<0 and y>0:
        q[1] += 1
    elif x<0 and y<0:
        q[2] += 1
    else:
        q[3] += 1


for i in range(1,5):
    print(f"Q{i}: {q[i-1]}")
print(f"AXIS: {axis}")