# 최소공배수를 구하는 함수 정의
def lcm(n, m):
    return n * m // gcd(n, m)

# 최대공약수를 구하는 함수 정의
def gcd(n, m):
    while m != 0:
        n, m = m, n % m
    return n

# 한 줄로 입력받아 처리
n, m = map(int, input().split())

print(lcm(n, m))