
# Contributed by Paraj Shah
# https://github.com/parajshah

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quickSort(arr):
    p = arr[0]
    left = [arr[i] for i in range(len(arr)) if arr[i] < p]
    equal = [arr[i] for i in range(len(arr)) if arr[i] == p]
    right = [arr[i] for i in range(len(arr)) if arr[i] > p]

    return left + equal + right
    

if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = quickSort(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')
