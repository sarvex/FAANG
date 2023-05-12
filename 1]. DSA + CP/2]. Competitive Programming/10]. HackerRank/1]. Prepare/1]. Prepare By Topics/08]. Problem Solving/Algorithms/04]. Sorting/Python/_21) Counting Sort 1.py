
# Contributed by Paraj Shah
# https://github.com/parajshah

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    counts = [0] * 100
    for i in arr:
        counts[i] += 1
    return counts

if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = countingSort(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')
