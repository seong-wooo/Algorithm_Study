def solution(sizes):
    w, h = max(sizes[0]), min(sizes[0])

    for wh in sizes:
        w, h = max(w, max(wh)), max(h, min(wh))

    return w * h


print([][-1:])