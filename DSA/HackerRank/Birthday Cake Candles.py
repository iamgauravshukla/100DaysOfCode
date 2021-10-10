"""You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for each year of their total age. They will only be able to blow out the tallest of the candles. Count how many candles are tallest.

Example
arr = [4, 4, 1, 3]

The maximum height candles are 4 units high. There are 2 of them, so return 2.
"""

import math
import os
import random
import re
import sys


def birthdayCakeCandles(candles):
    tallest = max(candles)
    count = 0
    for i in candles:
        if i == tallest:
            count += 1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()