for i in range(ord('a'), ord('z')):
    for j in range(i + 1, ord('z')):
        print("i is", i, "j is ",j)
        print("i ^ j is ", i ^ j)
        assert(i ^ j > ord('z') or i ^ j < ord('a'))