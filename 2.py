facults = set()
n = int(input())
for _ in range(n):
    ind_facults = set(map(str, input().split()))
    facults = facults.union(ind_facults)

print(len(facults))
