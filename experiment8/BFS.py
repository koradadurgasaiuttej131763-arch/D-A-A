# What it does: Implements Breadth-First Search (BFS) — traverses a graph level by level 
#   (all immediate neighbors first, then their neighbors).
# Core Data Structure: Uses a Queue (deque) following FIFO (First-In, First-Out) order 
#   to visit vertices in order of arrival.
# Graph Representation: Uses an Adjacency List (Python dictionary of lists), 
#   which is memory-efficient for sparse graphs.
# Cycle Prevention: Uses a visited set to track processed nodes and avoid 
#   infinite loops in cyclic graphs.
# Why deque over list: deque.popleft() takes $O(1)$ time, whereas list.pop(0) takes $O(V)$ time.
# Time Complexity: $O(V + E)$ — visits every vertex ($V$) once and checks every edge ($E$).
# Space Complexity: $O(V)$ — for the queue and the visited set.
# Common Viva Question:
#   Difference from DFS: BFS uses a Queue and explores level-by-level 
#   (finds the shortest path in unweighted graphs); DFS uses a Stack/Recursion and 
#   goes as deep as possible first.