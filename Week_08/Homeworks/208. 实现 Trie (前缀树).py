# https://leetcode-cn.com/problems/implement-trie-prefix-tree/

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        trie = self.root
        for w in word:
            if w not in trie:
                trie[w] = {}
            trie = trie[w]
        trie['end'] = {}

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        trie = self.root
        for w in word:
            if w in trie:
                trie = trie[w]
            else:
                return False
        return True if 'end' in trie else False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        trie = self.root
        for w in prefix:
            if w in trie:
                trie = trie[w]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)