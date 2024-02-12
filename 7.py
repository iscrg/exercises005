import itertools
numbers = set(map(int, input().split()))
res = list(itertools.permutations(numbers))

for perm in res:
    print(*perm)
