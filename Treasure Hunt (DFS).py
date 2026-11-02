
# TREASURE HUNT GAME USING DFS

# Creating the graph
graph = {
    'Entrance': ['Level 1'],
    'Level 1': ['Trap 1', 'Level 2'],
    'Level 2': ['Trap 2', 'Level 3'],
    'Level 3': ['Trap 3', 'Final Treasure'],
    'Trap 1': [],
    'Trap 2': [],
    'Trap 3': [],
    'Final Treasure': []
}


# Function to ask riddles
def solve_riddle(level):

    attempts = 3

    if level == 'Level 1':
        question = "What has keys but cannot open locks?"
        correct_answer = "keyboard"

    elif level == 'Level 2':
        question = "What has hands but cannot clap?"
        correct_answer = "clock"

    elif level == 'Level 3':
        question = "What gets wetter as it dries?"
        correct_answer = "towel"

    # Allowing 3 attempts
    while attempts > 0:

        print("\nRiddle:", question)
        answer = input("Your answer: ")

        if answer.lower() == correct_answer:
            print("Correct! You got a key.")
            return True

        else:
            attempts = attempts - 1
            print("Wrong answer!")

            if attempts > 0:
                print("Attempts remaining:", attempts)

    print("You failed this level!")
    return False


# DFS function
def dfs(start, goal):

    stack = [[start]]
    visited = []
    keys = []

    while stack:

        path = stack.pop()
        node = path[-1]

        if node not in visited:

            visited.append(node)
            print("\nExploring:", node)

            # Checking the level and solving its riddle
            if node == 'Level 1' or node == 'Level 2' or node == 'Level 3':

                if solve_riddle(node):
                    keys.append("Key")
                else:
                    continue

            # Checking if all three keys are collected
            if node == goal:

                if len(keys) == 3:
                    print("\nAll 3 keys collected!")
                    print("Final Treasure Unlocked!")
                    return path

            # Exploring neighbouring nodes
            for neighbour in graph[node]:
                new_path = path + [neighbour]
                stack.append(new_path)

    return None


# Starting the game
print("================================")
print("       TREASURE HUNT GAME       ")
print("================================")

print("\nSolve 3 riddles to collect 3 keys.")
print("Collect all keys to unlock the treasure!")

result = dfs('Entrance', 'Final Treasure')

# Displaying the final result
if result:
    print("\nCONGRATULATIONS!")
    print("You found the final treasure!")
    print("Your path:", result)

else:
    print("\nGAME OVER!")
    print("Treasure not found.")
