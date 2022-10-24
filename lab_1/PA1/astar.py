#
# astar.py
#
# This file provides a function implementing A* search for a route finding
# problem. Various search utilities from "route.py" are used in this function,
# including the classes RouteProblem, Node, and Frontier. Also, this function
# uses heuristic function objects defined in the "heuristic.py" file.
#
# YOUR COMMENTS INCLUDING CITATIONS
#
# YOUR NAME - THE DATE
#


from route import Node
from route import Frontier


def a_star_search(problem, h, repeat_check=False):
    """Perform A-Star search to solve the given route finding problem,
    returning a solution node in the search tree, corresponding to the goal
    location, if a solution is found. Only perform repeated state checking if
    the provided boolean argument is true."""

    # PLACE YOUR CODE HERE
    #  node containing initial state of the problem
    startNode = Node(problem.start)
    # return  Node if it contains goal node
    if problem.is_goal(startNode):
        return startNode
    # add startNode to frontier,initializing a queue
    queue = Frontier(startNode, True)
    # reached set must contain startNode
    path = set()
    if repeat_check:
        path.add(startNode.loc)

    # while frontier is not empty
    while not queue.is_empty():
        # node that has just been removed
        popped = queue.pop()
        # return if goal node
        if problem.is_goal(popped.loc):
            return popped
        # expand removedNode then iterate

        for i in popped.expand(problem):
            # add child to  frontier
            current = i.loc

            if repeat_check:
                current = i.loc
                if current in path:  # if the child is in the reached set
                    if i in queue:
                        if Node.value(i) < Node.value(popped):
                            queue.pop()
                            queue.add(i)
                else:
                    queue.add(i)
                    path.add(current)  # adds to reached set
            else:
                queue.add(i)
                path.add(current)  # adds to reached set

    return None  # none is failure
