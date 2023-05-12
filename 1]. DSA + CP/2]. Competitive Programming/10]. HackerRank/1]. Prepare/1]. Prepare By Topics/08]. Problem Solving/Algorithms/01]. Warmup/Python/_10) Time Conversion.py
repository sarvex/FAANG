
# Contributed by Paraj Shah
# https://github.com/parajshah

#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    if s[-2:].upper() == "AM":
        if s[:2] == '12':
            s = f'00{s[2:]}'
        time = s[:-2]
    if s[-2:].upper() == "PM":
        time = int(s[:2]) + 12 if s[:2] != '12' else int(s[:2])
        time = str(time) + s[2:-2]
    return time

if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as f:
        s = input()

        result = timeConversion(s)

        f.write(result + '\n')
