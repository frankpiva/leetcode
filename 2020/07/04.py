"""
Ugly Number II

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note:  

    1 is typically treated as an ugly number.
    n does not exceed 1690.
"""

# approach: naive brute force
# memory: O(n)
# runtime: O(n^2)
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # uglies = [1.0,2.0,3.0,4.0,5.0]
        uglies = [1,2,3,4,5]

        # short circuit cases: 0-4
        if n == 0: return 0
        if n < 5:
            print('n', n, uglies[n -1])
            return uglies[n - 1]
        
        while len(uglies) < n:
            nth += 1
            quotient2 = nth / 2.0
            if quotient2 in uglies:
                uglies.append(nth)
                continue
            
            quotient3 = nth / 3.0
            if quotient3 in uglies:
                uglies.append(nth)
                continue
            
            quotient5 = nth / 5.0
            if quotient5 in uglies:
                uglies.append(nth)
                continue
                
        print('n', n, uglies[-1])
        return uglies[-1]


# approach: iterative comparison
# memory: O(n)
# runtime: O(n)
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        uglies = [1]

        c2, c3, c5 = 0, 0, 0

        while len(uglies) < n:
            n2 = uglies[c2] * 2
            n3 = uglies[c3] * 3
            n5 = uglies[c5] * 5

            minimum = min([n2, n3, n5])
            if minimum not in uglies:
                uglies.append(minimum)

            if minimum == n2:
                c2 += 1
            elif minimum == n3:
                c3 += 1
            else:
                c5 +=1 

        return uglies[n-1]
