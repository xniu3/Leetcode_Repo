def is_functions():
    route = "Route9: Eaux Claires to Southgate"
    route1 = route.capitalize()
    print("route 1 is ## ",route1)
    route2 = dict()
    for index, char in enumerate(route):
        route2[index] =char.isalnum()
    print("route 2 is ##",route2)
    print("route 2 is ##",route[:6].isalnum())
    print("route 2 is ##",route[:7].isalnum())



is_functions()
