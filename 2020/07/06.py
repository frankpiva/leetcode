# approach naive iterate and increment
# memory: O(n)
# runtime: O(2n)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # short circuit case: last digit < 9
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        else:
            newList = digits[::-1]
            newList[0] += 1
            for i in range(0, len(newList)):
                if newList[i] == 10:
                    newList[i] = 0
                    if i == len(newList) - 1:
                        newList.append(1)
                    else:
                        newList[i+1] += 1
            return newList[::-1]


# approach: big brain iterate and increment
# memory: O(1)
# runtime: O(n)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # short circuit case: last digit < 9
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        else:
            index = len(digits) - 1
            digits[index] += 1
            while digits[index] == 10:
                digits[index] = 0
                index -= 1
                if index == -1:
                    digits = [1] + digits
                else:
                    digits[index] += 1
            return digits


# approach: one-liner
# memory: ???
# runtime: ???
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # cast to string, cast to list, join list, cast to int, increment, cast to string, cast to list
        return list(str(int(''.join(list(map(lambda x: str(x), digits))))+1))
