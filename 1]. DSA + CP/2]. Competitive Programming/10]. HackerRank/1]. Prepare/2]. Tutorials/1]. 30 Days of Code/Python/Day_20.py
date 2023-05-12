# 21st Solution
#---------------------------------------------------------------

#!/bin/python3
import sys
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
swaps = 0
is_sorted = False

while not is_sorted:
    is_sorted = True
    for i in range(0, len(a)):
        if i < len(a) - 1 and a[i] > a[i + 1]:
            a[i], a[i+1] = a[i+1], a[i]
            is_sorted = False
            swaps += 1

print(f"Array is sorted in {swaps} swaps.")
print(f"First Element: {a[0]}")
print(f"Last Element: {a[-1]}")

