a, b = map(int, input().split())

# Please write your code here.
def magic(a, b):
    if a > b:
        a += 25 ; b *= 2
    else:
        a *=2 ; b += 25
    print(a, b)

magic(a,b)