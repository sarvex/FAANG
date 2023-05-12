
# Contributed by Paraj Shah
# https://github.com/parajshah

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong

    count = 0
    if not any(i.isdigit() for i in password):
        count += 1
    if not any(i.isupper() for i in password):
        count += 1
    if not any(i.islower() for i in password):
        count += 1
    if all(i not in "!@#$%^&*()-+" for i in password):
        count += 1
    return max(count,6 - n)


if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        n = int(input())

        password = input()

        answer = minimumNumber(n, password)

        fptr.write(str(answer) + '\n')
