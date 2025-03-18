a, o, c = input().split()
a = int(a)
c = int(c)

def cal(a, o, c):
    if o == '+':
        result = a+c
    elif o == '-':
        result = a-c
    elif o == '/':
        result = a//c
    elif o == '*':
        result = a*c
    else:
        print(False)
        return
    print(f"{a} {o} {c} = {result}")

cal(a,o,c)



