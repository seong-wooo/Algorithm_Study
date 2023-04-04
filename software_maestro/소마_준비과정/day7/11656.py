s = input()

result = [s[i:] for i in range(len(s))]

result.sort()

print("\n".join(result))