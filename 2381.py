def convert(num:int):
    if 97 <= num and num <= 122:
        return num
    elif num < 97:
        num += 26 * ((97 - num - 1) // 26 + 1)
    else:
        num -= 26 * ((num - 122 - 1) // 26 + 1)
    return num
print(convert(174))