class Graph:
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def add_edge(self, node, neighbour):
        if node not in self.graph_dict:
            self.graph_dict[node] = []
        self.graph_dict[node].append(neighbour)

    def iddf_search(self, start_node, goal_node, max_depth):
        for depth in range(max_depth + 1):
            result = self.depth_limited_dfs(start_node, goal_node, depth)
            if result is not None:
                return result
        return None

    def depth_limited_dfs(self, current_node, goal_node, depth_limit, visited=None):
        if visited is None:
            visited = set()

        if current_node == goal_node:
            return [current_node]

        if depth_limit == 0:
            return None

        visited.add(current_node)

        for neighbour in self.graph_dict.get(current_node, []):
            if neighbour not in visited:
                path = self.depth_limited_dfs(neighbour, goal_node, depth_limit - 1, visited)
                if path is not None:
                    return [current_node] + path

        return None


# Example usage:
if __name__ == "__main__":
    graph = Graph({
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    })

    start_node = 'A'
    goal_node = 'F'
    max_depth = 3

    path = graph.iddf_search(start_node, goal_node, max_depth)

    if path is not None:
        print("Path found:", ' -> '.join(path))
    else:
        print("Path not found within the depth limit.")
