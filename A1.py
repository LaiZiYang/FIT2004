"""
Some header maybe?
Version control?
"""

# remember, no codes outside
# remember, NO PRINT anywhere else your marks is print(0)

# ==========
# Q1

def function1(argv_something):
    """
    # do the same documentation as below...
    """
    # make sure no print at all!!!
    # print("hello")
    return 123

def fuse(fitmons):
    """
    This function does magic
    Written by l337coderblazeIT

    Precondition:
    Postcondition:

    Input:
        d: bla
        site_list: bla bla
    Return:
        cuteness_score: is the answer (of course do write properly)

    Time complexity: 
        Best case analysis:
        Worst case analysis:
    Space complexity: 
        Input space analysis:
        Aux space analysis::
    """
    # do something
    answer = []
    # loop 10
    for i in range(10):
        # call the function
        function1(i)
    # return answer
    cuteness_score = 0
    return cuteness_score

# ==========
# Q2

class TreeMap:
    """
    Some class???
    """

    def __init__(self, roads, solulus):
        """
        This init function that create magic
        Written by l337coderblazeIT

        Precondition:
        Postcondition:

        Input:
            roads: bla
            solulus: bla bla
        Return:
            None

        Time complexity: 
            Best case analysis:
            Worst case analysis:
        Space complexity: 
            Input space analysis:
            Aux space analysis::
        """
        self.something = None
    
    def escape(self, start, exits):
        """
        This climb function that performs magic
        Written by l337coderblazeIT

        Precondition:
        Postcondition:

        Input:
            start: bla
            exits: bla bla
        Return:
            (total_time, route):
            total_time: is the answer
            route: is the answer

        Time complexity: 
            Best case analysis:
            Worst case analysis:
        Space complexity: 
            Input space analysis:
            Aux space analysis::
        """
        # do something
        total_time = 0
        route = []
        return (total_time, route)

# ==========
# Main Run
# The following below should be deleted before your submission, but you can use it for testing etc... I am leaving it as an example...

# Q1
if __name__ == "__main__":
    # Example
    q1output = fuse([[0, 29, 0.9], [0.9, 91, 0.8], [0.8, 48, 0]])
    print(q1output)

# Q2
if __name__ == "__main__":
    # Example 1
    # The roads represented as a list of tuples
    roads = [(0,1,4), (1,2,2), (2,3,3), (3,4,1), (1,5,2),
    (5,6,5), (6,3,2), (6,4,3), (1,7,4), (7,8,2),
    (8,7,2), (7,3,2), (8,0,11), (4,3,1), (4,8,10)]
    # The solulus represented as a list of tuples
    solulus = [(5,10,0), (6,1,6), (7,5,7), (0,5,2), (8,4,8)]
    # Creating a TreeMap object based on the given roads
    myforest = TreeMap(roads, solulus)
     # Example 1.1
    start = 1
    exits = [7, 2, 4]
    q2output = myforest.escape(start, exits)
    print(q2output)