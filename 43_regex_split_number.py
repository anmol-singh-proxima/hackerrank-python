"""
Task:
You are given a string S consisting only of digits[0-9], commas[,] and dots[.].

Your task is to complete the regex_pattern defined below, which will be used to re.split() all of the , and . symbols in S.

It's guaranteed that every comma and every dot in S is preceeded and followed by a digit.

Sample Input:
100,000,000.000

Sample Output:
100
000
000
000

"""

import re
regex_pattern = r"[,]|[.]"
print("\n".join(re.split(regex_pattern, input())))
