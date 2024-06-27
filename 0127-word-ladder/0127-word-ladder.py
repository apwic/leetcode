class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        n = len(beginWord)

        if endWord not in wordList:
            return 0

        all_word = defaultdict(set)
        for word in wordList:
            for i in range(n):
                all_word[(word[:i] + "*" + word[i+1:])].add(word)


        queue = deque([(beginWord, 1)])
        seen = set({beginWord})

        while queue:
            word, step = queue.popleft()

            if word == endWord:
                return step

            for i in range(n):
                temp_word = word[:i] + "*" + word[i+1:]
    
                for neighbor in all_word[temp_word]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        queue.append((neighbor, step+1))
                    
        return 0
                
        