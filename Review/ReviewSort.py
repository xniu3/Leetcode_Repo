def ListSort():
    a = [1, 1, 4, 5, 1, 4, ]
    a.sort()
    print(a)
# ListSort()
def ListSort1():
    routes = [
        ('Eaux Claires', 'Southgate', 9),
        ('Southgate', 'Davies', 6),
        ('Castle Downs', 'University', 51),
        ('West Edmonton Mall', 'Meadows', 55),
    ]
    routes.sort()
    print(routes)
    routes.sort(key=lambda student:student[0])
    print(routes)
    routes.sort(key=lambda student:student[1])
    print(routes)
    routes.sort(key=lambda student:student[2])
    print(routes)
    routes = sorted(routes,key=lambda student:student[0])
    print(routes)
    routes = sorted(routes,key=lambda student:student[0],reverse=True)
    print(routes)
ListSort1()

def Sorted():
    ets = {
        920:"West Edmonton Mall",
        8: "Abbottsfield",
        9: "Southgate"
    }
    ets1 = sorted(ets)
    print(ets1)
    print(ets)

# Sorted()