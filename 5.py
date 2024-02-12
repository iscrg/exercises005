n = 30
nums = set(range(2, n + 1))
res = set()

while nums:
    p = min(nums)
    res.add(p)

    mltp = set(range(p, n + 1, p))
    nums -= mltp

print(res)
