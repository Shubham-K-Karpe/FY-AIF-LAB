
# WAREHOUSE INVENTORY ROBOT USING A* SEARCH

# Creating warehouse grid
# 0 = Empty Space
# 1 = Obstacle (Storage Rack)

warehouse = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

# Starting and destination positions
start = (0, 0)
goal = (4, 4)


# Manhattan Distance Function
def heuristic(node, goal):

    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])


# A* Search Function
def astar(start, goal):

    open_list = [start]
    closed_list = []

    g_cost = {start: 0}
    f_cost = {start: heuristic(start, goal)}

    parent = {}

    while open_list:

        # Finding node with lowest f_cost
        current = open_list[0]

        for node in open_list:

            if f_cost[node] < f_cost[current]:
                current = node

        # Checking if destination is reached
        if current == goal:

            path = [goal]

            while path[-1] != start:
                path.append(parent[path[-1]])

            path.reverse()
            return path

        open_list.remove(current)
        closed_list.append(current)

        # Finding neighbouring positions
        neighbours = [
            (current[0] + 1, current[1]),
            (current[0] - 1, current[1]),
            (current[0], current[1] + 1),
            (current[0], current[1] - 1)
        ]

        for neighbour in neighbours:

            x = neighbour[0]
            y = neighbour[1]

            # Checking warehouse boundaries
            if x < 0 or x >= 5 or y < 0 or y >= 5:
                continue

            # Avoiding storage racks
            if warehouse[x][y] == 1:
                continue

            if neighbour in closed_list:
                continue

            # Calculating actual movement cost
            new_g = g_cost[current] + 1

            if neighbour not in g_cost or new_g < g_cost[neighbour]:

                parent[neighbour] = current

                g_cost[neighbour] = new_g

                f_cost[neighbour] = new_g + heuristic(neighbour, goal)

                if neighbour not in open_list:
                    open_list.append(neighbour)

    return None


# Starting the robot
print("================================")
print("     WAREHOUSE ROBOT SYSTEM     ")
print("================================")

print("Robot Starting Position:", start)
print("Product Destination:", goal)

result = astar(start, goal)


# Displaying the shortest path
if result:

    print("\nOptimal Path Found!")
    print("Robot Path:", result)

    print("Total Distance:", len(result) - 1, "steps")

    print("\nWarehouse Map:")

    for i in range(5):

        for j in range(5):

            if (i, j) == start:
                print("S", end=" ")

            elif (i, j) == goal:
                print("G", end=" ")

            elif (i, j) in result:
                print("*", end=" ")

            elif warehouse[i][j] == 1:
                print("#", end=" ")

            else:
                print(".", end=" ")

        print()

    print("\nRobot successfully reached the destination!")

else:

    print("\nNo path available!")
    print("Destination cannot be reached.")
