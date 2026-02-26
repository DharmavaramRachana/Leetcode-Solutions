class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not endWord in wordList:
            return 0

        neiWord = collections.defaultdict(list)
        visit = set()

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                neiWord[pattern].append(word)


        q = deque([beginWord])
        visit.add(beginWord)
        res = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res

                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]

                    for nei in neiWord[pattern]:
                        if nei not in visit:
                            visit.add(nei)
                            q.append(nei)

                    neiWord[pattern] = []

            res += 1

        return 0

        
