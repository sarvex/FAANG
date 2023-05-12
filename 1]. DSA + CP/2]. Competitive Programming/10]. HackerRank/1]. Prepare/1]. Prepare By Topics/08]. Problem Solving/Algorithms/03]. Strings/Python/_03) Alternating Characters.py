
# Contributed by Paraj Shah
# https://github.com/parajshah

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    return sum(
        1
        for i in range(len(s) - 1)
        if (s[i] != 'A' or s[i + 1] != 'B')
        and (s[i] != 'B' or s[i + 1] != 'A')
    )

if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        q = int(input())

        for _ in range(q):
            s = input()

            result = alternatingCharacters(s)

            fptr.write(str(result) + '\n')
