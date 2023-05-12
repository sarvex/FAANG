
# Contributed by Paraj Shah
# https://github.com/parajshah

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    leap = False
    if year < 1918 and year % 4 == 0:
        leap = True
    elif year < 1918:
        leap = False
    elif year > 1918:
        if year % 4 == 0:
            leap = True
            if year % 400 == 0:
                leap = True
            elif year % 100 == 0:
                leap = False
    else:
        leap = False

    if (
        not leap
        and year < 1918
        or (not leap or year >= 1918)
        and not leap
        and year > 1918
    ):
        return f"13.09.{year}"
    elif leap and year < 1918 or year != 1918:
        return f"12.09.{year}"
    else:
        return f"26.09.{year}"

if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        year = int(input().strip())

        result = dayOfProgrammer(year)

        fptr.write(result + '\n')
