
# Contributed by Paraj Shah
# https://github.com/parajshah

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    temp = n
    count = 0
    while n > 0:
        d = n % 10
        n //= 10
        if d == 0:
            continue
        if temp % d == 0:
            count += 1        
    return count

if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        t = int(input())

        for _ in range(t):
            n = int(input())

            result = findDigits(n)

            fptr.write(str(result) + '\n')
