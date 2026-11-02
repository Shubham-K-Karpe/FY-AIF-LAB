
# FOOD DELIVERY NAVIGATION SYSTEM USING BFS

# Creating the city map
# 0 = Open Road
# 1 = Roadblock

city = [
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

# Starting and destination positions
restaurant = (0, 0)
customer = (4, 4)


# Function to find neighbouring roads
def get_neighbours(position):

    neighbours = [
        (position[0] + 1, position[1]),
        (position[0] - 1, position[1]),
        (position[0], position[1] + 1),
        (position[0], position[1] - 1)
    ]

    valid = []

    for x, y in neighbours:

        if x >= 0 and x < 5 and y >= 0 and y < 5:

            if city[x][y] == 0:
                valid.append((x, y))

    return valid


# BFS Search Function
def bfs(start, goal):

    queue = [[start]]
    visited = []

    while queue:

        # Taking the first path from queue
        path = queue.pop(0)

        position = path[-1]

        if position not in visited:

            visited.append(position)

            # Checking if customer is reached
            if position == goal:
                return path

            # Exploring neighbouring roads
            for neighbour in get_neighbours(position):

                new_path = path + [neighbour]

                queue.append(new_path)

    return None


# Intelligent Agent
print("====================================")
print("     FOOD DELIVERY NAVIGATION       ")
print("====================================")

print("\nRestaurant Position:", restaurant)
print("Customer Position:", customer)

print("\nAgent is searching for the best route...")

# Finding the shortest route
route = bfs(restaurant, customer)


# Displaying the result
if route:

    print("\nShortest Route Found!")

    print("Delivery Route:", route)

    print("Total Distance:", len(route) - 1, "steps")

    print("\nCity Map:")

    for i in range(5):

        for j in range(5):

            if (i, j) == restaurant:
                print("R", end=" ")

            elif (i, j) == customer:
                print("C", end=" ")

            elif (i, j) in route:
                print("*", end=" ")

            elif city[i][j] == 1:
                print("#", end=" ")

            else:
                print(".", end=" ")

        print()

    print("\nDelivery rider can proceed!")
    print("Order successfully delivered!")

else:

    print("\nNo available route found!")
    print("Delivery cannot be completed.")
