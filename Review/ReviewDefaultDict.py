from collections import defaultdict, Counter

def listDefaultDict():
    hashtable = defaultdict(list)
    hashtable[4] = ["Lewis Farms", "Capilano"]
    hashtable[8] = ["Abbottsfield", "University"]
    print(hashtable)
    hashtable = defaultdict(dict)
    print(hashtable)
    hashtable[{"Lewis Farms": "Capilano"}] = 4
    hashtable[8] = {"Abbottsfield": "University"}
listDefaultDict()

