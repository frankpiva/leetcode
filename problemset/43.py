"""
43. Multiply Strings
Medium

3522

1386

Add to List

Share
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
 

Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""

# approach: mimic manual human multiplication
# memory: O(m + n) m = len(num1) and n = len(num2)
# runtime: O(m * n)

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"
        
        num1 = num1[::-1]
        num2 = num2[::-1]
        result  = [0] * (len(num1) + len(num2))
        start = 0
        
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                product = int(num1[i1]) * int(num2[i2])
                result[i1 + i2] += product
                result[i1 + i2 + 1] += (result[i1 + i2] // 10)
                result[i1 + i2] = result[i1 + i2] % 10
        
        result = result[::-1]
        while result[start] == 0:
            start += 1
        
        return "".join(map(str, result[start:]))
