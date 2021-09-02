# 1개를 옮기기 위해서 n-1개를 옮겨야 한다는 아이디어로 구현하였다.
# 실행 시간이 오래걸리는 코드이다.


def hanoi_top(move_list,n, start,end,flag):
    if n == 1:
        move_list.append((start,end))

    else:
        hanoi_top(move_list, n-1, start,flag, end)
        hanoi_top(move_list,1,start,end,flag)
        hanoi_top(move_list,n-1,flag,end,start)

n = int(input())

move_list = []

hanoi_top(move_list, n, 1, 3, 2)

print(len(move_list))
for i in move_list:
    print(" ".join(map(str,i)))


# 코드 수정
# 하노이 탑의 이동 횟수는 2**n - 1 임을 알게되었다.
# 따라서 다음과 같이 수정할 수 있다.
# start + end + flag = 6임을 이용하여 인자 하나를 없앨수도 있다.

# def hanoi_top(n, start,end,flag):
#     if n == 1:
#         print(start,end)
#
#     else:
#         hanoi_top(n-1, start,flag, end)
#         hanoi_top(1,start,end,flag)
#         hanoi_top(n-1,flag,end,start)
#
# n = int(input())
# print(2**n -1)
# hanoi_top(n, 1, 3, 2)
