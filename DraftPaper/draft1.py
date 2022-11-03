def encode(string:str):
    vocab = dict()
    for char in string:
        if char not in vocab:
            vocab[char] = 1
        else:
            vocab[char] += 1
    ret = []
    print("vocab is ",vocab)
    for i in range(ord('a'), ord('z') + 1):
        char = chr(i)
        if char not in vocab:
            continue
        else:
            ret += [char] * vocab[char]
    return tuple(ret)
char = encode("west edmonton mall")
print(char)