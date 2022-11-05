

def decipheringString(string:str,k:int):

    # def distance(chara:str, charb:str):
    #    return (ord(chara) - ord(charb) ) % 26 if (ord(chara) - ord(charb) ) % 26 < (ord(charb) - ord(chara) ) % 26 else (ord(charb) - ord(chara) ) % 26
    # print(distance('a','z'))
    remain , i = k , 0
    newlist = list()
    n = len(string)
    while i < n:
        if string[i] == 'a':
            newlist.append(string[i])
        else:
            if ord(string[i]) - ord('a') < remain:
                newlist.append('a')
                remain -= ord(string[i]) - ord('a')
            else:
                newlist.append(chr(ord(string[i]) - remain))
                break
        i += 1
    if i != n - 1:
        newlist.append(string[i + 1:])
    return ''.join(newlist)
print(decipheringString("gx",4))
