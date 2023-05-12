
# Contributed by Paraj Shah
# https://github.com/parajshah

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'theLoveLetterMystery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def theLoveLetterMystery(s):
    return sum(abs(ord(s[i]) - ord(s[len(s) - i - 1])) for i in range(len(s) // 2))

if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        q = int(input().strip())

        for _ in range(q):
            s = input()

            result = theLoveLetterMystery(s)

            fptr.write(str(result) + '\n')
