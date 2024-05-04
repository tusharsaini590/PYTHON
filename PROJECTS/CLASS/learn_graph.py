def learn_graph():
    print('''
   A graph is an abstract data type (ADT) that consists of a set of objects, termed as vertices, interconnected via links called edges. 
   \nFormally, a graph is a pair of sets (V, E), where V is the set of vertices and E is the set of edges connecting the pairs of vertices.

\nGraphs can be represented using an array of vertices and a two-dimensional array of edges.
\n Key terms related to graphs include vertex (each node of the graph), edge (path between two vertices), adjacency (two vertices are adjacent if they are connected through an edge), and path (sequence of edges between two vertices).

\nCommon operations on graphs include creating a graph with vertices and edges, displaying the graph, and traversal. 
\nTraversal refers to visiting every vertex of the graph in a specific order. There are two types of traversals: Depth First Search (DFS) and Breadth First Search (BFS).

\nGraphs can be represented in various ways, such as Adjacency Matrix and Adjacency List. 
\nAn Adjacency Matrix is a V x V matrix where the values are filled with either 0 or 1, indicating whether a link exists between two vertices. An Adjacency List is a list of the vertices directly connected to the other vertices in the graph.

\nThere are two basic types of graphs: Directed Graph and Undirected Graph. 
\nIn a Directed Graph, edges possess a direction that goes either away from a vertex or towards the vertex.
 \nUndirected Graphs have edges that are not directed.

\nA Spanning Tree is a subset of an undirected graph that contains all the vertices of the graph connected with the minimum number of edges. A Minimum Spanning Tree (MST) is a subset of edges of a connected weighted undirected graph that connects all the vertices together with the minimum possible total edge weight.

\nThe shortest path in a graph is defined as the minimum cost route from one vertex to another. This is most commonly seen in weighted directed graphs but is also applicable to undirected graphs. The two common shortest path algorithms are Dijkstra’s Shortest Path Algorithm and Bellman Ford’s Shortest Path Algorithm.


\nCycles: A cycle in a graph is a non-empty trail in which the only repeated vertices are the first and last vertices. A directed graph (or digraph) is acyclic if there are no cycles in the graph.
\nConnectivity: A graph is said to be connected if there is a path between every pair of vertices. In a connected graph, there are no unreachable vertices. A graph that is not connected is disconnected.
\nGraph Isomorphism: Two graphs are said to be isomorphic if there is a one-to-one correspondence between their vertices and edges that preserve the connectivity.
\nSubgraph: A subgraph is a portion of a graph that constitutes a graph itself. Every graph is technically a subgraph of itself.
\nGraph Coloring: Graph coloring is a method to assign colors to the vertices of a graph G such that no two adjacent vertices have the same color.
\nGraph Matching: A matching in a graph is a set of edges chosen in such a way that no two edges share an endpoint. A maximum matching is a matching of maximum size (maximum number of edges). In a perfect matching, every vertex of the graph is connected to an edge in the matching.
\nGraph Cut: A cut is a partition of the vertices of a graph into two disjoint subsets. The cut-set of the cut is the set of edges whose end vertices have been separated by the cut.
\nGraph Partitioning: Graph partitioning is the problem of dividing a graph into parts, subject to various constraints and objectives, such as the size of the parts or the number of edges cut.
\nGraph Drawing: Graph drawing is the problem of assigning a geometric layout to a graph to optimize certain aesthetic criteria.
\nGraph Algorithms: There are several fundamental graph algorithms such as Depth-First Search (DFS), Breadth-First Search (BFS), Minimum Spanning Tree (MST), Dijkstra’s Algorithm, Floyd-Warshall Algorithm, etc.
\nApplications of Graphs: Graphs are used in numerous fields including computer science, operations research, chemistry, biology, linguistics, physics, sociology, and many others. They are used to model many types of relations and processes in various domains. For example, in computer networks, data organization, computational devices, the flow of computation, etc.
    
    ''')

def main():
   learn_graph()

if __name__ == "__main__":
    main()
