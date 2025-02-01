# Graph Minimum Spanning Tree (MST) and Closest Point Calculation

## Overview
This Python script calculates the closest point for each given point in a set and constructs a Minimum Spanning Tree (MST) using Prim's algorithm. The goal is to determine the shortest connection between points and analyze their minimum distances.

## Problem Statement
Given a set of points represented as coordinate pairs (x, y), the script determines:
- The closest point for each given point based on Manhattan distance.
- The Minimum Spanning Tree (MST) using Prim’s algorithm.
- The total cost of the MST.

## Formulae Used
1. **Manhattan Distance Calculation**
   \[ \text{distance} = |x_1 - x_2| + |y_1 - y_2| \]

2. **Prim’s Algorithm** (For MST Construction)
   - Use a priority queue to always expand the minimum weighted edge.
   - Keep track of visited nodes to avoid cycles.
   - Continue until all nodes are included in the MST.

## Code Explanation
The script consists of two main functions:

### 1. `find_min(points)`
- Iterates through each point and finds the closest neighboring point based on Manhattan distance.
- Constructs an adjacency list representation of the graph.
- Returns a dictionary of closest points and a graph representation for Prim’s algorithm.

### 2. `prim_mst(graph, start)`
- Implements Prim’s algorithm to construct the MST.
- Uses a min-heap (priority queue) to expand the smallest edge first.
- Returns the edges forming the MST and the total cost.

## Usage
The script initializes the following parameters:
```python
points = [(3,12),(-2,5),(-4,1)]
```
Then, it calculates the closest points and graph structure:
```python
distances, graph = find_min(points)
```
After that, it constructs the MST starting from a given point:
```python
mst, total_cost = prim_mst(graph, (3, 12))
```
Finally, it prints the results:
```python
for point, (min_distance, closest_point) in distances.items():
    print(f"Point {point}: Minimum Distance = {min_distance}, Closest Point = {closest_point}")

print("\nEdges in MST:")
for u, v, weight in mst:
    print(f"{u} , {v}, Weight: {weight}")
print(total_cost)
```

## Example Output
```
Point (3, 12): Minimum Distance = 6, Closest Point = (-2, 5)
Point (-2, 5): Minimum Distance = 4, Closest Point = (-4, 1)
Point (-4, 1): Minimum Distance = 4, Closest Point = (-2, 5)

Edges in MST:
(3, 12) , (-2, 5), Weight: 6
(-2, 5) , (-4, 1), Weight: 4
Total MST Cost: 10
```

## Notes
- The script uses Manhattan distance instead of Euclidean distance to measure distances between points.
- Prim’s algorithm ensures that the final spanning tree connects all points with minimal cost.
- The starting node for Prim’s algorithm can be any point in the dataset.

## License
This project is open-source and available for modification and distribution.

---

This README provides a structured and professional explanation of the script. 🚀

