
# Contributed by Paraj Shah
# https://github.com/parajshah

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr,n):
    # Write your code here
    d1 = 0
    d2 = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                d1 += arr[i][j]

            if i == n - j - 1:
                d2 += arr[i][j]
    return abs(d1 - d2)
    

if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        n = int(input().strip())

        arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
        result = diagonalDifference(arr,n)

        fptr.write(str(result) + '\n')
