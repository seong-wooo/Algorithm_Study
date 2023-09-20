def solution(new_id):
    valid = set([chr(i) for i in range(97, 123)] + ["_", ".", "-"] + [str(i) for i in range(0, 10)])
    # 1
    new_id = new_id.lower()

    # 2
    new_id = "".join([i for i in new_id if i in valid])
    # 3

    while True:
        if ".." in new_id:
            new_id = new_id.replace("..", ".")
        else:
            break

    # 4
    while new_id:
        if new_id[0] == ".":
            if len(new_id) > 1:
                new_id = new_id[1:]
            else:
                new_id = "a"
        if new_id[-1] == ".":
            if len(new_id) > 1:
                new_id = new_id[:-1]
            else:
                new_id = "a"

        if new_id[0] != "." and new_id[-1] != ".":
            break

    # 6
    if len(new_id) >= 16:
        new_id = new_id[:15]

    while new_id:
        if new_id[-1] == ".":
            if len(new_id) > 1:
                new_id = new_id[:-1]
            else:
                new_id = ""
        else:
            break

    # 7
    while len(new_id) < 3:
        new_id += new_id[-1]

    return new_id