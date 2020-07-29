"""
Task Scheduler

You are given a char array representing tasks CPU need to do. It contains capital letters A to Z where each letter represents a different task. Tasks could be done without the original order of the array. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

You need to return the least number of units of times that the CPU will take to finish all the given tasks.

 

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.

Example 2:

Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.

Example 3:

Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A

 

Constraints:

    The number of tasks is in the range [1, 10000].
    The integer n is in the range [0, 100].
"""

# approach: right idea, wrong implementation
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # special case: no buffer
        if n == 0:
            return len(tasks)

        import collections

        counter = collections.Counter(tasks)
        # print(counter)

        # initialize list
        order = []
        largest = max(counter)
        for i in range(counter[largest]):
            order.append(largest)
            for j in range(n):
                order.append('idle')
        del counter[largest]
        idleIndex = 1
        # print(order)
        # print(counter)
        while len(counter) > 0:
            for task in list(counter):
                # print(task)
                for i in range(counter[task]):
                    # print(idleIndex + i * (n + 1))
                    nextIdle = idleIndex + i * (n + 1)
                    order[nextIdle] = task
                idleIndex = order.index('idle')
                del counter[task]
        # print(order)

        # for loop only
        idleIndex = 0
        for task in list(counter):
            # print(task)
            for i in range(counter[task]):
                # print(idleIndex + i * (n + 1))
                nextIdle = idleIndex + i * (n + 1)
                order[nextIdle] = task
            idleIndex = order.index('idle')
            del counter[task]

        # remove extra idles
        while order[-1] == 'idle':
            order.pop(len(order) - 1)

        # return length of pipeline
        return len(order)

# approach: dynamic programming
# memory: O(1)
# runtime: O(n)
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # early exit optimization
        if n == 0:
            return len(tasks)

        # initialize, populate, and sort the frequency of all tasks
        frequencies = [0] * 26
        for task in tasks:
            frequencies[ord(task) - 65] += 1        
        frequencies = sorted(frequencies)

        # calculate the maximum possible number of idle slots
        maximum = frequencies[25] - 1
        idles = maximum * n

        # loop from most frequent to least frequent, "filling" idle slots
        # in the event of a tie the original maximum was decreased by 1
        # this accounts for tasks that get added to the end of the optimization
        # without subtracting an extra slot from the middle
        # ex: [A,A,A,B,B,B], maximum: 3 - 1 = 2  
        # ex: A - - A - - A -> A B - A B - A B
        # the third B was added to the end, so we decrease idles by the maximum (2)
        for frequency in frequencies[24::-1]:
            idles -= min(frequency, maximum)

        # the leftover idle cycles are added back into the number of tasks, if they exist
        if idles > 0:
            return len(tasks) + idles
        else:
            return len(tasks)
