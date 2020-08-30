def solution(l):
    afterDivis = []
    for i in range(len(l)):
        count = 0
        for j in range(i+1, len(l)):
            if l[j] % l[i] == 0:
                count += 1
        afterDivis.append(count)

    result = 0
    for i in range(len(l)):
        count = 0
        for j in range(i+1, len(l)):
            if l[j] % l[i] == 0:
                result += afterDivis[j]
    return result

print(solution([1, 2, 3, 4, 5, 6]))
print(solution([1, 1, 1]))