array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
    a = array[i]
    for j in range(i, -1, -1):
        if a < array[j-1]:
            array[j] = array[j-1]
        else:
            break
    array[j] = a
print(array)