import math
import heapq


def find_min(points):
    results = {}
    graph = {point: [] for point in points}  
    for p1 in points:
       
        min_distance = 10000000000000 
        closest_point = None
        for p2 in points:
            if p1 != p2:
               
                distance = abs((p1[0] - p2[0])) + abs((p1[1] - p2[1]))
                print( distance)
               
                if distance < min_distance:
                    min_distance = distance
                    closest_point = p2
               
                graph[p1].append((p2, distance))
       
        results[p1] = (min_distance, closest_point)
    return results, graph


def prim_mst(graph, start):
    mst = []
    visited = set()
    total_cost = 0
    min_heap = [(0, start, None)]  # (cost, current_node, previous_node)
    
    while min_heap:
        cost, current, prev = heapq.heappop(min_heap)
        if current not in visited:
            visited.add(current)
            total_cost += cost
            if prev is not None:
                mst.append((prev, current, cost))
            
            for neighbor, weight in graph[current]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (weight, neighbor, current))
    return mst, total_cost


points = [(3,12),(-2,5),(-4,1)]


distances, graph = find_min(points)



for point, (min_distance, closest_point) in distances.items():
    print(f"Point {point}: Minimum Distance = {min_distance}, Closest Point = {closest_point}")


mst, total_cost = prim_mst(graph, (3, 12))


print("\nEdges in MST:")
for u, v, weight in mst:
    print(f"{u} , {v}, Weight: {weight}")
print(total_cost)
