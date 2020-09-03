def generatePositions(dimensions, position, distance):
    result = []
    left_right = []
    for i in range(-(distance//dimensions[0]), distance//dimensions[0] + 1): #generate locations along x-axis
        if i % 2 == 0:
            left_right.append((dimensions[0]*i + position[0], position[1]))
        else:
            left_right.append((dimensions[0]*i + (dimensions[0] - position[0] - 1), position[1]))
    for i in range(-(distance//dimensions[1]), distance//dimensions[1] + 1): #project x-axis locations over y-axis
        thisAxis
        if i % 2 == 0:
    return result


def solution(dimensions, your_position, guard_position, distance):
    your_positions = generatePositions(dimensions, your_position, distance)
    guard_positions = generatePositions(dimensions, guard_position, distance)

    print(your_positions)
    print(guard_positions)

print(solution([3,2], [1,1], [2,1], 4))
print(solution([300,275], [150,150], [185,100], 500))