# Python3 program to print DFS traversal
# from a given graph
from collections import defaultdict
from ssl import VERIFY_ALLOW_PROXY_CERTS


# This class represents a directed graph using
# adjacency list representation
class Graph:

	# Constructor
	def __init__(self):

		# Default dictionary to store graph
		self.graph = defaultdict(list)

	
	# Function to add an edge to graph
	def addEdge(self, u, v):
		self.graph[u].append(v)
		self.visited=set()

	
	# The function to do DFS traversal. It uses
	def DFS(self, s):
		print(s, end=" ")
		self.visited.add(s)
		print("visited:",self.visited)
		print("self.graph",self.graph[s])
		for n in self.graph[s]:
			if n not in self.visited:
				self.DFS(n)
		print()


# Driver's code
if __name__ == "__main__":
	g = Graph()
	g.addEdge(0, 1)
	g.addEdge(0, 2)
	g.addEdge(1, 2)
	g.addEdge(2, 0)
	g.addEdge(2, 3)
	g.addEdge(3, 3)

	print("Following is Depth First Traversal (starting from vertex 2)")
	
	# Function call
	g.DFS(2)

# This code is contributed by Neelam Yadav
