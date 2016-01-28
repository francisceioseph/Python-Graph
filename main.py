from graph import Graph


graph = Graph(30)

graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")
graph.add_node("E")
graph.add_node("F")

graph.add_arc(0,1)
graph.add_arc(1,2)

graph.add_arc_with_labels("F", "A")
graph.show_adjacency_matrix()