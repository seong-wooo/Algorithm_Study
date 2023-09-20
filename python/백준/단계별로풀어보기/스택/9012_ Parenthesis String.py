# ")" 가 입력 되었을 때 스택을 처리하는 방법에서 헤맸다.

import sys

t = int(sys.stdin.readline())

for i in range(t):
    ps = sys.stdin.readline().strip()
    ps_list = []
    ps_true = True
    for p in ps:
        if p == "(":
            ps_list.append(p)
        else:
            if len(ps_list) == 0:
                ps_true = False
                break

            elif ps_list[-1] == "(":
                ps_list.pop()

    if len(ps_list) > 0:
        ps_true = False

    if ps_true:
        print("YES")
    else:
        print("NO")


# 스택의 성질을 이용한 다른 방법
# 스택에 삽입하는 것을 숫자로 표현한다
# 단순 숫자 계산으로 더 간단하게 실행한다.

# import sys
#
# t = int(sys.stdin.readline())
#
# for i in range(t):
#     ps = sys.stdin.readline().strip()
#     total = 0
#     for p in ps:
#         if p == "(":
#             total += 1
#         elif p == ")":
#             total -= 1
#         if total < 0:
#             # ")"가 "(" 보다 먼저 나오게 되면
#             print("NO")
#             break
#     if total == 0:
#         print("YES")
#     elif total > 0:
#         print("NO")





