"""

Task:

A valid postal code P have to fullfil both below requirements:
1. P must be a number in the range from 100000 to 999999 inclusive.
2. P must not contain more than one alternating repetitive digit pair.

Alternating repetitive digits are digits which repeat immediately after the next digit. In other words, an alternating repetitive digit pair is formed by two equal digits that have just a single digit between them.

For example:
121426 # Here, 1 is an alternating repetitive digit.
523563 # Here, NO digit is an alternating repetitive digit.
552523 # Here, both 2 and 5 are alternating repetitive digits.

Input Format:
Locked stub code in the editor reads a single string denoting  from stdin and uses provided expression and your regular expressions to validate if  is a valid postal code.

Output Format:
You are not responsible for printing anything to stdout. Locked stub code in the editor does that.

Sample Input:
110000

Sample Output:
False

"""


import re
P = input()

regex_integer_in_range = r"^([1-9]{1})(\d{5})$"
regex_alternating_repetitive_digit_pair = r"(?=(([0-9])[0-9]\2))"
# regex_alternating_repetitive_digit_pair = r'(\d)(?=\d\1)'

print(bool(re.match(regex_integer_in_range, P))
      and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
