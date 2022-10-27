#
# heuristic.py
#
# This script defines a utility class that can be used as an implementation
# of a frontier state (location) evaluation function for use in route-finding
# heuristic search algorithms. When a HeuristicSearch object is created,
# initialization code can be executed to prepare for the use of the heuristic
# during search. In particular, a RouteProblem object is typically provided 
# when the HeuristicFunction is created, providing information potentially
# useful for initialization. The actual heuristic cost function, simply
# called "h_cost", takes a state (location) as an argument.
#
# YOUR COMMENTS INCLUDING CITATIONS
#
# Samuel Saldivar 10-13-2021


import route
from route import RoadMap




class HeuristicFunction:
    """A heuristic function object contains the information needed to
    evaluate a state (location) in terms of its proximity to an optimal
    goal state."""

    def __init__(self, problem=None):
        self.problem = problem
        # PLACE ANY INITIALIZATION CODE HERE
        self.goal = problem.goal
        self.map = problem.map



    def h_cost(self, loc=None):
        """An admissible heuristic function, estimating the cost from
        the specified location to the goal state of the problem."""
        # a heuristic value of zero is admissible but not informative
        value = 0.0
        goal = self.problem.goal
        problem = self. problem

        if loc is None:
            return value
        else:
            # PLACE YOUR CODE FOR CALCULATING value OF loc HERE
            #euclidean distance
            distance = problem.euclidean_distance(loc,goal)
            speed = 0
            roads = problem.actions(loc)
            start = loc
            current = start
            cost = 0
            for i in roads:#iterate through segments to get the costs
                    node = problem.result(current,i)
                    cost = problem.action_cost(current, node)
                    current = node


            value = distance/cost#time formula.












            return value

