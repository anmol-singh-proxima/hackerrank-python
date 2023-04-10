"""

Task:
You are given a string S.
Your task is to find out whether S is a valid regex or not.

Input Format:
The first line contains integer T, the number of test cases.
The next T lines contains the string S.

Output Format:
Print "True" or "False" for each test case without quotes.

Sample Input:
2
.*\+
.*+

Sample Output:
True
False

Explanation:
.*\+ : Valid regex.
.*+: Has the error multiple repeat. Hence, it is invalid.

"""

import re
for _ in range(int(input())):
    try:
        re.compile(input())
        print("True")
    except:
        print("False")
