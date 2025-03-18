M, D = map(int, input().split())

def is_valid_date(M, D):
    if M in [1, 3, 5, 7, 8, 10, 12]:
        # 해당 월은 31일까지 있음
        return D < 32
    elif M in [4, 6, 9, 11]:
        # 해당 월은 30일까지 있음
        return D < 31
    elif M == 2:
        # 2월은 28일까지(윤년 제외)라고 가정
        return D < 29
    else:
        return False

if is_valid_date(M, D):
    print("Yes")
else:
    print("No")
