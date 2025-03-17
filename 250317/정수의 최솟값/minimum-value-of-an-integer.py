a, b, c = map(int, input().split())

def my_min(a, b, c):
    # 첫 번째 값을 최솟값으로 가정
    minimum = a
    # b와 비교
    if b < minimum:
        minimum = b
    # c와 비교
    if c < minimum:
        minimum = c
    return minimum

print(my_min(a, b, c))
