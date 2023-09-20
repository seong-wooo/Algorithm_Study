r = 31
m = 1234567891

l = input()
al = input()

print(
    sum(
        [
            ((ord(al[i]) - 96) * (r ** i)) for i in range(len(al))
        ]
    ) % m
)
