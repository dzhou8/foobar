import numpy
from fractions import Fraction

def solution(pegs):
    numVars = len(pegs)-1

    if numVars == 1:
        result = Fraction(pegs[1]-pegs[0])*2/3
        return [result.numerator, result.denominator]

    b = []
    for i in range(numVars):
        b.append(Fraction(pegs[i+1] - pegs[i]))

    a = [[0 for x in range(numVars)] for y in range(numVars)]
    for i in range(len(a)):
        if i == 0:
            a[i][-1] = 2
        else:
            a[i][i-1] = 1
        a[i][i] = 1

    for subMat in a:
        for element in subMat:
            element = Fraction(element)
    for element in b:
        element = Fraction(element)
    radii = numpy.linalg.inv(a).dot(b)

    for radius in radii: #radius must be positive, and > 1
        if radius < 1:
            return [-1, -1]

    result = Fraction(radii[-1]*2).limit_denominator(100)

    return [result.numerator, result.denominator]


print(solution([4, 30, 50]))
print(solution([4, 17, 50]))