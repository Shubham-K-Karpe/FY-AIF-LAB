
# WAREHOUSE ROBOT PATH PLANNING
# Comparing BFS, DFS and A* Search

# Creating warehouse grid
# 0 = Empty Space
# 1 = Obstacle

warehouse = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)


# Function to find neighbouring positions
def get_neighbours(node):

    neighbours = [
        (node[0] + 1, node[1]),
        (node[0] - 1, node[1]),
        (node[0], node[1] + 1),
        (node[0], node[1] - 1)
    ]

    valid = []

    for x, y in neighbours:

        if x >= 0 and x < 5 and y >= 0 and y < 5:

            if warehouse[x][y] == 0:
                valid.append((x, y))

    return valid


# BFS Algorithm
def bfs(start, goal):

    queue = [[start]]
    visited = []

    while queue:

        path = queue.pop(0)
        node = path[-1]

        if node not in visited:

            visited.append(node)

            if node == goal:
                return path, len(visited)

            for neighbour in get_neighbours(node):

                new_path = path + [neighbour]
                queue.append(new_path)

    return None, len(visited)


# DFS Algorithm
def dfs(start, goal):

    stack = [[start]]
    visited = []

    while stack:

        path = stack.pop()
        node = path[-1]

        if node not in visited:

            visited.append(node)

            if node == goal:
                return path, len(visited)

            for neighbour in get_neighbours(node):

                new_path = path + [neighbour]
                stack.append(new_path)

    return None, len(visited)


# Manhattan Distance Function
def heuristic(node, goal):

    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])


# A* Search Algorithm
def astar(start, goal):

    open_list = [start]
    closed_list = []

    g_cost = {start: 0}
    f_cost = {start: heuristic(start, goal)}

    parent = {}

    while open_list:

        current = open_list[0]

        # Finding node with lowest f_cost
        for node in open_list:

            if f_cost[node] < f_cost[current]:
                current = node

        # Checking if goal is reached
        if current == goal:

            path = [goal]

            while path[-1] != start:
                path.append(parent[path[-1]])

            path.reverse()

            return path, len(closed_list) + 1

        open_list.remove(current)
        closed_list.append(current)

        for neighbour in get_neighbours(current):

            if neighbour in closed_list:
                continue

            new_g = g_cost[current] + 1

            if neighbour not in g_cost or new_g < g_cost[neighbour]:

                parent[neighbour] = current
                g_cost[neighbour] = new_g

                f_cost[neighbour] = new_g + heuristic(neighbour, goal)

                if neighbour not in open_list:
                    open_list.append(neighbour)

    return None, len(closed_list)


# Comparing all three algorithms
print("====================================")
print("    WAREHOUSE ROBOT PATH PLANNING")
print("====================================")

print("Start Position:", start)
print("Goal Position:", goal)


# Running BFS
bfs_path, bfs_visited = bfs(start, goal)

# Running DFS
dfs_path, dfs_visited = dfs(start, goal)

# Running A*
astar_path, astar_visited = astar(start, goal)


# Displaying BFS result
print("\n----- BFS RESULT -----")

if bfs_path:
    print("Path:", bfs_path)
    print("Path Cost:", len(bfs_path) - 1)
    print("Nodes Explored:", bfs_visited)


# Displaying DFS result
print("\n----- DFS RESULT -----")

if dfs_path:
    print("Path:", dfs_path)
    print("Path Cost:", len(dfs_path) - 1)
    print("Nodes Explored:", dfs_visited)


# Displaying A* result
print("\n----- A* RESULT -----")

if astar_path:
    print("Path:", astar_path)
    print("Path Cost:", len(astar_path) - 1)
    print("Nodes Explored:", astar_visited)


# Comparing the algorithms
print("\n===== FINAL COMPARISON =====")

if bfs_path and dfs_path and astar_path:

    print("BFS Path Cost:", len(bfs_path) - 1)
    print("DFS Path Cost:", len(dfs_path) - 1)
    print("A* Path Cost:", len(astar_path) - 1)

    print("\nShortest Path Algorithm: BFS and A*")
    print("A* uses Manhattan Distance to guide the robot.")

    print("\nRobot successfully reached the packing section!")
