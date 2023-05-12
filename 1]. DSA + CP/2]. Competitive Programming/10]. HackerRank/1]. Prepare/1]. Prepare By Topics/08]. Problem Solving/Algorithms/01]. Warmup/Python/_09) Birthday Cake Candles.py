
# Contributed by Paraj Shah
# https://github.com/parajshah

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    m = max(ar)
    return sum(1 for i in range(len(ar)) if ar[i] == m)

if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        ar_count = int(input())

        ar = list(map(int, input().rstrip().split()))

        result = birthdayCakeCandles(ar)

        fptr.write(str(result) + '\n')
