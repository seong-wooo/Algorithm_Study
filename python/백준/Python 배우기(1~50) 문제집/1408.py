start = list(map(int, input().split(":")))
end = list(map(int, input().split(":")))

result = []
if(end[2] >= start[2]):
    result.append(end[2]-start[2])
else:
    end[1] -= 1
    result.append(end[2] + 60 - start[2])

if (end[1] >= start[1]):
    result.append(end[1] - start[1])
else:
    end[0] -= 1
    result.append(end[1] + 60 - start[1])


if (end[0] >= start[0]):
    result.append(end[0] - start[0])
else:
    result.append(end[0] + 24 -start[0])

print(f"{str(result[2]).zfill(2)}:{str(result[1]).zfill(2)}:{str(result[0]).zfill(2)}")