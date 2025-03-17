a, b, c = map(int, input().split())

def min(a, b, c):
    if a > b:
        if b > c:
            return c
        else:
            return b
    elif b > c:
        if c > a:
            return a
        else: return c
    elif c > a:
        if b > a:
            return a
        else:
            return b
    

print(min(a,b,c))