for i in range(100, 1000):
    num = set(str(i))
    res_num = i * 3
    res_set = set(str(i * 3))
    res = num.union(res_set)
    if len(res) == 6:
        print(f"{i} + {i} + {i} = {res_num}")
    elif res_num > 999:
        break
