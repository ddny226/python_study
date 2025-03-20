n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def abbs(arr):
    for i in range(n):
        arr[i] = abs(arr[i])
        print(arr[i], end=" ")

abbs(arr)