from CircularQueue import CircularQueue
from MinHeap import VerticesMinHeap

class Vertex:

    def __init__(self, id) -> None:
        self.id = id
        self.edges = []
        self.visited = False
        self.distance = 0 # Distance from source vertex
        self.pos = None # Position in the heap's array (for update operation)

    def __str__(self) -> str:
        return "Vertex " + str(self.id)
    
    def add_edge(self, v, w):
        self.edges.append(Edge(self, v, w))

    def __repr__(self) -> str:
        return "Vertex " + str(self.id)
    
    def __eq__(self, value: object) -> bool:
        self.distance == value.distance

    def __lt__(self, value: object) -> bool:
        return self.distance < value.distance
    
    def __le__(self, value: object) -> bool:
        return self.distance <= value.distance
    
    def __gt__(self, value: object) -> bool:
        return self.distance > value.distance
    
    def __ge__(self, value: object) -> bool:
        return self.distance >= value.distance

class Edge:

    def __init__(self, u: Vertex, v: Vertex, w) -> None:
        self.u = u
        self.v = v
        self.w = w

class Graph:
    """
    Undirected graph implementation using adjacency list
    """

    def __init__(self, V) -> None:
        self.vertices = [None] * len(V)
        for i in range(len(V)):
            self.vertices[i] = Vertex(V[i])

    def add_edge(self, u, v, w):
        u = self.get_vertex(u)
        v = self.get_vertex(v)

        u.add_edge(v, w)
        v.add_edge(u, w)

    def get_vertex(self, id):
        for vertex in self.vertices:
            if vertex.id == id:
                return vertex
        return None

    def djikstra(self, s, destination):
        # Initialize all vertices with distance = infinity and visited = False
        for vertex in self.vertices:
            vertex.distance = float('inf')
            vertex.visited = False

        # Set the source vertex distance to 0
        self.get_vertex(s).distance = 0

        # Initialize MinHeap with all vertices
        heap = VerticesMinHeap(len(self.vertices), self.vertices)
        print(heap.array)

        # Dijsktra's algorithm
        while not heap.is_empty():
            vertex = heap.serve()
            vertex.visited = True

            # Terminate if destination vertex is reached
            if vertex.id == destination:
                return vertex.distance
            
            # Perform edge relaxation
            for edge in vertex.edges:
                if not edge.v.visited:
                    if vertex.distance + edge.w < edge.v.distance:
                        edge.v.distance = vertex.distance + edge.w
                        heap.update(edge.v.pos, edge.v.distance)


    def __str__(self) -> str:
        string = ""
        for vertex in self.vertices:
            string += str(vertex) + "\n"
        return string


if __name__ == "__main__":
    graph = Graph([1, 2, 3, 4, 5, 6])
    
    # graph.vertices[0].add_edge(graph.vertices[3], 1)
    # graph.vertices[0].add_edge(graph.vertices[2], 1)
    # graph.vertices[1].add_edge(graph.vertices[3], 1)
    # graph.vertices[1].add_edge(graph.vertices[4], 1)
    # graph.vertices[2].add_edge(graph.vertices[4], 1)
    # graph.vertices[3].add_edge(graph.vertices[5], 1)

    graph.add_edge(1, 2, 5)
    graph.add_edge(1, 3, 2)
    graph.add_edge(1, 4, 10)
    graph.add_edge(2, 6, 2)
    graph.add_edge(3, 4, 5)
    graph.add_edge(3, 5, 4)
    graph.add_edge(4, 5, 3)
    graph.add_edge(4, 6, 9)
    graph.add_edge(5, 6, 7)

    # for vertex in graph.vertices:
    #     print("\n" + str(vertex.id))
    #     print("Adjacent vertices:")
    #     for edge in vertex.edges:
    #         print(edge.v.id, edge.w)


    print(graph.djikstra(1, 3))
    for vertex in graph.vertices:
        print(vertex.id, vertex.distance)
