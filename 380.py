class RandomizedSet:
    from random import randint
    def __init__(self):
        self.wordlist = dict()

    def insert(self, val: int) -> bool:
        if val in self.wordlist:
            self.wordlist[val] += 1
            return False
        else:
            self.wordlist[val] = 1
            return True
    def remove(self, val: int) -> bool:
        if val in self.wordlist:
            self.wordlist[val] -= 1
            if self.wordlist[val] == 0:
                self.wordlist.pop(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        k = randint(0,len(self.wordlist))
        print("length of self wordlist is ",self.wordlist)
        key = list(self.wordlist.keys())[k]
        # value = self.wordlist[key]
        return key