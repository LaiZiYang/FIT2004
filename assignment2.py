from Queue import CircularQueue

def allocate(preferences, officers_per_orgs, min_shifts, max_shifts):
    # res = [None for _ in range(len(preferences))]
    # for i in range(len(res)):
    #     res[i] = [None for _ in range(len(officers_per_orgs))]
    #     for j in range(len(res[i])):
    #         res[i][j] = [[0, 0, 0]]*3
    res = [[[[0 for _ in range(3)] for _ in range(30)] for _ in range(len(officers_per_orgs))] for _ in range(len(preferences))]
            
    shift1_req = 0
    shift2_req = 0
    shift3_req = 0
    for org in officers_per_orgs:
        shift1_req += org[0]
        shift2_req += org[1]
        shift3_req += org[2]
    total_shift_req = shift1_req + shift2_req + shift3_req
    

    shift1_max_sup = 0
    shift2_max_sup = 0
    shift3_max_sup = 0
    for preference in preferences:
        shift1_max_sup += preference[0]
        shift2_max_sup += preference[1]
        shift3_max_sup += preference[2]

    # if (len(preferences) < total_shift_req 
    #     or shift1_max_sup < shift1_req 
    #     or shift2_max_sup < shift2_req 
    #     or shift3_max_sup < shift3_req 
    #     or total_shift_req//len(preferences) < min_shifts
    #     or total_shift_req//len(preferences) > max_shifts):
    #     return None
    
    day_padding = len(preference)
    shift_padding = day_padding + 30
    cds_padding = shift_padding + 90*len(preference)

    fn = FlowNetwork(0)
    security_officers = [None] * len(preferences)
    companies = [[[None for _ in range(3)] for _ in range(30)] for _ in range(len(officers_per_orgs))]
    so_days = [[None for _ in range(30)] for _ in range(len(preferences))]
    shifts = [[[None for _ in range(3)] for _ in range(30)] for _ in range(len(preferences))]

    for i in range(len(security_officers)):
        security_officers[i] = fn.add_vertex([i])
    
    for i in range(len(security_officers)):
        for j in range(30):
            so_days[i][j] = fn.add_vertex()

    for i in range(len(security_officers)):
        for j in range(30):
            for s in range(3):
                shifts[i][j][s] = fn.add_vertex()

    for i in range(len(officers_per_orgs)):
        for j in range(30):
            for s in range(3):
                companies[i][j][s] = fn.add_vertex([i,j,s])
    
    min_source = fn.add_vertex()
    max_source = fn.add_vertex()

    fn.add_edge(min_source.id, max_source.id, 0, 0, total_shift_req*30 - min_shifts*len(preferences))

    # print(min_shifts*len(preferences))
    # print(total_shift_req*30)

    for i in range(len(preferences)):
        fn.add_edge(min_source.id, security_officers[i].id, 0, 0, min_shifts)
        fn.add_edge(max_source.id, security_officers[i].id, 0, 0, max_shifts-min_shifts)
        for d in range(30):
            # k = security_officers[i]
            # p = so_days[i][d]
            fn.add_edge(security_officers[i].id, so_days[i][d].id, 0, 0, 1)
            for s in range(3):
                if preferences[i][s] == 1:
                    fn.add_edge(so_days[i][d].id, shifts[i][d][s].id, 0, 0, 1)
                else:
                    fn.add_edge(so_days[i][d].id, shifts[i][d][s].id, 0, 0, 0)
                for c in range(len(officers_per_orgs)):
                    fn.add_edge(shifts[i][d][s].id, companies[c][d][s].id, 0, 0, 1)
    
    sink = fn.add_vertex()
    for c in range(len(companies)):
        for d in range(30):
            for s in range(3):
                fn.add_edge(companies[c][d][s].id, sink.id, 0, 0, officers_per_orgs[c][s])
    
    fn.ford_fulkerson(min_source.id, sink.id)

    # for c in companies:
    #     for d in range(30):
    #         for s in range (s):
    #             for e in companies[c][d][s].incoming.forward_flow

    for edge in min_source.edges:
        # print(edge)
        if edge.flow < edge.capacity:
            return
    
    for c in range(len(companies)):
        for d in range(30):
            for s in range(3):
                for edge in companies[c][d][s].edges:
                    if edge.flow < edge.capacity:
                        return
                    
    # for path in min_source.data:
    #     accessor = []
    #     for i in range(1, len(path)-1):
    #         if path[i].data is not None:
    #             accessor = path[i].data + accessor
    #     print(accessor)
    #     res[accessor[0]][accessor[1]][accessor[2]][accessor[3]] = 1
    total = 0
    for i in range(len(security_officers)):
        for d in range(30):
            for s in range(3):
                for edge in shifts[i][d][s].edges:
                    if edge.flow > 0:
                    # accessor = [i]
                    # accessor.append(edge.v.data[0])
                    # accessor.append(edge.v.data[1])
                    # accessor.append(edge.v.data[2])
                        res[i][edge.v.data[0]][edge.v.data[1]][edge.v.data[2]] = 1
                        total+=1

    # print(res)
    # print(min_source.data)
    return res
    

    

    # flow_network = FlowNetwork(len(preferences) + len(officers_per_orgs) + 30*3)
    # source = flow_network.add_vertex()
    # sink = flow_network.add_vertex()
    # for i in range(len(preferences)):
    #     flow_network.add_edge(source.id, i, 0, 0, capacity=max_shifts)
    #     for d in range(30):
    #         flow_network.add_edge(i, d+day_padding, 0, 0, capacity=1)
    #         for s in range(3):
    #             if preferences[i][s] == 1:
    #                 flow_network.add_edge(d+day_padding, s+shift_padding, 0, 0, capacity=1)
    #             else:
    #                 flow_network.add_edge(d+day_padding, s+shift_padding, 0, 0, capacity=0)
    #             for c in range(len(officers_per_orgs)):
    #                 cds = cds_padding + d*90 + c*3 + s
    #                 flow_network.add_edge(s+shift_padding, cds, 0, 0, capacity=1)
    
    # for i in range(len(officers_per_orgs*30*3)):
    #     cds = cds_padding + i
    #     req = officers_per_orgs[(cds - cds_padding - d*90 - s)//3]
    #     flow_network.add_edge(cds, sink, 0, 0, capacity=req)

class Vertex:
    """
    Class that represent vertex in a graph
    """
    def __init__(self, id, data=None) -> None:
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
        # self.prev = None # previous vertex, for djikstra backtracking
        self.visited = False
        self.incoming = None
        # self.prev_path = None
        self.data = data
    
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
        self.u: Vertex = u
        self.v: Vertex = v
        self.flow = flow
        self.lowerbound = lowerbound
        self.capacity = capacity
        self.potential_flow: Edge = None
        self.backward_flow: Edge = None
        self.forward_flow: Edge = None

    def __str__(self) -> str:
        return f"u: {self.u} | v: {self.v} | ({self.lowerbound}/{self.flow}/{self.capacity})"
    
    def __repr__(self) -> str:
        return str(self)
class FlowNetwork:
    """
    Directed graph implementation using adjacency list.
    The vertex id is their index in the adjacency list.
    """

    def __init__(self, V):
        
        self.size = V
        self.flow_network = [None] * V
        self.residual_network = [None] * V
        for i in range(V):
            self.flow_network[i] = Vertex(i)
            self.residual_network[i] = Vertex(i)

    def add_edge(self, u, v, flow, lowerbound, capacity):
        
        # ref to vertices in flow network
        flow_u = self.flow_network[u]
        flow_v = self.flow_network[v]
        
        # ref to vertices in residual network
        residual_u:Vertex = self.residual_network[u]
        residual_v:Vertex = self.residual_network[v]

        # add flow path in flow network
        path = flow_u.add_edge(flow_v, flow, lowerbound, capacity)

        # add potential path in residual network, and store the reference of it inside flow path in flow network
        path.potential_flow = residual_u.add_edge(residual_v, path.capacity-path.flow)

        # add backward path in residual network, and store reference of it inside potential path in residual network
        path.backward_flow = residual_v.add_edge(residual_u, path.flow)

        path.potential_flow.forward_flow = path
        path.backward_flow.forward_flow = path
        
    def ford_fulkerson(self, source, destination):

        # while source can reach sink using bfs, run bfs
        # get the min flow that can be pump out of all path
        # back track to add flow
        have_path = True
        max_flow = 0
        while have_path:
            
            curr = self.bfs(source, destination)
            if curr is None:
                return

            min = float('inf')
            found_path = []

            # backtreack to build the path
            while curr is not None and curr.incoming is not None:
                # if curr.id == source:
                #     if curr.data is None:
                #         curr.data = []
                #     curr.data.append(found_path)
                if curr.incoming.flow < min:
                    min = curr.incoming.flow
                found_path.append(curr.incoming.forward_flow)
                curr = curr.incoming.u

            res = []
            if found_path[-1].u.data is None:
                found_path[-1].u.data = []
            # found_path[-1].u.data.append(found_path)
            lst = [found_path[0].v]
            for edge in found_path:
                lst.append(edge.u)
                self.update_flow(min, edge)
                res.append(edge)
            found_path[-1].u.data.append(lst)
            # print(res)
            max_flow += min
        return max_flow

    def update_flow(self, flows, edge: Edge):
        edge.flow += flows
        edge.potential_flow.flow -= flows
        edge.backward_flow.flow += flows

    def bfs(self, source, destination):
        for v in self.residual_network:
            v.visited = False
            v.prev = None
            v.incoming = None

        queue = CircularQueue(len(self.flow_network))

        source_v = self.get_residual_vertex(source)
        queue.append(source_v)
        self.residual_network[source].visited = True

        while not queue.is_empty():
            curr_vertex = queue.serve()

            if curr_vertex.id == destination:
                return curr_vertex
            
            for edge in curr_vertex.edges:
                
                if edge.flow > 0 and not edge.v.visited:
                    queue.append(edge.v)
                    edge.v.visited = True
                    edge.v.incoming = edge
        

    def add_vertex(self, data=None):
        
        new_vertex_id = len(self.flow_network)
        new_flow_network_vertex = Vertex(new_vertex_id, data)
        new_residual_network_vertex = Vertex(new_vertex_id, data)
        self.flow_network.append(new_flow_network_vertex)
        self.residual_network.append(new_residual_network_vertex)

        return new_flow_network_vertex
    
    def delete_vertex(self, id):
        
        self.vertices.pop(id)

    def get_residual_vertex(self, id):
        return self.residual_network[id]
    
    def get_network_flow_vertex(self, id):
        return self.flow_network[id]


if __name__ == "__main__":
    network_flow = FlowNetwork(5)
    source = network_flow.add_vertex()
    # print(source.edges)
    sink = network_flow.add_vertex()
    # print(sink.edges)
    # network_flow.add_edge(0, 1, 0, 0, 2)
    # network_flow.add_edge(0, 2, 0, 0, 4)
    # network_flow.add_edge(0, 3, 0, 0, 0)
    # network_flow.add_edge(1, 2, 0, 0, 2)
    # network_flow.add_edge(3, 2, 0, 0, 2)
    # network_flow.add_edge(3, 4, 0, 0, 3)
    # network_flow.add_edge(2, 4, 0, 0, 3)
    # print("======")
    # network_flow.add_edge(0, sink.id, 0, 0, 2)
    # print("======")
    # network_flow.add_edge(3, sink.id, 0, 0, 2)
    # print("======")
    # network_flow.add_edge(source.id, 2, 0, 0, 3)

    # v = network_flow.bfs(0, 4)
    # print(v)
    #####################
    network_flow.add_edge(source.id, 2, 0, 0, 4)
    network_flow.add_edge(source.id, 3, 0, 0, 3)
    network_flow.add_edge(0, sink.id, 0, 0, 2)
    network_flow.add_edge(1, sink.id, 0, 0, 5)
    network_flow.add_edge(0, 1, 0, 0, 2)
    network_flow.add_edge(1, 4, 0, 0, 2)
    network_flow.add_edge(2, 0, 0, 0, 3)
    network_flow.add_edge(2, 3, 0, 0, 3)
    network_flow.add_edge(3, 0, 0, 0, 2)
    network_flow.add_edge(3, 1, 0, 0, 3)
    network_flow.add_edge(4, 3, 0, 0, 2)
    #####################
    # route = []
    # while v is not None:
    #     if route and v.id != route[0] or len(route) == 0: # if the solulu teleport to itself upon destroyed, only add the id to the route once
    #         route = [v.id] + route # if the tree is a duplicated tree, mod its id to the id of its corresponding original tree
        
    #     v = v.prev
    # print(route)
    network_flow.ford_fulkerson(source.id,sink.id)

    edges = []
    for v in network_flow.flow_network:
        for e in v.edges:
            if e not in edges:
                edges.append(e)

    for e in edges:
        print(e)
    print(network_flow.get_network_flow_vertex(source.id).data)

    allocate([[1,1,1], [0,0,1], [1,0,1]], [[1,0,0], [0,0,0], [0,0,1]], 15, 30)