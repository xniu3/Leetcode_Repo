a = [52, 56, 55 , 4 , 7, 2, 920 , 904]
a.append(915)
print("a is now",a)
b = a
a[2] = 54
print("b is now ",b)
c = a.copy()
a[2] = 55
print("c is now ",c)
a[0] = 55
print("a is ",a,"a has 55 of " ,a.count(55))
d = [900, 917,918]
a.extend(d)
print("a is now",a)
a.insert(0,54)
print("a is now",a)
southgate = [6,9,701]
a.insert(0,southgate)
print("a is now",a)
a.pop(0)
print("a is now",a)