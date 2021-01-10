"""
Word Ladder

Given two words beginWord and endWord, and a dictionary wordList, return the length of the shortest transformation sequence from beginWord to endWord, such that:

    Only one letter can be changed at a time.
    Each transformed word must exist in the word list.

Return 0 if there is no such transformation sequence.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog", return its length 5.

Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

 

Constraints:

    1 <= beginWord.length <= 100
    endWord.length == beginWord.length
    1 <= wordList.length <= 5000
    wordList[i].length == beginWord.length
    beginWord, endWord, and wordList[i] consist of lowercase English letters.
    beginWord != endWord
    All the strings in wordList are unique.
"""


# approach: BFS with queue
# memory: O(n)
# runtime: O(n)
# passes 43/43 test cases, but takes too long
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # short-circuit check       
        if endWord not in wordList:
            return 0
        
        level = 1
        queue = [beginWord]
        
        # while there are words to process
        while len(queue) > 0:
            # for every word currently in line
            for i in range(len(queue)):
                # get the front of the queue
                front = queue.pop(0)
                # compare it with every word in the word list
                remove = []
                for word in wordList:
                    # count the number of different characters
                    count = 0
                    for i in range(len(word)):
                        if front[i] != word[i]:
                            count += 1
                    # check if it is a valid transformation
                    if count == 1:
                         # check if we found the end word
                        if word == endWord:
                            return level + 1
                        queue.append(word)
                        remove.append(word)
                # remove all words we added to queue
                for word in remove:
                    wordList.pop(wordList.index(word))
            
            # increment level, process next word in queue
            level += 1

        return 0
