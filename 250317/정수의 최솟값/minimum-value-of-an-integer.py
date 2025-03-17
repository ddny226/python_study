a, b, c = map(int, input().split())

def min(a, b, c):
    if a > b:
        if b > c:
            return c
        else:
            return b
    else: return a

print(min(a,b,c))