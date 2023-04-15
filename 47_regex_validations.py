"""

Task:
Validate phone number
Phone number starts from 7,8 or 9
There are total 10 digits

Sample Input:
2
9587456281
1252478965

Sample Output:
YES
NO

"""

import email.utils
import re

phone_pattern = "^[789]\d{9}$"
[print("YES" if re.match(phone_pattern, input()) else "NO")
 for _ in range(int(input()))]


"""

A valid email address meets the following criteria:
1. It's composed of a username, domain name, and extension assembled in this format: username@domain.extension
2. The username starts with an English alphabetical character, and any subsequent characters consist of one or more of the following: alphanumeric characters [-] [.] [_]
3. The domain and extension contain only English alphabetical characters.
4. The extension is 1-3 characters in length.

Sample Input:
2  
DEXTER <dexter@hotmail.com>
VIRUS <virus!@variable.:p>

Sample Output:
DEXTER <dexter@hotmail.com>

"""


email_pattern = "^[a-zA-Z](\w|-|_|\.)+@[a-zA-Z]+\.[a-zA-Z]{1,3}$"


def my_code_short():
    for _ in range(int(input())):
        name, email = input().split()
        print(name, email) if re.match(email_pattern, email[1:-1]) else ""


def my_code_using_email_utils():
    for _ in range(int(input())):
        name, email_id = email.utils.parseaddr(input())
        print(name, email_id) if re.match(email_pattern, email_id) else ""


my_code_short()
