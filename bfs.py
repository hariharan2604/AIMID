from collections import defaultdict
from math import e 
class Graph: 
	def __init__(self): 
		self.graph = defaultdict(list) 

	def addEdge(self,u,v): 
		self.graph[u].append(v) 
		self.visited=set() 

	def BFS(self, s): 
		queue = [] 
		# print(self.graph)
		queue.append(s) 
		self.visited.add(s)
		while queue: 
			# print("queue:",queue)
			# print("visited:",self.visited)
			s = queue.pop(0)
			print(s,end=" ")
			self.visited.add(s)
			# print("self.graph",self.graph[s])
			for i in self.graph[s]: 
				if i not in self.visited: 
					queue.append(i) 
					# self.visited.add(s)
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 

print ("Following is Breadth First Traversal"
				" (starting from vertex 2)") 
g.BFS(2) 

# This code is contributed by Neelam Yadav 
