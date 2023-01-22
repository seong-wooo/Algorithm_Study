import sys


def div(x, y):
    if x < 0:
        return - (abs(x) // y)
    return x // y


results = []
n = int(sys.stdin.readline())


def dfs(a, plus, minus, multiple, divide, cur_value, i):
    if plus < 0 or minus < 0 or multiple < 0 or divide < 0:
        return

    if i > n - 1:
        results.append(cur_value)
        return


    dfs(a, plus - 1, minus, multiple, divide, cur_value + a[i], i + 1)
    dfs(a, plus, minus - 1, multiple, divide, cur_value - a[i], i + 1)
    dfs(a, plus, minus, multiple - 1, divide, cur_value * a[i], i + 1)
    dfs(a, plus, minus, multiple, divide - 1, div(cur_value, a[i]), i + 1)


a_ = list(map(int, sys.stdin.readline().split()))
op_ = list(map(int, sys.stdin.readline().split()))

dfs(a_, op_[0], op_[1], op_[2], op_[3], a_[0], 1)

maximum = results[0]
minimum = results[0]
for result in results:
    if result > maximum:
        maximum = result
    elif result < minimum:
        minimum = result

print(maximum)
print(minimum)