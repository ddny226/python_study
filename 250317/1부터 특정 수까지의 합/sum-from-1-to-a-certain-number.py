n = int(input())

def sum_N(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum

print(sum_N(n)//10)
