def greedy_best_first_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    came_from[start] = None
    
    while not frontier.empty():
        current = frontier.get()
        
        if current == goal:
            break
        
        for next_node in graph.neighbors(current):
            if next_node not in came_from:
                priority = heuristic(goal, next_node)
                frontier.put(next_node, priority)
                came_from[next_node] = current
    
    return reconstruct_path(came_from, start, goal)
