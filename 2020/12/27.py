"""
Jump Game IV

Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

    i + 1 where: i + 1 < arr.length.
    i - 1 where: i - 1 >= 0.
    j where: arr[i] == arr[j] and i != j.

Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.

 

Example 1:

Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
Output: 3
Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.

Example 2:

Input: arr = [7]
Output: 0
Explanation: Start index is the last index. You don't need to jump.

Example 3:

Input: arr = [7,6,9,6,9,6,9,7]
Output: 1
Explanation: You can jump directly from index 0 to index 7 which is last index of the array.

Example 4:

Input: arr = [6,1,9]
Output: 2

Example 5:

Input: arr = [11,22,7,7,7,7,7,7,7,22,13]
Output: 3

 

Constraints:

    1 <= arr.length <= 5 * 10^4
    -10^8 <= arr[i] <= 10^8
"""

# approach: dynamic programming
# passed 20/28 test cases
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
        # initialize values
        self.length = len(arr) - 1
        self.lookup = self.create_lookup(arr)
        self.minimum = -1
        
        # short circuit: single value
        if self.length == 1:
            return 1

        this_iteration = [(0, [], [0])]
        while self.minimum == -1:
            next_iteration = []
            for path in this_iteration:
                for possibility in path[2]:
                    next_moves = self.calculate_next_moves(path[0], possibility, path[1])
                    next_iteration.append((path[0] + 1, path[1] + [possibility], next_moves))
            this_iteration = next_iteration
                
        return self.minimum
                
        
    def create_lookup(self, arr: List[int]) -> List[int]:
        lookup = []
        for index, value in enumerate(arr):
            # initialize ld with element
            lookup.append([])
            # move left
            if index > 0:
                lookup[index].append(index - 1)
            # move right
            if index < len(arr) - 1:
                lookup[index].append(index + 1)
            # jump
            for jump_index, jump_value in enumerate(arr):
                if jump_value == value:
                    if jump_index != index:
                        if jump_index not in lookup[index]:
                            lookup[index].append(jump_index)
        # print(f"[DEBUG] lookup: {lookup}")
        return lookup
        
    
    def calculate_next_moves(self, count: int, index: int, visited: List[int]):
        if index == self.length:
            self.minimum = count
        return list(filter(lambda x: x not in visited , self.lookup[index]))
        
# approach: queue and adjacency list
# memory: O(n)
# runtime: O(n)
# passed 24/28 test cases
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
        # initialize values
        count = 0
        length = len(arr)
        lookup = {}
        queue = [0]
        visited = [0]
        
        # short circuit
        if length == 1:
            return 0
        
        # populate lookup
        for index, value in enumerate(arr):
            if value not in lookup:
                lookup[value] = []
            lookup[value].append(index)
                        
        while len(queue) > 0:
            count += 1
            size = len(queue)
            
            # for current members of the queue
            while size > 0:
                size -= 1
                index = queue.pop(0)
                adjacents = []
                if arr[index] in lookup:
                    adjacents += lookup[arr[index]]
                    del lookup[arr[index]]
                adjacents.append(index - 1)
                adjacents.append(index + 1)

                # consider all possibilities
                for possibility in adjacents:
                    if 0 < possibility < length:
                        if possibility not in visited:
                            # early exit
                            if possibility == length - 1:
                                return count
                            queue.append(possibility)
                            visited.append(possibility)
        
        # error code if nothing was found at this point
        return -1

# approach: queue and adjacency list
# memory: O(n)
# runtime: O(n)
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
        # initialize values
        count = 0
        length = len(arr)
        lookup = {}
        queue = [0]
        visited = [0]
        
        # short circuit
        if length == 1:
            return 0
        
        # populate lookup
        for index, value in enumerate(arr):
            if value not in lookup:
                lookup[value] = []
            lookup[value].append(index)
                        
        while len(queue) > 0:
            count += 1
            size = len(queue)

            # for current members of the queue
            for i in range(size):
                index = queue.pop(0)
                
                # only consider going backwards if a jump is possible
                if index - 1 >= 0 and arr[index - 1] in lookup:
                    queue.append(index - 1)
                
                # consider going forwards, check if it is the solution
                if index + 1 < length and arr[index + 1] in lookup:
                    if index + 1 == length - 1:
                        return count
                    queue.append(index + 1)
                    
                # consider jumps, check if they are the solution
                if arr[index] in lookup:
                    for possibility in lookup[arr[index]]:
                        if possibility != index:
                            if possibility == length - 1:
                                return count
                            queue.append(possibility)
                    
                    # remove jumps after all jumps have been processed
                    del lookup[arr[index]]

        return count