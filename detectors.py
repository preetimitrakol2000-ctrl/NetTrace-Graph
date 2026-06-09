def check_routing_loops(graph, start_node, visited=None, stack=None):
    """Depth-First Search recursion to isolate circular routing loops (malicious relays)."""
    if visited is None:
        visited = set()
    if stack is None:
        stack = set()
        
    visited.add(start_node)
    stack.add(start_node)
    
    for neighbor in graph.adj_list.get(start_node, []):
        if neighbor not in visited:
            if check_routing_loops(graph, neighbor, visited, stack):
                return True
        elif neighbor in stack:
            return True
            
    stack.remove(start_node)
    return False
