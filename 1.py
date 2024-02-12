# А вообще задание решения не имеет, так как "множества повторяющихся чисел" в Python быть не может согласно определению множеств.
nums = set(map(int, input().split()))
current_num = int(input())
if current_num in nums:
    print('y')
else:
    print('n')
