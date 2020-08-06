"""
Add and Search Word - Data structure design

Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)

search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true

Note:
You may assume that all words are consist of lowercase letters a-z.
"""

# approach: trie with DFS
# memory: O(n) where n the number of nodes in the root WordDictionary
# runtime: O(n)
class WordDictionary:

    def __init__(self):
        self.trie = {}
        self.isEndOfWord = False

    def addWord(self, word: str) -> None:
        pointer = self
        for character in word:
            if character not in pointer.trie:
                # add the character to the current WD
                pointer.trie[character] = WordDictionary()
            # advance the pointer
            pointer = pointer.trie[character]
        # mark the current WD as a word
        pointer.isEndOfWord = True

    def search(self, word: str) -> bool:
        pointer = self
        # check every character
        for index, character in enumerate(word):
            if character == '.':
                # search every child WD
                for child in pointer.trie:
                    # if child has substring, bubble up True
                    if pointer.trie[child].search(word[index+1:]):
                        return True
                # no child had substring, bubble up False
                return False
            else:
                # advance the pointer if possible or stop searching
                if character in pointer.trie:
                    pointer = pointer.trie[character]
                else:
                    return False
        # the current WD has no children, evaluate if it's a word
        return pointer and pointer.isEndOfWord


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)