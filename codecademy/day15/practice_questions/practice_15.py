#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n: str, k: int) -> int:
    string_to_validate = n * k

    if len(string_to_validate) == 1:
        return int(string_to_validate)
    else:
        temporal_number = 0
        for number in string_to_validate:
            temporal_number += int(number)
        if temporal_number <= 9:
            return int(temporal_number)
        else:
            return superDigit(str(temporal_number), 1)


if __name__ == '__main__':
    print(superDigit("123", 3))
