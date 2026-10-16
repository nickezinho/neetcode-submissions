class TrieNode:
    def __init__(self):    
        self.children = {}
        self.endOfWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
            
    def search(self, word: str) -> bool:
        current = self.root

        def dfs(idx, cur):
            if idx == len(word):
                return cur.endOfWord

            if word[idx] != '.':
                if word[idx] not in cur.children:
                    return False
                cur = cur.children[word[idx]]
                return dfs(idx + 1, cur)
            

            if word[idx] == '.':
                for c in cur.children:
                    res = dfs(idx + 1, cur.children[c])
                    if res:
                        return True
                return False

        ans = dfs(0, current)
        return ans
