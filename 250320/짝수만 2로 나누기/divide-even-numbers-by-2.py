n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def even(arr):
    for i in range(n):
        if i % 2 == 0:
            if arr[i] == 1:
                continue
            arr[i] = arr[i] // 2 
        else: 
            continue

even(arr)
for elem in arr:
    print(elem, end=" ")
