import time
import random
import matplotlib.pyplot as plt


# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]

# 퀵 정렬에서 사용되는 partition 함수
# pivot의 위치를 return 한다
def partition(my_list, start, end):
    i = start
    p = end
    b = start

    while i < p:
        if my_list[i] <= my_list[p]:
            swap_elements(my_list, i, b)
            b += 1
        i += 1
    swap_elements(my_list, b, p)

    return b


# 퀵 정렬
# 재귀를 이용하여 정렬한다.
def quicksort(my_list, start=0, end=None):
    if end == None:
        end = len(my_list) - 1
    if start >= end:
        return
    p = partition(my_list, start, end)
    quicksort(my_list, start, p - 1)
    quicksort(my_list, p + 1, end)


x_n = [100000,200000,300000,400000,500000,600000,700000,800000,900000,1000000]
y_time=[0,0,0,0,0,0,0,0,0,0]

for i in range(5):
    for j in range(10):
        sort_list = [random.randint(1, 1000000) for _ in range(x_n[j])]
        start = time.time()
        quicksort(sort_list)
        end = time.time()
        y_time[j] += end - start


for i in range(10):
    y_time[i] /= 5

plt.plot(x_n, y_time)
plt.title("Quick Sort")
plt.xlabel("n")
plt.ylabel("time")
plt.show()




