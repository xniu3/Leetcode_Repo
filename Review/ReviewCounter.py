from collections import Counter

def copy():
    counter1 = Counter("114514")
    print("counter1 is ",counter1)
    counter2 = counter1.copy()
    # print("counter2 is ",counter2)
    print("counter1 elements are ",counter1.elements())
    for element in counter1.elements():
        print("element is", element)
    print("counter1 most common is ",counter1.most_common())
    counter2 = Counter("1919810")
    print("counter2 is ",counter2)
    counter1.subtract(counter2)
    print("counter3 is ",counter1)
# copy()

def app():
    numlist = [1,9,1,9,8,1,0]
    count = Counter(numlist)
    hashtable = dict()
    for i in count.most_common():
        hashtable[i[0]] = i[1]
    print("hashtable is ",hashtable)
    # print(count.elements())
app()