from graph import Graph

graph = Graph(
	["a", "b", "c", "d"],
	{
		("a", "b"): 4, 
		("a", "c"): 2, 
		("b", "d"): 1, 
		("c", "d"): 7
	}
)

path = graph.walk("a", "d")
print("Graph 1 walk has 3 steps - " + str(len(path) == 3))
print("Graph 1, step 1 - " + str(path[0] == "a"))
print("Graph 1, step 2 - " + str(path[1] == "b"))
print("Graph 1, step 3 - " + str(path[2] == "d"))



graph = Graph(
	["a", "b", "c", "d", "e", "f"],
	{
		("a", "b"): 7, 
		("a", "c"): 9, 
		("a", "f"): 14, 
		("b", "c"): 10,
		("b", "d"): 15,
		("c", "d"): 11,
		("c", "f"): 2,
		("d", "e"): 6,
		("f", "e"): 9
	}
)

path = graph.walk("a", "e")
print("Graph 1 walk has 4 steps - " + str(len(path) == 4))
print("Graph 2, step 1 - " + str(path[0] == "a"))
print("Graph 2, step 2 - " + str(path[1] == "c"))
print("Graph 2, step 3 - " + str(path[2] == "f"))
print("Graph 2, step 4 - " + str(path[3] == "e"))