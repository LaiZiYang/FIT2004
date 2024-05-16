from Queue import CircularQueue

class FlowNetwork:
    """
    Directed graph implementation using adjacency list.
    The vertex id is their index in the adjacency list.
    """

    def __init__(self, V):
        
        self.size = V
        self.flows = [None] * V
        self.residual = [None] * V
        for i in range(V):
            self.flows[i] = Vertex(i)
            self.residual[i] = Vertex(i)

    def add_edge(self, u, v, flow, lowerbound, capacity):
        
        # ref to vertices in flow network
        flow_u = self.flows[u]
        flow_v = self.flows[v]
        # ref to vertices in residual network
        residual_u:Vertex = self.residual[u]
        residual_v:Vertex = self.residual[v]

        # add flow path in flow network
        path = flow_u.add_edge(flow_v, flow, lowerbound, capacity)
        # print(path.capacity - path.flow)

        # add potential path in residual network, and store the reference of it inside flow path in flow network
        path.potential = residual_u.add_edge(residual_v, path.capacity-path.flow)

        # add backward path in residual network, and store reference of it inside potential path in residual network
        path.potential.backward = residual_v.add_edge(residual_u, path.flow)

        # store the potential path reference inside backward path
        path.potential.backward.potential = path.potential

        path.potential.flow_edge = path
        path.potential.backward.flow_edge = path

    def ford_fulkerson(self, source, destination):
        curr_flow = 0

        # while source can reach sink using bfs, run bfs
        # get the min flow that can be pump out of all path
        # back track to add flow
        have_path = True
        while have_path:
            
            curr = bfs(source, destination)
            if curr is None:
                have_path = False

            min = float('inf')
            found_path = []

            while curr is not None:
                if curr.incoming.flow < min:
                    min = curr.incoming.flow
                found_path.append(curr.incoming)
                curr = curr.prev

            for edge in found_path:
                self.update_flow(min, edge)

    def update_flow(self, flows, edge):
        edge.flow += 1
        edge.potential.flow -= 1
        edge.potential.backward

    def bfs(self, source, destination):
        for v in self.residual:
            v.visited = False
            v.prev = None
            v.incoming = None

        queue = CircularQueue(self.size)
        source_v = self.get_vertex(source)
        queue.append(source_v)
        self.residual[source].visited = True
        min = float('inf')
        while not queue.is_empty():
            curr_vertex = queue.serve()

            if curr_vertex.id == destination:
                v = curr_vertex
                route = []
                while v.incoming is not None:
                    route.append(v.incoming)
                    if v.free_space < min:
                        min = v.free_space
                    v = v.prev
                return curr_vertex
            
            for edge in curr_vertex.edges:
                
                if edge.flow > 0 and not edge.v.visited:
                    queue.append(edge.v)
                    edge.v.visited = True
                    if edge.v.prev is None:
                        edge.v.prev = curr_vertex
                        edge.v.free_space = edge.flow
                        edge.v.incoming = edge.flow_edge
        

    def add_vertex(self):
        
        new_vertex_id = len(self.vertices)
        self.vertices.append(Vertex(new_vertex_id))
        return self.vertices[new_vertex_id]
    
    def delete_vertex(self, id):
        
        self.vertices.pop(id)

    def get_vertex(self, id):
        
        return self.residual[id]

    def djikstra(self, s, destination):
        """
        Dijkstra's algorithm for finding the shortest path between two vertices
        
        Input:
            s: source vertex
            destination: destination vertex
        
        Return:
            shortest time/distance from source to destination

        Time complexity: 
            Best case analysis: O(E log V), where E is the number of edges, and V is the number of vertices
            Worst case analysis: O(E log V), where E is the number of edges, and V is the number of vertices
        Space complexity: 
            Input space analysis: O(1)
            Aux space analysis: O(V), where V is the number of vertices
        """

        # Initialize/reset all vertices:
        for vertex in self.vertices:
            vertex.distance = float('inf')
            vertex.visited = False
            vertex.prev = None

        
        # Set the source vertex distance to 0
        self.vertices[s].distance = 0

        # Initialize MinHeap with all vertices
        heap = MinHeap(len(self.vertices), self.vertices)
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
                        edge.v.prev = vertex    # Store the previous vertex, allowing to reconstruct the path
                        heap.update(edge.v.pos, edge.v.distance) # update discovered vertex's distance and its position in the minheap

        return self.vertices[destination].distance

class Vertex:
    """
    Class that represent vertex in a graph
    """
    def __init__(self, id) -> None:
        """
        Initialize a vertex.
        
        Time complexity: 
            Best case analysis: O(1)
            Worst case analysis: O(1)
        Space complexity: 
            Input space analysis: O(1)
            Aux space analysis: O(1)
        """
        self.id = id # id of vertex, its also the index of self inside the graph adjacency list
        self.edges = [] # all directed edges from self to other vertex
        self.prev = None # previous vertex, for djikstra backtracking
        self.visited = False
        self.distance = 0 # Distance from source vertex
        self.pos = None # Position in the heap's array (for update operation)
        self.incoming = None
    
    def add_edge(self, v, flow, lowerbound = None, capacity=None):
        edge = Edge(self, v, flow, lowerbound, capacity)
        self.edges.append(edge)
        return edge

    def __str__(self) -> str:
        return "Vertex " + str(self.id)

    def __repr__(self) -> str:
        return "Vertex " + str(self.id)

class Edge:
    """
    Class that represent an edge.
    """
    def __init__(self, u: Vertex, v: Vertex, flow, lowerbound=None, capacity=None) -> None:
        self.u = u
        self.v = v
        self.flow = flow
        self.lowerbound = lowerbound
        self.capacity = capacity
        self.potential = None
        self.backward = None
        self.flow_edge = None

if __name__ == "__main__":
    network_flow = Graph(5)
    network_flow.add_edge(0, 1, 2, 1, 2)
    network_flow.add_edge(0, 2, 1, 0, 4)
    network_flow.add_edge(0, 3, 1, 1, 1)
    network_flow.add_edge(1, 2, 1, 1, 3)
    network_flow.add_edge(3, 2, 3, 2, 4)
    network_flow.add_edge(3, 4, 1, 0, 1)
    network_flow.add_edge(2, 4, 1, 0, 3)

    v = network_flow.bfs(0, 4)
    print(v)

    route = []
    while v is not None:
        if route and v.id != route[0] or len(route) == 0: # if the solulu teleport to itself upon destroyed, only add the id to the route once
            route = [v.id] + route # if the tree is a duplicated tree, mod its id to the id of its corresponding original tree
        
        v = v.prev
    print(route)