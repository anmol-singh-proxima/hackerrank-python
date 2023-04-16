"""

Task:
ABCXYZ company has up to 100 employees.
The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs.

A valid UID must follow the rules below:
1. It must contain at least 2 uppercase English alphabet characters.
2. It must contain at least 3 digits (0-9).
3. It should only contain alphanumeric characters (a-z, A-Z & 0-9).
4. No character should repeat.
5. There must be exactly 10 characters in a valid UID.

Input Format:
The first line contains an integer T, the number of test cases.
The next T lines contains an employee's UID.

Output Format:
For each test case, print 'Valid' if the UID is valid. Otherwise, print 'Invalid', on separate lines. Do not print the quotation marks.

Sample Input:
2
B1CD102354
B1CDEF2354

Sample Output:
Invalid
Valid

Explanation:
B1CD102354:  is repeating → Invalid
B1CDEF2354: Valid


"""

import re

for _ in range(int(input())):
    uid = input()
    v1 = len(re.findall(r"[a-zA-Z]", uid)) >= 2
    v2 = len(re.findall(r"[0-9]", uid)) >= 3
    v3 = not bool(re.search(r"[^a-zA-Z0-9]", uid))
    v4 = len(set(uid)) == 10
    v5 = len(uid) == 10
    print("Valid" if all([v1, v2, v3, v4, v5]) else "Invalid")
