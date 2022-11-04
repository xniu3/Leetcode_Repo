

def substringRemoval(string:str):
    string = string.upper()
    ab_list = string.split("AB")
    ab_string = ''.join(ab_list)
    bb_list = ab_string.split("BB")
    return len(''.join(bb_list))
def substringRemoval2(string:str):
    stack = list()
    reduce_count = 0
    for char in string:
        if char == 'A':
            stack.append(char)
        else: # char == "B"
            if stack:
                stack.pop()
                reduce_count += 1
            else:
                stack.append(char)
    print("len string is ", len(string), "reduce count is ",reduce_count)
    return len(string) - reduce_count * 2
length = substringRemoval2("BAABBBA")
length = substringRemoval2("BABB")
print(length)
