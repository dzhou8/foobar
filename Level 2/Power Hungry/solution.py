def solution(xs):
    if len(xs) == 1:
        return str(xs[0])

    positive = False
    result = 1
    negative = []
    for panel in xs:
        if panel > 0:
            positive = True
        if panel != 0:
            result *= panel
        if panel < 0:
            negative.append(panel)

    if not positive and len(negative) < 2:
        return "0"

    negative.sort(reverse=True)
    if len(negative) % 2 == 1: # don't multiply by the smallest negative number
        result /= negative[0]

    return str(int(result))


print(solution([2, 0, 2, 2, 0]))
print(solution([-2, -3, 4, -5]))