a, b = map(int, input().split())

def cond1(num):
    num_str = str(num)
    for digit in num_str:
        if digit in '369':
            return True
    return False

def cond2(num):
    return num % 3 == 0

cnt = 0
for i in range(a, b+1):
    if cond1(i) or cond2(i):
        cnt += 1

print(cnt)
