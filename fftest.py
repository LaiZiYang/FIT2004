from assignment2 import FlowNetwork

def test_case_1():
    network = FlowNetwork(2)
    network.add_edge(0, 1, 0, 0, 10)
    network.ford_fulkerson(0, 1)
    assert network.flow_network[0].edges[0].flow == 10
    print("Test Case 1 Passed")

def test_case_2():
    network = FlowNetwork(4)
    network.add_edge(0, 1, 0, 0, 10)
    network.add_edge(0, 2, 0, 0, 5)
    network.add_edge(1, 3, 0, 0, 5)
    network.add_edge(2, 3, 0, 0, 10)
    network.ford_fulkerson(0, 3)
    assert network.flow_network[0].edges[0].flow + network.flow_network[0].edges[1].flow == 10
    assert network.flow_network[1].edges[0].flow == 5
    assert network.flow_network[2].edges[0].flow == 5
    print("Test Case 2 Passed")

def test_case_3():
    network = FlowNetwork(4)
    network.add_edge(0, 1, 0, 0, 10)
    network.add_edge(0, 2, 0, 0, 10)
    network.add_edge(1, 2, 0, 0, 5)
    network.add_edge(2, 3, 0, 0, 10)
    network.ford_fulkerson(0, 3)
    assert network.flow_network[0].edges[0].flow + network.flow_network[0].edges[1].flow == 10
    assert network.flow_network[2].edges[0].flow == 10
    print("Test Case 3 Passed")

def test_case_4():
    network = FlowNetwork(6)
    network.add_edge(0, 1, 0, 0, 16)
    network.add_edge(0, 2, 0, 0, 13)
    network.add_edge(1, 2, 0, 0, 10)
    network.add_edge(1, 3, 0, 0, 12)
    network.add_edge(2, 1, 0, 0, 4)
    network.add_edge(2, 4, 0, 0, 14)
    network.add_edge(3, 2, 0, 0, 9)
    network.add_edge(3, 5, 0, 0, 20)
    network.add_edge(4, 3, 0, 0, 7)
    network.add_edge(4, 5, 0, 0, 4)
    network.ford_fulkerson(0, 5)
    assert sum(edge.flow for edge in network.flow_network[0].edges) == 23
    print("Test Case 4 Passed")

def test_case_5():
    network = FlowNetwork(3)
    network.add_edge(0, 1, 0, 0, 10)
    network.add_edge(1, 2, 0, 0, 10)
    network.add_edge(0, 2, 0, 0, 0)
    network.ford_fulkerson(0, 2)
    assert sum(edge.flow for edge in network.flow_network[0].edges) == 10
    print("Test Case 5 Passed")

if __name__ == "__main__":
    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
    test_case_5()
    print("All test cases passed!")
