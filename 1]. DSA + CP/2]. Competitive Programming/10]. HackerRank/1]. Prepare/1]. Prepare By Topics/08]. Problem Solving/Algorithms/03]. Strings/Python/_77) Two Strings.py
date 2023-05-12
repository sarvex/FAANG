
# Contributed by Paraj Shah
# https://github.com/parajshah

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    return "YES" if set(s1) & set(s2) else "NO"

if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        q = int(input())

        for _ in range(q):
            s1 = input()

            s2 = input()

            result = twoStrings(s1, s2)

            fptr.write(result + '\n')
