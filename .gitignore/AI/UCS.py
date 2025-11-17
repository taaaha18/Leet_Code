import heapq


def uniform_cost_search(graph, start, goal):
    frontier=[]
    heapq.heappush(frontier,(0,start,[start]))

    visited=set()
     
    while frontier:
        cost, current, path= heapq.heappop(frontier)

        if current==goal:
            return cost, path
        if current in visited:
            continue
        visited.add(current) 

        for neighbor, edge_cost in graph.get(current,[]):
            if neighbor not in visited:
                new_cost=cost+edge_cost
                new_path=path+[neighbor]
                heapq.heappush(frontier,(new_cost,neighbor,new_path))
        
    return float('inf'), []


if __name__ == "__main__":
    
    graph = {
        'A': [('B', 1), ('C', 3)],
        'B': [('D', 4)],
        'C': [('D', 2)],
        'D': []
    }

    start = 'A'
    goal = 'D'

    cost, path = uniform_cost_search(graph, start, goal)
    print("Shortest cost:", cost)
    print("Path:", " -> ".join(path))          
