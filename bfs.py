from collections import defaultdict
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
		# self.visited.add(s)
		while queue: 
			print("queue:",queue)
			print("visited:",self.visited)
			s = queue.pop(0)
			print(s,end=" ")
			self.visited.add(s)
			print("self.graph",self.graph[s])
			for i in self.graph[s]: #For getting adjacent nodes from current node
				if i not in self.visited: 
					queue.append(i) 
					# self.visited.add(s)
g = Graph() 
# n=int(input("Edges:"))
# for i in range(n):
# 	edge=map(int,input().split(" "))
# 	g.addEdge(edge[0],edge[1])
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 

print ("Following is Breadth First Traversal"
				" (starting from vertex 2)") 
g.BFS(2) 

# a={}
# a["1"]=[0,1,2];
# print(a)