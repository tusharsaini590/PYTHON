class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, from_vertex, to_vertex):
        if from_vertex in self.graph and to_vertex in self.graph:
            self.graph[from_vertex].append(to_vertex)
        else:
            print("One or both vertices do not exist.")

    def display_graph(self):
        for vertex in self.graph:
            print(vertex, "->", self.graph[vertex])
def main():
    graph = Graph()
    while True:
        print("Graph Operations:")
        print("1. Add Vertex")
        print("2. Add Edge")
        print("3. Display Graph")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            vertex = input("Enter the vertex to add: ")
            graph.add_vertex(vertex)
        elif choice == "2":
            from_vertex = input("Enter the starting vertex: ")
            to_vertex = input("Enter the ending vertex: ")
            graph.add_edge(from_vertex, to_vertex)
        elif choice == "3":
            graph.display_graph()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
