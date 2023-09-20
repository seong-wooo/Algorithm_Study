cute = 0
for i in range(int(input())):
    if input() == "1":
        cute+=1
    else:
        cute-=1

print("Junhee is cute!" if cute > 0 else "Junhee is not cute!")