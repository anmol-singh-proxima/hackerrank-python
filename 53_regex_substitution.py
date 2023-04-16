"""

The re.sub() tool (sub stands for substitution) evaluates a pattern and, for each valid match, it calls a method (or lambda).
The method is called for all matches and can be used to modify strings in different ways.
The re.sub() method returns the modified string as an output.

Transformation of Strings (Example)

Code:
import re
#Squaring numbers
def square(match):
    number = int(match.group(0))
    return str(number**2)
print re.sub(r"\d+", square, "1 2 3 4 5 6 7 8 9")

Output:
1 4 9 16 25 36 49 64 81


Task:
You are given a text of N lines. The text contains && and || symbols.
Your task is to modify those symbols to the following:
&& → and
|| → or
Both && and || should have a space " " on both sides.

Input Format:
The first line contains the integer, N.
The next N lines each contain a line of the text.

Output Format:
Output the modified text.

Sample Input:
11
a = 1;
b = input();

if a + b > 0 && a - b < 0:
    start()
elif a*b > 10 || a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.

Sample Output:
a = 1;
b = input();

if a + b > 0 and a - b < 0:
    start()
elif a*b > 10 or a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.    

"""

import re


def my_code():
    and_pattern = r"(?<=[ ])([&]{2})(?=[ ])"
    or_pattern = r"(?<=[ ])([|]{2})(?=[ ])"

    for _ in range(int(input())):
        string = input()
        string = re.sub(and_pattern, "and", string)
        string = re.sub(or_pattern, "or", string)
        print(string)


def short_code():
    for _ in range(int(input())):
        print(re.sub(r'(?<= )(&&|\|\|)(?= )',
              lambda x: 'and' if x.group() == '&&' else 'or', input()))


if __name__ == "__main__":
    my_code()
