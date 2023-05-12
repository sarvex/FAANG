
# Contributed by Paraj Shah
# https://github.com/parajshah

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    emergencyString = (len(s) // 3) * 'SOS'
    return sum(1 for i in range(len(s)) if s[i] != emergencyString[i])
    

if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        s = input()

        result = marsExploration(s)

        fptr.write(str(result) + '\n')
