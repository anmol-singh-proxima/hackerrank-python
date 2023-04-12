"""

Task:
You are given a string N.
Your task is to verify that N is a floating point number.

In this task, a valid float number must satisfy all of the following requirements:

1. Number can start with +, - or . symbol.
For example:
✔ +4.50
✔ -1.0
✔ .5
✔ -.7
✔ +.4
✖ -+4.5

2. Number must contain at least 1 decimal value.
For example:
✖ 12.
✔ 12.0  

3. Number must have exactly one . symbol.
4. Number must not give any exceptions when converted using float(N).

Input Format:
The first line contains an integer T, the number of test cases.
The next T line(s) contains a string N.

Output Format:
Output True or False for each test case.

Sample Input:
4
4.0O0
-1.00
+4.54
SomeRandomStuff

Sample Output:
False
True
True
False

Explanation:
: O is not a digit.
: is valid.
: is valid.
SomeRandomStuff: is not a number.

"""


import re
pattern = "^[+-]?[0-9]*[.]{1}[0-9]+$"
for _ in range(int(input())):
    num = input()
    print("True" if re.match(pattern, num) else "False")
