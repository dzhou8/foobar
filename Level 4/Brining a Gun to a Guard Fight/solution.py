import math

def dist(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def generatePositions(dimensions, position, distance):
    result = []
    left_right = []
    for i in range(-(distance//dimensions[0] + 1), distance//dimensions[0] + 2): #generate locations along x-axis
        if i % 2 == 0:
            left_right.append([dimensions[0]*i + position[0], position[1]])
        else:
            left_right.append([dimensions[0]*i + (dimensions[0] - position[0]), position[1]])
    for i in range(-(distance//dimensions[1] + 1), distance//dimensions[1] + 2): #project x-axis locations over y-axis
        thisAxis = list(left_right)
        if i % 2 == 0:
            for j in range(len(thisAxis)):
                thisAxis[j] = [thisAxis[j][0], dimensions[1]*i + thisAxis[j][1]]
        else:
            for j in range(len(thisAxis)):
                thisAxis[j] = [thisAxis[j][0], dimensions[1]*i + (dimensions[1] - thisAxis[j][1])]
        for elem in thisAxis:
            result.append(elem)
    return result


def solution(dimensions, your_position, guard_position, distance):
    dimensions[0]
    dimensions[1]

    your_positions = generatePositions(dimensions, your_position, distance)
    guard_positions = generatePositions(dimensions, guard_position, distance)

    your_positions.remove(your_position)

    # print(your_positions)
    # print(guard_positions)

    anglesDict = {}
    for your_pos in your_positions:
        beam = [your_pos[0] - your_position[0], your_pos[1] - your_position[1]]
        thisDistance = dist([0, 0], beam)
        angle = math.atan2(beam[1], beam[0])
        if thisDistance <= distance:
            if angle in anglesDict:
                if thisDistance < anglesDict[angle]:
                    anglesDict[angle] = thisDistance
            else:
                anglesDict[angle] = thisDistance

    # print(anglesDict)

    workingAngles = set()
    for guard_pos in guard_positions:
        beam = [guard_pos[0] - your_position[0], guard_pos[1] - your_position[1]]
        thisDistance = dist([0, 0], beam)
        angle = math.atan2(beam[1], beam[0])
        if thisDistance <= distance:
            if angle in anglesDict:
                if thisDistance < anglesDict[angle]:
                    anglesDict[angle] = thisDistance
                    workingAngles.add(angle)
            else:
                anglesDict[angle] = thisDistance
                workingAngles.add(angle)

    # print(workingAngles)
    return len(workingAngles)

print(solution([3,2], [1,1], [2,1], 4))
print(solution([300,275], [150,150], [185,100], 500))