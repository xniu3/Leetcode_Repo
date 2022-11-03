from select import select


def bubblesort():
    array = [55, 4, 52, 7, 56, 920, 918, 2]
    #[3,9,4,0,5,2]
    n = len(array)
    for i in range(n):
        terminal = n - i
        for j in range(0,terminal - 1):
            if array[j] < array[j + 1]:
                array[j + 1] , array[j] = array[j] , array[j + 1]
    print(array)
bubblesort()    

def selectsort():
    array = [51, 4, 8, 902, 723, 726, 404, 414]
    n = len(array)
    for i in range(n):
        min_index = i
        j = i
        while j < n:
            if j == i:
                j += 1
                continue
            if array[min_index] < array[j]:
                min_index = j
            j += 1
        array[min_index] , array[i] = array[i] , array[min_index]
    print(array)
selectsort()

def insertsort():
    array = [55, 708, 704, 701, 6, 702, 705, 507, 9]
    n = len(array)
    for i in range(1,n):
        element = array[i]
        j = i - 1
        while j >= 0:
            if array[j] > element:
                array[j + 1] = array[j]
                j -= 1
            else:
                break
        array[j + 1] = element
    print(array)
insertsort()

