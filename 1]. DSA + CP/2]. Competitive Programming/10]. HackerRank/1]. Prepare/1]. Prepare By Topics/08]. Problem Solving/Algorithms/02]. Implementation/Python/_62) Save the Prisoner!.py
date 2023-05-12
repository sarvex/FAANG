
# Contributed by Paraj Shah
# https://github.com/parajshah

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    m %= n
    s += m - 2
    return 1 + (s % n)


if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        t = int(input())

        for _ in range(t):
            nms = input().split()

            n = int(nms[0])

            m = int(nms[1])

            s = int(nms[2])

            result = saveThePrisoner(n, m, s)

            fptr.write(str(result) + '\n')
