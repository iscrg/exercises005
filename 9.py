nums = set(map(str, input().split()))
n = int(input())
res = []

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        res_set = {list(nums)[k] for k in range(i, j+1)}
        if len(res_set) == n:
            res.append(res_set)

print(res)
