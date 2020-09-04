import math
from fractions import gcd

def partitions(n, I=1):
    yield (n,)
    for i in range(I, n//2 + 1):
        for p in partitions(n-i, i):
            yield (i,) + p

def denom(list, number):
    dict = {}
    for number in list:
        dict[number] = dict.get(number, 0) + 1

    result = 1
    for i in range(1, number + 1):
        result *= i ** dict.get(i, 0)
        result *= math.factorial(dict.get(i, 0))

    return result

def gcds(partition1, partition2):
    result = 0
    for number1 in partition1:
        for number2 in partition2:
            result += gcd(number1, number2)
    return result

def solution(w, h, s):
    endDivisor = math.factorial(w) * math.factorial(h)
    result = 0
    for w_partition in partitions(w):
        for h_partition in partitions(h):
            result += math.factorial(w)//denom(w_partition, w) * math.factorial(h)//denom(h_partition, h) * (s ** gcds(w_partition, h_partition))

    return str(int(result // endDivisor))

print(solution(2, 3, 4))
print(solution(2, 2, 2))