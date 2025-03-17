y = int(input())

def yoon_year(y):
    if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
        return "true"
    else:
        return "false"

print(yoon_year(y))