import time

# DFS function
def dfs(graph, vertex, visited):
    if vertex not in visited:
        print(vertex, end=" ")
        visited.add(vertex)

        # Visit all adjacent vertices
        for neighbour in graph[vertex]:
            dfs(graph, neighbour, visited)


# Graph represented using adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Starting vertex
start_vertex = 'A'

# Set to store visited vertices
visited = set()

# Measure execution time
start_time = time.perf_counter()

print("DFS Traversal:")
dfs(graph, start_vertex, visited)

end_time = time.perf_counter()

# Calculate execution time
execution_time = end_time - start_time

print("\nExecution Time:", execution_time, "seconds")

# Complexity
print("Time Complexity: O(V + E)")
print("Space Complexity: O(V)")

# What it does: Implements Depth-First Search (DFS) — explores a graph by going 
#   as deep as possible along each branch before backtracking.
# Core Mechanism: Uses Recursion, which internally relies on the Call Stack 
#   (LIFO: Last-In, First-Out).
# Graph Representation: Uses an Adjacency List (dictionary mapping nodes to neighbors) for fast neighbor lookups.
# Cycle Prevention: Uses a visited set so nodes aren't processed twice, preventing infinite loops.
# Base Condition: The if vertex not in visited: check stops recursion when an already visited node is reached.
# Time Complexity: $O(V + E)$ — visits each vertex ($V$) once and traverses each edge ($E$).
# Space Complexity: $O(V)$ — used by the visited set and the recursion call stack (in the worst-case of a linear/skewed graph).
# Top Viva Difference (DFS vs BFS):
#    DFS: Uses a Stack / Recursion, dives deep first, great for cycle detection, topological sorting, and maze solving.
# BFS: Uses a Queue, explores level-by-level, finds the shortest path in unweighted graphs.