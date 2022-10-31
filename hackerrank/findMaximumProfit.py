from audioop import findmax



def findMaximumProfit(n:int, category:list, price:list):
    from collections import defaultdict
    from heapq import heapify, heappop, heappush
    total = 0
    def binary_insert(array,num):
        if not array:
            array.append(num)
            return array
        else:
            if array[0] >= num:
                array = [num] + array
            elif array[-1] <= num:
                array.append(num)
            else:
                slow , fast = 0 , len(array)
                while slow <fast:
                    mid = (slow + fast) // 2
                    if num == array[mid]:
                        break
                    elif num < array[mid]:
                        fast = mid - 1
                    else:# num > array[mid]
                        slow = mid + 1
                array = array[:mid] + [num] + array[mid:]            
            return array
    hashtable = defaultdict(list)
    for i in range(len(category)):
        cat = category[i]
        cat_price = price[i]
        if cat not in hashtable:
            hashtable[cat].append(cat_price)
        else:
            hashtable[cat] = binary_insert(hashtable[cat],cat_price)
    print(hashtable)
    other = list()
    heapify(other)
    category_num = 0
    for i in range(len(hashtable.keys())):
        min_cat = min(hashtable,key=hashtable.get)
        # print(min_cat)
        category_num += 1
        total += category_num * hashtable[min_cat][0]
        hashtable[min_cat].remove(hashtable[min_cat][0])
        other += hashtable[min_cat]
        hashtable.pop(min_cat)
    for i in range(len(other)):
        temp_val = heappop(other)
        total += temp_val * category_num
    return total

                
        




n = 4
category = [3, 1, 2, 3, 4]
price = [2, 1, 4 , 4 , 7]
print(findMaximumProfit(n,category,price))


# a = [1,2,4,5,8]
# a.remove(a[0])
# print(a)