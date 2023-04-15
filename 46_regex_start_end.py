"""

Task
You are given a string S.
Your task is to find the indices of the start and end of string K in S.

Input Format:
The first line contains the string S.
The second line contains the string K.

Output Format:
Print the tuple in this format: (start _index, end _index).
If no match is found, print (-1, -1).

Sample Input:
aaadaa
aa

Sample Output:
(0, 1)  
(1, 2)
(4, 5)

"""

import re

def my_code():
    s, k = input(), input()
    m = re.finditer(r'(?=('+k+'))', s)
    print("\n".join(map(str, [(i.start(), i.start()+len(k)-1) for i in m])) or (-1, -1))


def other_code():
    string = input()
    substring = input()

    pattern = re.compile(substring)
    match = pattern.search(string)
    if not match: print('(-1, -1)')
    while match:
        print('({0}, {1})'.format(match.start(), match.end() - 1))
        match = pattern.search(string, match.start() + 1)


if __name__ == "__main__":
    my_code()
    other_code()