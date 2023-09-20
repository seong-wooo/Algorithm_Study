# 4628ms 걸린 코드
# 에라토네스의 체를 이용하였지만 별료 효율적이진 않은 듯 하다.
# 맨 밑에 효율적인 에라토네스 체 코드를 적어 놓았다.
n = int(input())

primes = [0,0]+[i for i in range(2,n+1)]

for i in range(2,n):
    if primes[i] != 0:
        j = i + primes[i]
        while n + 1 > j:
            primes[j] = 0
            j += primes[i]

primes = [i for i in primes if i > 0]

result = 0
for i in range(len(primes)):
    test = n
    for j in range(i, len(primes)):
        test -= primes[j]
        if test == 0:
            result += 1
            break
        elif test < 0:
            break
print(result)


# 에라토네스의 체
# 이 코드를 사용하면 1080ms로 시간이 줄어든다
def primes(n):
    result = [False,False] + [True]*(n-1)
    for i in range(2, int(n**0.5+1.5)):
        if result[i]:
            # result[2*i::i] 는 값을 리턴하는게 아니라 가리키는 것 .. ?
            # result[2*i::i]와 같은 길이의 False 리스트를 대입해야한다.
            result[2*i::i] = [False]*((n-i)//i)  # 헷갈리는 부분

    return [x for x in range(n+1) if result[x]]