import heapq

class Graph:
    def __init__(self):
        self.edges = {}
        
    def add_edge(self, from_node, to_node, cost):
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append((to_node, cost))
        
    def ucs(self, start, goal):
        visited = set()
        queue = [(0, start, [])]  # (cost, node, path)
        
        while queue:
            cost, node, path = heapq.heappop(queue)
            if node not in visited:
                path = path + [node]
                visited.add(node)
                if node == goal:
                    return path, cost
                for next_node, next_cost in self.edges.get(node, []):
                    if next_node not in visited:
                        heapq.heappush(queue, (cost + next_cost, next_node, path))
        
        return [], float('inf')

# Example usage:
graph = Graph()
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 5)
graph.add_edge('B', 'D', 3)
graph.add_edge('C', 'D', 1)
graph.add_edge('C', 'E', 4)
graph.add_edge('D', 'E', 1)

start_node = 'A'
goal_node = 'E'
path, cost = graph.ucs(start_node, goal_node)

if path:
    print("Path from", start_node, "to", goal_node, ":", path)
    print("Cost:", cost)
else:
    print("No path found from", start_node, "to", goal_node)
