"""
Dungeon Game

The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

 

Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.
-2 (K) 	-3 	3
-5 	-10 	1
10 	30 	-5 (P)

 

Note:

    The knight's health has no upper bound.
    Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.
"""

# naive greedy attempt, fails on test #33
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        health = 0
        minimum = 0
        n_inf = float('-inf')
        x = 0
        y = 0

        while x != len(dungeon) and y != len(dungeon[0]):
            print('x', x, 'y', y)
            health += dungeon[y][x]
            next_x = dungeon[y][x+1] if x + 1 < len(dungeon[0]) else n_inf
            next_y = dungeon[y+1][x] if y + 1 < len(dungeon) else n_inf
            if next_x > next_y:
                x += 1
            else:
                y += 1
            if health < minimum:
                minimum = health

        return abs(minimum) + 1

# dynamic attempt
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon) - 1
        n = len(dungeon[0]) - 1
        n_inf = float('-inf')
        
        for i in range(m,-1,-1):
            for j in range(n,-1,-1):
                down = dungeon[i+1][j] if i < m else n_inf # edge case
                right = dungeon[i][j+1] if j < n else n_inf # edge case
                maximum = max(down, right)
                if maximum == n_inf: # corner case
                    if dungeon[i][j] > 0:
                        dungeon[i][j] = 0
                else:
                    total = maximum + dungeon[i][j]
                    dungeon[i][j] = 0 if total > 0 else total
                
        return abs(dungeon[0][0]) + 1
