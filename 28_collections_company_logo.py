"""


"""


#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    s = input()
    occur_count = dict()
    for i in s:
        occur_count[i] = occur_count.get(i, 0) + 1

    # print(occur_count)
    print(sorted(occur_count.items()))
    occur_count = sorted(occur_count)

    for _ in range(3):
        print(occur_count)
        max_value = -9999999999
        max_key = ""
        for key, value in occur_count.items():
            if value > max_value:
                max_value = occur_count[key]
                max_key = key
        print(max_key, occur_count[max_key])
        occur_count.pop(max_key)
