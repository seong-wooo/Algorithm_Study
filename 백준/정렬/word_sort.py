# 처음에는 중복을 없애지 않고 정렬을 실행하였는데 실행 시간이 굉장히 길었다.
# set() 을 이용하여 중복을 없앤 뒤 정렬을 실행했다


import  sys

n = int(sys.stdin.readline())

word_list =[]

for i in range(n):
    word_list.append(sys.stdin.readline().strip())

word_list = list(set(word_list))
word_list.sort(key=lambda x:(len(x), x))


for j in word_list:
    print(j)