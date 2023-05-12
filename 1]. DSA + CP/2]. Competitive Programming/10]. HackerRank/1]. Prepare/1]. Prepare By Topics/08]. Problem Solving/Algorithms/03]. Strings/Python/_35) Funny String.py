
# Contributed by Paraj Shah
# https://github.com/parajshah

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    asciiValues = [ord(i) for i in s]
    asciiValuesReverse = [
        asciiValues[len(asciiValues) - i - 1] for i in range(len(asciiValues))
    ]
    return next(
        (
            "Not Funny"
            for i in range(len(s) - 1)
            if abs(asciiValues[i + 1] - asciiValues[i])
            != abs(asciiValuesReverse[i + 1] - asciiValuesReverse[i])
        ),
        "Funny",
    )

if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        q = int(input().strip())

        for _ in range(q):
            s = input()

            result = funnyString(s)

            fptr.write(result + '\n')
