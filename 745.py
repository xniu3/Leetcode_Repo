class WordFilter:
    from collections import defaultdict
    from typing import List
    def __init__(self, words: List[str]):
        self.worddict = defaultdict(list)
        for word,wordid in enumerate(self.worddict):
            print("prefix is ",prefix , suffix)
            print("wordid is",wordid)
            prefix , suffix = word[0] , word[-1]
            self.worddict[prefix + suffix].append((word,wordid))
        
    def f(self, prefix: str, suffix: str) -> int:
        fix = prefix + suffix
        if fix not in self.worddict:
            return -1
        else:
            wordlist = self.worddict[fix]
            wordlist.sort(key=lambda word:word[1])
            return wordlist[-1][0]
if __name__ == '__main__':
    

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)