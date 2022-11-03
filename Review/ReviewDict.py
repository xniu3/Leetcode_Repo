def key_value_item():
    hashtable = {
        55:"WEM",
        56:"Mill Woods",
        4:"Capilano",
        900:"Lewis Farms",               
        920:"University"
    }
    key = hashtable.keys()
    value = hashtable.values()
    items = hashtable.items()
    print("key is ",key, "Type of key is ",type(key))
    print("value is ",value, "Type of value is ",type(value))
    print("items is ",items, "Type of value is ",type(items))
    # print("items[0][0] is ",items[0][0], "Type of value is ",type(items[0][0]))
    

# key_value_item()
def get_pop():
    hashtable = {
        55:"WEM",
        56:"Mill Woods",
        4:"Capilano",
        900:"Lewis Farms",               
        920:"University"
    }
    for a,b in hashtable.items():
        print("key", a, b)
    clareview = hashtable.pop(4)
    print("clareview is ", clareview)
    belvedere = hashtable.popitem()
    print("belvedere is ", belvedere)
    # hashtable[belvedere[0]] = belvedere[1]
    belvedere = hashtable.popitem()
    print("belvedere is ", belvedere)
# get_pop()

def setDefault():
    hashtable = {
        55:"WEM",
        56:"Mill Woods",
        4:"Capilano",
        900:"Lewis Farms",               
        920:"University"
    }
    hashtable.setdefault(54)
    for key, value in hashtable.items():
        print(key , value)
    clareview = {54:"West Clareview", 55:"Meadows"}
    hashtable.update(clareview)
    print("--------- Updated ----------")
    for key, value in hashtable.items():
        print(key , value)
    abbottsfield = ["University", "Kingsway RAH"]
    hashtable.update(abbottsfield)
    print("--------- Abbottsfield Updated ----------")
    for key, value in hashtable.items():
        print(key , value)
# setDefault()

def key_types():
    hashtable = dict()
    hashtable[('a','b','c')] = 1 # set is hashable type
    #hashtable[['a','b','c']] = 2 # list is not hashtable type
    hashtable[('lewis farms','capilano')] = 2 # set is hashable type
    # hashtable[{4:'capilano'}] = 2 # dict is not hashtable type
    route8 = set()
    route8.add("University")
    route8.add("Abbottsfield")
    hashtable[route8] = 8
    hashtable[True] = 3
    print(hashtable)
key_types()