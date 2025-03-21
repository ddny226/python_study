n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
def whole_sum(n, m, A):
    sum = 0
    while m >= 1:
        if m % 2 == 0:
            sum += A[m-1]
            m = m // 2
        else:
            sum += A[m-1]
            m = m -1
    return sum

print(whole_sum(n, m, A))
