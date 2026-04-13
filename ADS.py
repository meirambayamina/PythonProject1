#Task 1. Print numbers from 1 to n
def print_1_to_n(n):
    if n <= 0: return
    print_1_to_n(n - 1)
    print(n, end=" ")
print_1_to_n(5)

print("\n")

# time complexity: O(n)
# space complexity: O(n)

#Task 2. Print numbers from n to 1

def print_n_to_1(n):
    if n <= 0: return
    print(n, end=" ")
    print_n_to_1(n - 1)
print_n_to_1(5)

# time complexity: O(n)
# space complexity: O(n)

#Task 3. Find the sum of the first n natural numbers

def sum_natural(n):
    if n <= 1: return n
    return n + sum_natural(n - 1)
print(sum_natural(5))

# time complexity: O(n)
# space complexity: O(n)

# Task 4. Find the factorial of a number

def factorial(n):
    if n == 0 or n == 1: return 1
    return n * factorial(n - 1)
print(factorial(5))

# time complexity: O(n)
# space complexity: O(n)

# Task 5. Compute a power of a number

def power(a, b):
    if b == 0: return 1
    return a * power(a, b - 1)

print(power(2, 4))

# time complexity: O(b)
# space complexity: O(b)

# Task 6. Find the sum of digits

def sum_digits(n):
    if n == 0: return 0
    return (n % 10) + sum_digits(n // 10)

print(sum_digits(572))

# time complexity: O(log10n)
# space complexity: O(log10n)

# Task 7. Count the number of digits

def count_digits(n):
    if n < 10: return 1
    return 1 + count_digits(n // 10)

print(count_digits(5729))

# time complexity: O(log10n)
# space complexity: O(log10n)

# Task 8. Reverse a number

def reverse_num(n):
    if n < 10:
        print(n, end="")
        return
    print(n % 10, end="")
    reverse_num(n // 10)

reverse_num(1234)
print()

# Task 9. Find the nth Fibonacci number

def fibonacci(n):
    if n <= 1: return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))

# Task 10. Check palindrome

def is_palindrome(s):
    if len(s) <= 1: return "Palindrome"
    if s[0] != s[-1]: return "Not palindrome"
    return is_palindrome(s[1:-1])

print(is_palindrome("level"))
print(is_palindrome("hello"))

# Task 11. Sum of elements in an array

def sum_array(arr):
    if not arr: return 0
    return arr[0] + sum_array(arr[1:])

print(sum_array([3, 5, 2, 7]))

# Task 12. Maximum element in an array

def find_max(arr):
    if len(arr) == 1: return arr[0]
    return max(arr[0], find_max(arr[1:]))

print(find_max([4, 9, 1, 7, 3]))

# Task 13. Count occurrences

def count_target(arr, target):
    if not arr: return 0
    return (1 if arr[0] == target else 0) + count_target(arr[1:], target)

print(count_target([1, 2, 3, 2, 2, 5], 2))

# Task 14. Recursive linear search

def linear_search(arr, target):
    if not arr: return "Not found"
    if arr[0] == target: return "Found"
    return linear_search(arr[1:], target)

print(linear_search([4, 7, 1, 9, 3], 9))

# Task 15. Check if sorted

def is_sorted(arr):
    if len(arr) <= 1: return "Sorted"
    if arr[0] > arr[1]: return "Not sorted"
    return is_sorted(arr[1:])

print(is_sorted([1, 2, 4, 7, 9]))
print(is_sorted([1, 5, 3, 8]))

# Task 16. Recursive binary search

def binary_search(arr, target, low, high):
    if low > high: return "Not found"
    mid = (low + high) // 2
    if arr[mid] == target: return f"Element found at index {mid}"
    if arr[mid] > target: return binary_search(arr, target, low, mid - 1)
    return binary_search(arr, target, mid + 1, high)
arr_bin = [1, 3, 5, 7, 9, 11]
print(binary_search(arr_bin, 7, 0, len(arr_bin) - 1))

