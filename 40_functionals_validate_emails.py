"""

Task:

You are given an integer N followed by N email addresses. Your task is to print a list containing only valid email addresses in lexicographical order.
Valid email addresses must follow these rules:
1. It must have the username@websitename.extension format type.
2. The username can only contain letters, digits, dashes and underscores [a-z], [A-Z], [0-9], [_-].
3. The website name can only have letters and digits [a-z], [A-Z], [0-9].
4. The extension can only contain letters [a-z], [A-Z].
5. The maximum length of the extension is 3.

We are using filter() here.

Input Format:
The first line of input is the integer N, the number of email addresses.
N lines follow, each containing a string.

Sample Input:
3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com

Sample Output:
['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']

"""


import re

def fun(s):
    pattern = '^[a-zA-Z0-9_-]+[@]{1}[a-zA-Z0-9]+[.]{1}[a-zA-Z]{1,3}$'
    return re.match(pattern, s)


def long_fun(email):
    try:
        username, url = email.split('@')
        website, extension = url.split('.')
    except ValueError:
        return False
    if username.replace('-', '').replace('_', '').isalnum() is False:
        return False
    elif website.isalnum() is False:
        return False
    elif len(extension) > 3 and len(extension) < 1:
        return False
    else:
        return True


def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
