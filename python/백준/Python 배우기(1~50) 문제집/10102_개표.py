v, s  = int(input()), input()
a = s.count("A")
if a > v-a:
    print("A")
elif a < v-a:
    print("B")
else:
    print("Tie")
