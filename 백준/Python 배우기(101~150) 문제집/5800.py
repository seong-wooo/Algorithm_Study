for i in range(int(input())):
    scores = sorted(list(map(int, input().split()))[1:])

    max_gap = max(scores[x + 1] - scores[x] for x in range(len(scores) - 1))

    print(f"Class {i + 1}")
    print(f"Max {max(scores)}, Min {min(scores)}, Largest gap {max_gap}")
