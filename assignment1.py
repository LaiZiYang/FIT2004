"""
Some header maybe?
Version control?
"""

# remember, no codes outside
# remember, NO PRINT anywhere else your marks is print(0)

# ==========
# Q1

def merge(left, right):
    """
    Fuse left and right fitmons

    Input:
        left:   left fitmon
        right:  right fitmon
    Return: fused fitmon

    Time complexity: 
        Best case analysis: O(1)
        Worst case analysis: O(1)
    Space complexity: 
        Input space analysis: O(1)
        Aux space analysis: O(1)
    """
    return [left[0], int(left[1]*left[2] + right[0]*right[1]), right[2]]

def fuse(fitmons):
    """
    Use the optimal combination to fuse all the fitmons, in order to get the maximum cuteness score.

    Approach: 
    The approach is reference from the idea from in the lecture about the Maximum Subarray problem in week 6. The idea is that
    the memorization matrix is filled up diagnally, and at each cell [i,j], the resulting fitmon of optimal fusing combinatioin 
    from fitmon[i] to fitmon[j] will be filled in. This is done by comparing each possible combination by using the previously
    computed result stored in the memo.

    The number of combination increases by 1 for every diagonal cells.

    Postcondition: Every cell [i][j] in the matrix represent the optimal fitmon fused from fitmon[i] ... fitmon[j]

    Input:
        fitmons: list of fitmons represented in tuple. 
            Example: [0.8, 21, 0.9], this fitmons has left affinity of 0.8, right affinity of 0.9, and cuteness score of 21
    Return:
        cuteness_score: maximum cuteness score of all fusing combination of all the fitmons

    Time complexity: 
        Best case analysis: O(N^3), where N is the number of fitmons
        Worst case analysis: O(N^3), where N is the number of fitmons
    Space complexity: 
        Input space analysis: O(N), where N is the number of fitmons
        Aux space analysis: O(N^2), for the memorisation matrix of N*N, where N is the number of fitmons
    """
    # initialize the memorization matrix
    memo = [None] * len(fitmons)
    for i in range(len(fitmons)):
        memo[i]= [None] * len(fitmons)
    
    # fill in the base case: when there is only 1 fitmons
    for i in range(len(fitmons)):
        memo[i][i] = fitmons[i]
    

    # fill in the upper diagonal part of the matrix diagonally
    for i in range(len(fitmons)):
        row = 0
        for col in range(i+1, len(fitmons)):
            max_score = -1
            optimal_fitmon = None
            # compare and find the best combination
            for j in range(row, col):
                curr_fitmon = merge(memo[row][j], memo[j+1][col])
                if curr_fitmon[1] > max_score:
                    max_score = curr_fitmon[1]
                    optimal_fitmon = curr_fitmon
            memo[row][col] = optimal_fitmon
            row += 1

    # get the final optimal fitmon after fusing all the fitmons
    cuteness_score = memo[0][len(fitmons)-1][1]
    return cuteness_score

# ==========
# Q2
class MinHeap:
    """
    Minheap ADT

    citation:
    this implementaion is referenced from the my FIT1008 A3 codes: https://github.com/LaiZiYang/FIT1008-A3/blob/main/heap.py.
    modifications are made in the implementation of this MinHeap.
    """

    MIN_CAPACITY = 1

    def __init__(self, max_size, initial_array):
        """
        Initialize a heap using the initial array.

        Inputs:
            max_size: length of the initial array
            initial_array: array of items to store inside a heap

        Time complexity: 
            Best case analysis: O(N)
            Worst case analysis: O(N)
        Space complexity: 
            Input space analysis: O(N)
            Aux space analysis: O(N)
        """
        self.max_size = max_size
        if initial_array is None:
            self.length = 0
        else:
            self.length = self.max_size = len(initial_array)

        self.array = [None] * (max(self.max_size, self.MIN_CAPACITY) + 1)

        if initial_array:
            self.heapify(initial_array)

    def heapify(self, items):
        """
        construct a heap out of the given items

        Input: 
            items: list of items to be constructed into heap

        Time complexity: 
            Best case analysis: O(N), where N is the length of items
            Worst case analysis: O(N), where N is the length of items
        Space complexity: 
            Input space analysis: O(N), where N is the length of items
            Aux space analysis: O(1)
        """
        for i in range(len(items)):
            item = items[i]
            item.pos = i+1
            self.array[i+1] = item

        for i in range(self.length//2, 0, -1):
            self.sink(i)

    def rise(self, index):
        """
        increase the level of the item at the given index in heap until it reach its
        final position.

        Input:
            index: index of the item to rise

        Time complexity: 
            Best case analysis: O(log N), where N is the number of items in the heap
            Worst case analysis: O(log N), where N is the number of items in the heap
        Space complexity: 
            Input space analysis: O(1)
            Aux space analysis: O(1)
        """
        item = self.array[index]

        while index//2 >= 1 and item < self.array[index//2]:
            self.array[index] = self.array[index // 2]
            self.array[index].pos = index
            index = index//2

        self.array[index] = item
        self.array[index].pos = index

    def add(self, item):
        """
        add new item into the heap.

        Input:
            item: new item to add to the heap.

        Time complexity: 
            Best case analysis: O(log N), where N is the number of items in the heap
            Worst case analysis: O(log N), where N is the number of items in the heap
        Space complexity: 
            Input space analysis: O(1)
            Aux space analysis: O(1)
        """
        if self.is_full():
            raise IndexError('Heap is full')

        self.length += 1
        self.array[self.length] = item
        item.pos = self.length
        self.rise(self.length)

    def update(self, pos, distance):
        """
        Update the value of item at given index with given value.

        Input:
            pos: index of the item to be updated
            distance: new value of the item

        Time complexity: 
            Best case analysis: O(log N)
            Worst case analysis: O(log N)
        Space complexity: 
            Input space analysis: O(1)
            Aux space analysis: O(1)
        """
        self.array[pos].distance = distance

        # either rise or sink, not both.
        self.rise(pos)
        self.sink(pos)

    def is_full(self):
        """
        Check if the heap is full.

        return: 
            Boolean indicating if the heap is full.

        Time complexity: 
            Best case analysis: O(1)
            Worst case analysis: O(1)
        Space complexity: 
            Input space analysis: O(1)
            Aux space analysis: O(1)
        """
        return self.length + 1== len(self.array)
    
    def is_empty(self):
        """
        Check if the heap is empty.

        return: 
            Boolean indicating if the heap is empty.

        Time complexity: 
            Best case analysis: O(1)
            Worst case analysis: O(1)
        Space complexity: 
            Input space analysis: O(1)
            Aux space analysis: O(1)
        """
        return self.length == 0

    def get_min_child(self, index):
        """
        return the index of the minimum child of the parent at the given index.

        Input:
            index: index of the parent

        Return:
            index of the minimum child
        
        Time complexity: 
            Best case analysis: O(1)
            Worst case analysis: O(1)
        Space complexity: 
            Input space analysis: O(1)
            Aux space analysis: O(1)
        """
        if index*2 == self.length or self.array[index*2] < self.array[index*2 + 1]:
            return index*2
        else:
            return index*2 + 1
        
    def sink(self, index):
        """
        decrease the level of the item at the given index in heap until it reach its
        final position.

        Input:
            index: index of the item to rise

        Time complexity: 
            Best case analysis: O(log N), where N is the number of items in the heap
            Worst case analysis: O(log N), where N is the number of items in the heap
        Space complexity: 
            Input space analysis: O(1)
            Aux space analysis: O(1)
        """
        item = self.array[index]

        while index*2 <= self.length:
            min_child_index = self.get_min_child(index)
            if item > self.array[min_child_index]:
                self.array[index] = self.array[min_child_index]
                self.array[index].pos = index
                index = min_child_index
            else:
                break

        self.array[index] = item
        self.array[index].pos = index

    def serve(self):
        """
        Serve out the item at the top of the heap (minimum item).

        Return:
            minimum item in the heap

        Time complexity: 
            Best case analysis: O(log N), where N is the number of items in the heap
            Worst case analysis: O(log N), where N is the number of items in the heap
        Space complexity: 
            Input space analysis: O(1)
            Aux space analysis: O(1)
        """
        if self.length == 0:
            raise IndexError('Heap is empty')
        
        item = self.array[1]
        self.length -= 1

        if self.is_empty():
            return item
        else:
            self.array[1] = self.array[self.length + 1]
            self.array[1].pos = 1
            self.sink(1)
            return item

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
    
    def add_edge(self, v, w):
        """
        Add edge between self and target vertex.

        Input:
            v: to vertex
            w: edge weight

        Time complexity: 
            Best case analysis: O(1)
            Worst case analysis: O(1)
        Space complexity: 
            Input space analysis: O(1)
            Aux space analysis: O(1)
        """
        self.edges.append(Edge(self, v, w))

    def __str__(self) -> str:
        return "Vertex " + str(self.id)

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
    """
    Class that represent an edge.
    """
    def __init__(self, u: Vertex, v: Vertex, w) -> None:
        """
        u: from vertex
        v: to vertex
        w: weight

        
        Time complexity: 
            Best case analysis: O(1)            
            Worst case analysis: O(1)
        Space complexity: 
            Input space analysis: O(1)
            Aux space analysis: O(1)
        """
        self.u = u
        self.v = v
        self.w = w

class Graph:
    """
    Directed graph implementation using adjacency list.
    The vertex id is their index in the adjacency list.
    """

    def __init__(self, V):
        """
        Initialize graph of given size. vertices's id are generated automatically based on 
        vertex position in the adjacency list.

        Input:
            V: number of vertices

        Time complexity: 
            Best case analysis: O(V), where v is the number of vertices
            Worst case analysis: O(V), where v is the number of vertices
        Space complexity: 
            Input space analysis: O(1)
            Aux space analysis: O(V), where v is the number of vertices
        """
        self.vertices = [None] * V
        for i in range(V):
            self.vertices[i] = Vertex(i)

    def add_edge(self, u, v, w):
        """
        add an edge from vertex u to vertex v with weight w

        Input:
            u: from vertex
            v: to vertex
            w: weight

        Time complexity: 
            Best case analysis: O(1)
            Worst case analysis: O(1)
        Space complexity: 
            Input space analysis: O(1)
            Aux space analysis: O(1)
        """
        vertex_u = self.vertices[u]
        vertex_v = self.vertices[v]

        vertex_u.add_edge(vertex_v, w)

    def add_vertex(self):
        """
        Add new vertex to the graph.
        The id of the new vertex == len(adjacency list before the new vertex is added)

        Return:
            new vertex

        Time complexity: 
            Best case analysis: O(1)
            Worst case analysis: O(1)
        Space complexity: 
            Input space analysis: O(1)
            Aux space analysis: O(1)
        """
        new_vertex_id = len(self.vertices)
        self.vertices.append(Vertex(new_vertex_id))
        return self.vertices[new_vertex_id]
    
    def delete_vertex(self, id):
        """
        Delete vertex of with given id.

        Input:
            id: id of vertex to delete

        Time complexity: 
            Best case analysis: O(1), when item popped is at the end of the list
            Worst case analysis: O(V), where N is the number of vertices in the adjacency list
        Space complexity: 
            Input space analysis: O(1)
            Aux space analysis: O(1)
        """
        self.vertices.pop(id)

    def get_vertex(self, id):
        """
        get vertex by id

        Input:
            id: id of the vertex to get

        Return:
            vertex with given id

        Time complexity: 
            Best case analysis: O(1)
            Worst case analysis: O(1)
        Space complexity: 
            Input space analysis: O(1)
            Aux space analysis: O(1)
        """
        return self.vertices[id]

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

class TreeMap:
    """
    Class that represent The Forest
    Approach: 
    The idea is that we want to modify the graph such that it enforce the djikstra to destroy exactly 1 solulu 
    before reaching the one of the exits. In order to do so, I duplicate the forest. If a solulu has yet been 
    destroyed, we will still be in the original forest; where else if we are in the duplicate forest, it means 
    that exactly 1 solulu has been destroyed.

    To make the definition above valid, I model the teleportation as a directed edge from the original forest to 
    the duplicate forest to link both forest together, and also ensure that teleportation only occured once, 
    i.e exactly 1 solulu is destroyed. Now, using this modified graph, I set the starting point to be tree in the 
    original forest, and the exits will be in the duplicate graph. Running dijkstra using such starting point and
    exits will force the algorithm to teleport exactly once (exactly 1 solulu is destroyed) before reaching the 
    exits.
    """

    def __init__(self, roads, solulus):
        """
        Initialization of the forest.
        Represent the forest using graph and modify the graph to enable djikstra to solve the problem

        Precondition:   all trees are linked together by roads, and there is at least 1 solulu
        Postcondition:  2 set of trees is represented in a graph: original and duplicated trees, they are
                        connected by the teleportation of solulu.

        Input:
            roads: list of tuples that represent road if form form: (u, v, w)
                    - u: starting tree
                    - v: ending tree
                    - w: time take from u to v
            solulus: list of tuples that represent solulu if form form: (x, y, z)
                    - x: solulu id
                    - y: time taken to destroy solulu x
                    - z: target tree id of solulu teleportation
        Return:
            None

        Time complexity: 
            Best case analysis: O(R + T), where R is the number of roads and T is the number of Tree
            Worst case analysis: O(R + T), where R is the number of roads and T is the number of Tree
        Space complexity: 
            Input space analysis: O(E) where E is the number of roads
            Aux space analysis: O(1)
        """

        # find total number of tree O(E)
        self.total_tree = -1
        for road in roads:
            self.total_tree = max(self.total_tree, max(road[0], road[1]) + 1)
        self.total_tree = max(self.total_tree, len(solulus)) # when there's no road, e.g only has 1 tree, number of solulu will determine the total tree

        # Duplicate the Original Forest:
        # initialize a graph containing original and duplicated forest.
        #       - the corresponding id of a tree in the original forest is equal to (id + total number of tree)
        #       - for example: 
        #       -       total tree = 7
        #       -       tree_x's id = 4
        #       -       duplicated tree_x's id = 7 + 4 = 11 
        self.graph = Graph(self.total_tree*2)

        # add edges both in the original and the duplicated forest
        for road in roads:
            self.graph.add_edge(road[0], road[1], road[2])
            self.graph.add_edge(road[0] + self.total_tree, road[1] + self.total_tree, road[2])

        # link the original and the duplicated graph by using solulu edges, which represent teleportation.
        # the direction is always from original to duplicate forest
        for solulu in solulus:
            self.graph.add_edge(solulu[0], solulu[2]+self.total_tree, solulu[1])
    
    def escape(self, start, exits):
        """
        Find the fastest route to escape the forest.
        To find the best exit, I add a edge from each exit to a new vertex with weight of 0.
        The new vertex will be the target destination of the djikstra algorithm. By doing so,
        If any of the exit is visited this new vertex is ensured to be visited next. Thus, 
        the previous of the new vertex is the best exit.

        Precondition:   The starting point is at the original vertex, start_tree.id <= total tree; 
                        destinations is at the duplicated vertex, total tree <= destination.id < total tree*2
        Postcondition:  at least 1 solulu has been destroyed and the path to the exit is the fastest path.

        Input:
            start: starting tree
            exits: destination trees, reaching one of them is enough, not all
        Return:
            (total_time, route):
                total_time: time taken to escape the forest
                route: path to escape the forest

        Time complexity: 
            Best case analysis: O(R log T), where R is the number of roads and T is the number of trees
            Worst case analysis: O(R log T), where R is the number of roads and T is the number of trees
        Space complexity: 
            Input space analysis: O(T) where T is the number of trees
            Aux space analysis: O(T) where T is the number of trees
        """
        # add a new vertex where all exits converge, which will be the destination of dijkstra
        # note: add_vertex() method will auto assign id for the new vertex based on its position in the graph's adjacency list
        # so the new vertex will always be 2*total_tree (original forest size + duplicate forest size)
        self.graph.add_vertex()

        # add edges between new vertex and each exits, with weight = 0, to ensure that which ever exit that is served first is the optimum exit
        for exit in exits:
            self.graph.add_edge(exit + self.total_tree, self.total_tree*2, 0)

        # run djikstra to find the time taken and the path
        total_time = self.graph.djikstra(start,self.total_tree*2)

        # get the optimum exit found
        v = self.graph.get_vertex(self.total_tree*2).prev

        # delete the destination vertex created earlier, to avoid the next call to this method to use the same vertex as destination
        self.graph.delete_vertex(self.total_tree*2)
        
        # backtrack from the optimum exit to reconstruct the path
        route = []
        while v is not None:
            if route and v.id != route[0] or len(route) == 0: # if the solulu teleport to itself upon destroyed, only add the id to the route once
                route = [v.id%self.total_tree] + route # if the tree is a duplicated tree, mod its id to the id of its corresponding original tree
            
            v = v.prev

        # return the total time taken and the route if there is one (route length > 0), otherwise return None
        if len(route) > 0:
            return (total_time, route)
        else:
            return None