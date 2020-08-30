def solution(x, y):
    M, F = int(x), int(y)
    bigger = max(M, F)
    smaller = min(M, F)

    result = 0
    while smaller > 1:
        result += int(bigger/smaller)
        bigger %= smaller
        if smaller > bigger:
            bigger, smaller = smaller, bigger

    if smaller == 0:
        return "impossible"
    result += bigger - 1
    return str(result)

print(solution('4', '7'))
print(solution('2', '1'))