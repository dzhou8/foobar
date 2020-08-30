def solution(n):
    number = int(n)
    result = 0
    while number > 3:
        if number % 2 == 0:
            number /= 2
        elif number % 4 == 1:
            number -= 1
        else:
            number += 1
        result += 1
    result += (number - 1)
    return int(result)

print(solution('15'))
print(solution('4'))