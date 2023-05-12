
# Contributed by Paraj Shah
# https://github.com/parajshah

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    shares = 5
    likes = math.floor(shares / 2)
    total = likes
    for _ in range(n - 1):
        shares = likes * 3
        likes = math.floor(shares / 2)
        total += likes
    return total

if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        n = int(input())

        result = viralAdvertising(n)

        fptr.write(str(result) + '\n')
