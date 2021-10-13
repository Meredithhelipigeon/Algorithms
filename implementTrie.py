class Node(object):
    def __init__(self):
        self.children=[None]*27

class Trie(object):

    def __init__(self):
        self.trie=Node()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        t=self.trie
        for i in range(len(word)):
            diff=ord(word[i])-ord('a')
            if t.children[diff]==None:
                n=Node()
                t.children[diff]=n
            t=t.children[diff]
            if i==len(word)-1:
                nu=Node()
                t.children[-1]=nu
       
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        t=self.trie
        for i in range(len(word)):
            diff=ord(word[i])-ord('a')
            if t.children[diff]==None:
                return False
            else:
                if i==len(word)-1:
                    if t.children[diff].children[-1]==None:
                        return False
                t=t.children[diff]
        return True
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        t=self.trie
        for i in range(len(prefix)):
            diff=ord(prefix[i])-ord('a')
            if t.children[diff]==None:
                          return False
            else:
                          t=t.children[diff]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
