
# Contributed by Paraj Shah
# https://github.com/parajshah

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    return sum(abs(not (x - int(str(x)[::-1]))%k) for x in range(i, j+1))

if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        ijk = input().split()

        i = int(ijk[0])

        j = int(ijk[1])

        k = int(ijk[2])

        result = beautifulDays(i, j, k)

        fptr.write(str(result) + '\n')
