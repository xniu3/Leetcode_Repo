dogdistance = {'dog-dog': 33, 'dog-cat': 36, 'dog-car': 41, 'dog-bird': 42}
from collections import defaultdict
dogdistance2 = defaultdict(list)
dogdistance2["dog-dog"] = [1,14]
dogdistance2["dog-cat"] = [5,14]

e = min(dogdistance2, key=dogdistance2.get)

print(e)