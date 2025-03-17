y = int(input())

def yoon_year(y):
    if y % 4 == 0:
        return True
    elif y % 100 == 0 and y % 400 != 0:
        return True
    else:
        return False

print(yoon_year(y))