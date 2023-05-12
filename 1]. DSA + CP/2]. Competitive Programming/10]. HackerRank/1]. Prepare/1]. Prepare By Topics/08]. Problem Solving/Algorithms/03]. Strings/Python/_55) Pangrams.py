
# Contributed by Paraj Shah
# https://github.com/parajshah

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    alphabets = [0] * 26
    for i in s:
        if i.isalpha():
            index = ord(i.lower()) - ord('a')
            alphabets[index] += 1

    return next(("not pangram" for i in alphabets if i == 0), "pangram")

if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        s = input()

        result = pangrams(s)

        fptr.write(result + '\n')
