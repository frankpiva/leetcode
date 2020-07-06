# approach: naive convert and iterate
# memory: O(1)
# runtime: 0(1)
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # '031b' = 0: pad with 0's, 31: pad to 31 chars, b: convert to binary
        bx = format(x, '031b')
        by = format(y, '031b')
        counter = 0
        for i in range(0, len(bx)):
            if bx[i] != by[i]:
                counter += 1
        return counter

# approach: big brain convert and iterate
# memory: O(1)
# runtime: 0(1)
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1')
