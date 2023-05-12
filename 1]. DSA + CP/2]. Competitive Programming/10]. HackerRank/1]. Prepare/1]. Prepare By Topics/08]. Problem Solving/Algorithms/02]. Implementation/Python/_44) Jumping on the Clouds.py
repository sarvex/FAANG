
# Contributed by Paraj Shah
# https://github.com/parajshah

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    ans = 0
    i = 0
    while i < n - 1:
        i += 1 if i + 2 >= n or c[i + 2] == 1 else 2
        ans = ans + 1
    return ans

if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        n = int(input())

        c = list(map(int, input().rstrip().split()))

        result = jumpingOnClouds(c)

        fptr.write(str(result) + '\n')
