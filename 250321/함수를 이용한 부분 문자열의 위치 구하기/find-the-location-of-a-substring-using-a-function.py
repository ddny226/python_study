text = input()
pattern = input()

# Please write your code here.
def sub_text():
    for i in range(len(text)):
        if text[i:] == pattern:
            return i 
    return -1 

print(sub_text())