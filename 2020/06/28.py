"""
Reconstruct Itinerary

Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

    If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
    All airports are represented by three capital letters (IATA code).
    You may assume all tickets form at least one valid itinerary.
    One must use all the tickets once and only once.

Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
"""

# approach: DFS using adjaceny matrix and stack
# memory: O(E)
# runtime: O(E)
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """

        # short circuit case: []
        if tickets == []: return []

        # build adjacency matrix
        am = {}
        for ticket in tickets:
            if ticket[0] not in am:
                am[ticket[0]] = []
            am[ticket[0]].append(ticket[1])

        # sort adjaceny matrix for lexical ordering
        for node in am:
            am[node].sort()

        # initialize itinerary and exploration stack
        it = []
        st = ['JFK']

        # process adjacency matrix and exploration stack
        while len(st) > 0:
            src = st[-1]
            # no nodes left to explore, add source to itinerary
            if src not in am or len(am[src]) == 0:
                it.append(src)
                st.pop()
            # add destination to stack, remove from adjency matrix
            else:
                dst = am[src][0]
                st.append(dst)
                am[src].remove(dst)

        # return itinerary in reverse order
        return(it[::-1])
