
def solution(array:list):
    global obs
    obs = list()
    ret = list()
    if not array:
        return array
    def binary_add(value):
        global obs
        if not obs:
            obs.append(value)
        else:
            if obs[0] > value:
                obs = [value] + obs
            elif obs[-1] < value:
                obs.append(value)
            else:
                slow , fast = 0 , len(obs) - 1
                while slow < fast:
                    mid = (slow + fast) // 2
                    if obs[mid] == value:
                        return
                    elif obs[mid] < value:
                        slow  = mid + 1
                    else:
                        fast = mid - 1
                obs = obs[:slow] + [value] + obs[slow:]
    def binary_search(value):
        global obs
        if not obs:
            return None
        else:
            if obs[0] > value:
                return obs[0]
            elif obs[-1] < value:
                return None
            else:
                slow , fast = 0 , len(obs) - 1
                while slow < fast:
                    mid = (slow + fast) // 2
                    if obs[mid] == value:
                        return
                    elif obs[mid] < value:
                        slow  = mid + 1
                    else:
                        fast = mid - 1
                print("slow is ",slow, "fast is ",fast)
                return slow
    for subarray in array:
        if subarray[0] == 1:
            binary_add(subarray[1])
            print("obs is ",obs)
        else:# subarray[1] == 2
            next_index = binary_search(subarray[1])
            if not next_index:
                ret.append(True)
            else:
                if subarray[1] + subarray[2] <= obs[next_index]:
                    ret.append(True)
                else:
                    ret.append(False)
    print("The returned value is ",ret)
    return ret


array = [   [1,0],
            [1,114514],
            [1,3],
            [1,-3],
            [1,1919810],
            [2,-2,2],
            [2,-2,3]]
assert(solution(array) == [True, False])
