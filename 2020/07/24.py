"""
All Paths From Source to Target

Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.

Example:
Input: [[1,2], [3], [3], []] 
Output: [[0,1,3],[0,2,3]] 
Explanation: The graph looks like this:
0--->1
|    |
v    v
2--->3
There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

Note:

    The number of nodes in the graph will be in the range [2, 15].
    You can print different paths in any order, but you should keep the order of nodes inside one path.
"""

# approach: dynamic programming
# memory: O(e), where e is all edges connected to the root
# runtime: O(e)
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # null check
        if graph == []:
            return graph

        # initialize start
        paths = []
        for edge in graph[0]:
            paths.append([0, edge])

        # no path from 0 exists
        if len(paths) == 0:
            return []

        # iterate on paths
        for index, node in enumerate(graph[1:]):
            for edge in node:
                for path in paths:
                    if path[-1] == index + 1:
                        paths.append(path + [edge])
        
        # filter and return paths whose last element is n - 1
        return list(filter(lambda a: a[-1] == len(graph) - 1, paths))


# approach: DFS and backtracking
# memory: O(e), where e is all edges in graph
# runtime: O(e), where e is all edges in solution
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        path = []
        paths = []
        self.processEdgesAtNode(graph, paths, path, 0)
        return paths

    def processEdgesAtNode(self, graph, paths, path, node):
        if node == len(graph) - 1:
            paths.append(path[:] + [node])
        else:
            for edge in graph[node]:
                path.append(node)
                self.processEdgesAtNode(graph, paths, path, edge)
                path.pop()
