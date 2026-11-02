# Import deque from collections module for fast queue operations (First-In, First-Out)
from collections import deque

# Map Pune city intersections as an adjacency list (Graph)
pune_roads = {
    'Swargate': ['Shivajinagar', 'Kothrud'],
    'Shivajinagar': ['Swargate', 'FC Road', 'Viman Nagar'],
    'FC Road': ['Shivajinagar', 'Kothrud'],
    'Kothrud': ['Swargate', 'FC Road', 'Hinjewadi'],
    'Viman Nagar': ['Shivajinagar'],
    'Hinjewadi': ['Kothrud']
}

# Define BFS function to find the shortest route between start and destination
def find_shortest_route(graph, start, destination):
    # Create a queue storing tuples of (current_location, path_taken_so_far)
    queue = deque([(start, [start])])
    
    # Create a set to track visited locations so we do not loop infinitely
    visited = set([start])
    
    # Continue searching as long as there are routes left in the queue
    while queue:
        # Remove and get the oldest route from the left side of the queue
        current_city, path = queue.popleft()
        
        # Check if we reached our target destination
        if current_city == destination:
            # Return the complete list of locations traveled
            return path
        
        # Loop through every directly connected neighbor of the current city
        for neighbor in graph[current_city]:
            # Check if this neighbor location has not been visited yet
            if neighbor not in visited:
                # Mark neighbor as visited
                visited.add(neighbor)
                # Add the neighbor and updated path history to the back of the queue
                queue.append((neighbor, path + [neighbor]))
                
    # Return None if no path exists between start and destination
    return None

# Set starting point in Pune
start_location = 'Swargate'

# Set target destination in Pune
target_location = 'Hinjewadi'

# Run BFS algorithm
result_path = find_shortest_route(pune_roads, start_location, target_location)

# Print the resulting shortest path formatted with arrows
print("Shortest Route:", " -> ".join(result_path))
