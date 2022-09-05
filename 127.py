class Solution:
    from typing import List
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import defaultdict,deque
        from heapq import heappush, heappop

        edges = defaultdict(list)
        wordID = dict()
        wordcount = 0
        def addword(word):
            nonlocal wordcount
            if word not in wordID:
                wordID[word] = wordcount
                wordcount += 1
            return 
        def addedge(word):
            addword(word)
            id1 = wordID[word]
            wordlen = len(word)
            wordlist = list(word)
            for i in range(wordlen):
                tempchar = wordlist[i]
                wordlist[i] = '*'
                newword = ''.join(wordlist)
                addword(newword)
                id2 = wordID[newword]
                edges[id1].append(id2)
                edges[id2].append(id1)
                wordlist[i] = tempchar
        addedge(beginWord)
        for word in wordList:
            addedge(word)
        
        if endWord not in wordID:
            return 0
        beginID, endID = wordID[beginWord] , wordID[endWord]
        queue = deque()
        # encoding = 'utf-8'
        queue.append(beginID)
        print("queue is originally ",queue)
        dp = [float('inf')] * wordcount
        dp[beginID] = 0
        while queue:
            print("queue is now ",queue)
            currID = queue.popleft()

            if currID == endID:
                break
            for nextID in edges[currID]:
                if dp[nextID] == float('inf'):
                    dp[nextID] = dp[currID] + 1
                else:
                    if dp[nextID] > dp[currID] + 1:
                        dp[nextID] = dp[currID] + 1
                queue.append(nextID)
                
        if dp[endID] == float('inf'):
            return 0
        else:
            return dp[endID] // 2 + 1
                
if __name__ == "__main__":
    Solu = Solution()
    ret = Solu.ladderLength(beginWord = "hot", endWord = "dog", wordList = ["hot","cog"])
    print(ret)
        
        
        
        
        
        
        
        
            
            