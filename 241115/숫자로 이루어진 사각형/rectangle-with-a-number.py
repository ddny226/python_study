def num_rect(n):
    num = 1
    for _ in range(n):
        for _ in range(n):
            print(num, end=" ")
            num+=1
            if num > 9 :
                num = 1
        print()

num = int(input())
num_rect(num)