a, b= map(int, input().split())

def num(a, b):
    cnt = 0
    for i in range(a, b+1):
        if (i % 2 == 0) or (i % 10 == 5) or (i % 3 == 0 and i % 9 != 0):
            continue
        cnt += 1
    return cnt 

print(num(a,b))







