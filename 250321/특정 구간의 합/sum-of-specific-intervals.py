n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# 누적합 배열 생성
prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = prefix[i] + arr[i]

def part_sum():
    for start, end in queries:
        print(prefix[end] - prefix[start - 1])

part_sum()
