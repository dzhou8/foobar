result = []

def dfs(currentID, totalTime, shortest_path, visited, times_limit):
    if currentID == len(shortest_path) - 1:
        if totalTime <= times_l

def solution(times, times_limit):
    global result
    shortest_path = [row[:] for row in times]

    # floyd warshall
    for k in range(len(shortest_path)):
        for i in range(len(shortest_path)):
            for j in range(len(shortest_path)):
                if shortest_path[i][j] > shortest_path[i][k] + shortest_path[k][j]:
                    shortest_path[i][j] = shortest_path[i][k] + shortest_path[k][j]

    # print(shortest_path)

    #check for negative loop
    for i in range(len(shortest_path)):
        if shortest_path[i][i] < 0:
            for j in range(1, len(shortest_path)-1)
                result.append(j-1)
            return result

    visited = []
    dfs(0, 0, shortest_path, list(visited), times_limit)



print(solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1))
print(solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3))