def solution(x, y):
    bigger = []
    smaller = []
    if len(x) > len(y):
        bigger = x
        smaller = y
    else:
        bigger = y
        smaller = x
    for number in bigger:
        if number not in smaller:
            return number

print(solution([13, 5, 6, 2, 5], [5, 2, 5, 13])) # should be 6
print(solution([14, 27, 1, 4, 2, 50, 3, 1], [2, 4, -4, 3, 1, 1, 14, 27, 50])) # should be -4