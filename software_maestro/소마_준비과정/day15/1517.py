import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

result = 0


def merge(left, right):
    global result

    i = 0
    j = 0
    merge_list = []
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result += len(left) - i
            merge_list.append(right[j])
            j += 1


        else:
            merge_list.append(left[i])
            i += 1

    if i == len(left):
        merge_list += right[j:]

    else:
        merge_list += left[i:]

    return merge_list


def merge_sort(a):
    if len(a) == 1:
        return a


    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])

    return merge(left, right)


merge_sort(a)

print(result)