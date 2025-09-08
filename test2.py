#even and odd numbers
def even_odd_numbers(n):
    even_numbers = [x for x in range(n) if x % 2 == 0]
    odd_numbers = [x for x in range(n) if x % 2 !=0]
    return even_numbers, odd_numbers

print(even_odd_numbers(10))

# Output: ([0, 2, 4, 6, 8], [1, 3, 5, 7, 9])s