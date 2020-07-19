"""
Course Schedule II

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .

Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .

Note:

    The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
    You may assume that there are no duplicate edges in the input prerequisites.
"""

# approach: recursion, timed out on test 43/44
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.catalog, self.needToTake, self.taken = {}, [], []

        for course in prerequisites:
            if course[0] not in self.catalog:
                self.catalog[course[0]] = [course[1]]
            else:
                self.catalog[course[0]] += [course[1]]

        for course in prerequisites:
            if not self.takePrerequisites([course[0]]):
                return []

        for i in range(numCourses):
            if i not in self.taken:
                self.taken.append(i)

        return self.taken


    def takePrerequisites(self, prerequisites: List[int]) -> bool:
        print(prerequisites, self.taken, self.needToTake)
        for course in prerequisites:
            print('course', course)
            # no prerequisites
            if course not in self.catalog:
                if course not in self.taken:
                    self.taken.append(course)
                    self.needToTake = list(filter((course).__ne__, self.needToTake))
            else:
                # add prerequisites to list of courses that need to be taken
                for prerequisite in self.catalog[course]:
                    self.needToTake.append(prerequisite)

                # a cyclic dependcy exists if the course already needs to be taken:
                if self.needToTake.count(course) > 1:
                    return False
                else:
                    if course in self.taken:
                        continue
                    else:
                        print('checking', course)
                        if not self.takePrerequisites(self.catalog[course]):
                            return False
                        self.taken.append(course)
                        self.needToTake = list(filter((course).__ne__, self.needToTake))

        return True


# approach: while, timed out on test 43/44
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:  
        canTake, needToTake, pqs = [], [], {}

        # populate list of courses we need to take
        for i in range(numCourses):
            needToTake.append(i)

        # populate dictionary of prerequisites
        for course in prerequisites:
            if course[0] not in pqs:
                pqs[course[0]] = [course[1]]
            else:
                pqs[course[0]] += [course[1]]

        # take all courses with no prerequisites
        for course in needToTake:
            if course not in pqs:
                canTake.append(course)
        for course in canTake:
            needToTake.remove(course)

        # take all other courses
        lastIteration = 0
        while len(needToTake) != lastIteration:
            lastIteration = len(needToTake)
            for course in needToTake:
                prerequisitesMet = True
                for preprerequisite in pqs[course]:
                    if preprerequisite not in canTake:
                        prerequisitesMet = False
                if prerequisitesMet:
                    canTake.append(course)
                    needToTake.remove(course)

        # return list of courses if it is possible
        if len(canTake) != numCourses:
            return []
        else:
            return canTake


# approach: adjacency matrix, in-degree list, and queue
# memory: O(V+E)
# runtime: O(V+E)
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacencyMatrix, inDegreeList, order, processedNodes, queue = [], [], [], 0, []

        # initialize adjacency matrix and in-degree list
        for i in range(numCourses):
            adjacencyMatrix.append([])
            inDegreeList.append(0)
    
        # populate adjacency matrix and in-degree list
        for course in prerequisites:
            adjacencyMatrix[course[1]].append(course[0])
            inDegreeList[course[0]] += 1
   
        # populate queue
        for index, degree in enumerate(inDegreeList):
            if degree == 0:
                queue.append(index)

        # process queue
        while len(queue) != 0:
            node = queue.pop(0)
            order.append(node)
            processedNodes += 1
            # update adjacency matrix
            for adjacentNode in adjacencyMatrix[node]:
                inDegreeList[adjacentNode] -= 1
                if inDegreeList[adjacentNode] == 0:
                    queue.append(adjacentNode)

        # check if a cyclic dependency exists
        if processedNodes != numCourses:
            return []
        else:
            return order
