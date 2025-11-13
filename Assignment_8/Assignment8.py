import heapq 
 
# Graph represented as adjacency list with travel times 
# Each node (location) maps to a list of (neighbor, time) 
graph = { 
    'Shop': [('A', 4), ('B', 2)], 
    'A': [('Shop', 4), ('C', 3), ('D', 2)], 
    'B': [('Shop', 2), ('D', 4)], 
    'C': [('A', 3), ('D', 1), ('E', 5)], 
    'D': [('A', 2), ('B', 4), ('C', 1), ('E', 3)], 
    'E': [('C', 5), ('D', 3)] 
} 
 
def dijkstra(graph, start): 
    # Initialize distances 
    distances = {} 
    for node in graph: 
        distances[node] = float('inf') 
        distances[start] = 0 
    pq = [(0, start)]  # priority queue (time, node) 
 
    while pq: 
        current_time, node = heapq.heappop(pq) 
 
        if current_time > distances[node]: 
            continue 
 
        for neighbor, time in graph[node]: 
            new_time = current_time + time 
            if new_time < distances[neighbor]: 
                distances[neighbor] = new_time 
                heapq.heappush(pq, (new_time, neighbor)) 
 
    return distances 
 
# Execution 
start_location = 'Shop' 
result = dijkstra(graph, start_location) 
 
print(f"Minimum delivery times from {start_location}:") 
for location, time in result.items(): 
    print(f"{location}: {time} mins")