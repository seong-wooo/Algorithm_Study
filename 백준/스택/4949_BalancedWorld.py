# 괄호안에 아무것도 없는 상태에서 닫힐 때
# 괄호안에 다른 괄호가 있는 상태에서 닫힐 때
# 두 경우를 나누는 부분에서 어려움을 겪었다.
# 처음에는 9012와 같이 숫자로 접근했지만 위의 두 경우의 조건때문에 구현 실패했다.
# 스택의 기본 성질을 생각하며 풀면 쉬웠던 문제이다.

while True:
    sentense = input()
    if sentense ==".":
        break

    stack =[]
    for s in sentense:
        if s != "(" and s != ")" and s != "[" and s != "]":
            continue

        if s == "(" or s=="[":
            stack.append(s)
        elif s == ")":
            if len(stack) == 0 or stack[-1] !="(":
                stack.append(s)
                break
            elif stack[-1] == "[":
                break
            elif stack[-1] == "(":
                stack.pop()

        else:
            if len(stack) == 0 or stack[-1] !="[":
                stack.append(s)
                break
            elif stack[-1] == "(":
                break
            elif stack[-1] == "[":
                stack.pop()

    if len(stack) != 0:
        print("no")
    else:
        print("yes")

