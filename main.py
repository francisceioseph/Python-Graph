from graph import Graph


graph = Graph(30)

graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")
graph.add_node("E")
graph.add_node("F")

graph.add_arc_with_labels("F", "A")
graph.add_arc_with_labels("A", "B")
graph.add_arc_with_labels("B", "C")

graph.show_adjacency_matrix()
