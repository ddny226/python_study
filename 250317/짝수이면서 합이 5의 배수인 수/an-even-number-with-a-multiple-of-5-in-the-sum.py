n = int(input())

def is_even_five(n):
    sum = 0
    sum = (n // 10) + (n % 10)
    if n % 2 == 0 and sum % 5 == 0:
        return "Yes"
    else:
        return "No"

print(is_even_five(n))
