
# Contributed by Paraj Shah
# https://github.com/parajshah

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    # Write your code here
    d = []
    for i in range(len(a)):
        d.extend(abs(i - j) for j in range(i + 1, len(a)) if a[i] == a[j])
    if not d:
        return -1
    d.sort()
    return d[0]                

if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        n = int(input().strip())

        a = list(map(int, input().rstrip().split()))

        result = minimumDistances(a)

        fptr.write(str(result) + '\n')
