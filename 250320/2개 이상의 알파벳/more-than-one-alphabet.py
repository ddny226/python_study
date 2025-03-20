A = input()

cnt = [0] * 26

for char in A:
    cnt[ord(char) - 97] += 1

distinct_count = sum(1 for count in cnt if count > 0)

if distinct_count >= 2:
    print("Yes")
else:
    print("No")
