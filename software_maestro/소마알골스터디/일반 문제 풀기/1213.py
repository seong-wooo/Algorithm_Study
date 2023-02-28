from collections import Counter

s = input()
counter = Counter(s)

if sum(1 for i in counter.values() if i % 2 == 1) > 1:
    print("I'm Sorry Hansoo")

else:
    result = [""] * len(s)

    i = 0
    for alph in sorted(counter.keys()):
        if counter[alph] % 2 == 1:
            result[len(s) // 2] = alph
        counter[alph] //= 2
        result[i:i + counter[alph]] = [alph] * counter[alph]
        result[len(s) - 1 - i:len(s) - 1 - i - counter[alph]:-1] = [alph] * counter[alph]
        i += counter[alph]


    print("".join(result))