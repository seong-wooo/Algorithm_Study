def solution(numbers, hand):
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ["*", 0, "#"]]

    left_i, left_j = 0, 3
    right_i, right_j = 2, 3

    result = ""
    for i in numbers:
        if i in (1, 4, 7):
            result += "L"
            left_i, left_j = (i - 1) % 3, (i - 1) // 3
        elif i in (3, 6, 9):
            result += "R"
            right_i, right_j = (i - 1) % 3, (i - 1) // 3
        else:
            for j in range(3):
                for k in range(4):
                    if keypad[k][j] == i:
                        if abs(left_j - k) + abs(left_i - j) < abs(right_j - k) + abs(right_i - j):
                            result += "L"
                            left_i, left_j = j, k
                        elif abs(left_j - k) + abs(left_i - j) > abs(right_j - k) + abs(right_i - j):
                            result += "R"
                            right_i, right_j = j, k
                        else:
                            if hand == "right":
                                result += "R"
                                right_i, right_j = j, k
                            else:
                                result += "L"
                                left_i, left_j = j, k
    return result