
# Contributed by Paraj Shah
# https://github.com/parajshah

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    SUM = []

    for i in range(len(arr) - 2):
        SUM.extend(
            arr[i][j]
            + arr[i][j + 1]
            + arr[i][j + 2]
            + arr[i + 1][j + 1]
            + arr[i + 2][j]
            + arr[i + 2][j + 1]
            + arr[i + 2][j + 2]
            for j in range(len(arr) - 2)
        )
    return max(SUM)
    
    
# Consider 3x3 array
# [i][j]      [i][j + 1]      [i][j + 2]
# [i + 1][j]  [i + 1][j + 1]  [i + 1][j + 2]
# [i + 2][j]  [i + 2][j + 1]  [i + 2][j + 2]

# We consider these indices for the hourglass calculation
# [i][j]      [i][j + 1]      [i][j + 2]
#             [i + 1][j + 1]
# [i + 2][j]  [i + 2][j + 1]  [i + 2][j + 2]

if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        arr = [list(map(int, input().rstrip().split())) for _ in range(6)]
        result = hourglassSum(arr)

        fptr.write(str(result) + '\n')
