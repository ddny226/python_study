def ones_rect(n, m):
    for _ in range(n):
        print("1" * m)

row, col = tuple(map(int, input().split()))
ones_rect(row, col)