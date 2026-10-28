class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set: return 0
        if beginWord in word_set: word_set.remove(beginWord)

        m = len(beginWord)
        lowercase_alphabet = 'abcdefghijklmnopqrstuvwxyz'

        q = deque()
        q.append((beginWord, 1))

        while q:
            word, num_words = q.popleft()
            if word == endWord: return num_words
            for i in range(m):
                for c in lowercase_alphabet:
                    if c == word[i]: continue
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in word_set:
                        word_set.remove(new_word)
                        q.append((new_word, num_words + 1))
        return 0
