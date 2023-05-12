
# Contributed by Paraj Shah
# https://github.com/parajshah

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hurdleRace function below.
def hurdleRace(k, height):
    max_height = max(height)
    potions = max_height - k
    return max(potions, 0)


if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        height = list(map(int, input().rstrip().split()))

        result = hurdleRace(k, height)

        fptr.write(str(result) + '\n')
