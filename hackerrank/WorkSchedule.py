

def WorkSchedule(work_hours:int, day_hours:int,pattern:str ):
    worklist = list()
    for index, char in enumerate(pattern):
        if char == '?':
            worklist.append(index)
        else:
            hour = int(char)
            work_hours -= hour
    ret = list()
    # print(worklist)
    # pattern: ??2??00
    stack = list()
    def backtrack(remain_hour, pos:int):
        nonlocal worklist
        if pos > len(worklist):
            return
        remain_day = len(worklist) - pos
        if pos == len(worklist) and remain_hour == 0:
            ret.append(stack[:])
        if remain_day <= 0 or remain_hour / remain_day > day_hours:
            return
        
        for hour in range(0, day_hours + 1):
            stack.append(hour)
            backtrack(remain_hour - hour, pos + 1)
            stack.pop()
    backtrack(work_hours, 0)
    # print(ret)
    pattern_list = list(pattern)
    # print("pattern list is ",pattern_list)
    res = list()
    for result in ret:
        count = 0
        for workday in worklist:
            pattern_list[workday] = str(result[count])
            count += 1
        # print("pattern list is ",pattern_list)
        res.append(''.join(pattern_list))
    print(res)
    return res


WorkSchedule(3,2,'??2??00')
WorkSchedule(work_hours = 56,
day_hours = 8,
pattern = '???8???'
)
WorkSchedule(work_hours = 24,
day_hours = 4,
pattern = '08??840'
    
)