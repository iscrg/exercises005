slad = set(map(str, input().split()))
n = int(input())
for _ in range(n):
    friend = set(map(str, input().split()))
    slad = slad.difference(friend)
print(len(slad))