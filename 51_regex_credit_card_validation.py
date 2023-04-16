"""

Task:
You and Fredrick are good friends. Yesterday, Fredrick received N credit cards from ABCD Bank. He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!

A valid credit card from ABCD Bank has the following characteristics:
► It must start with a 4, 5 or 6.
► It must contain exactly 16 digits.
► It must only consist of digits (0-9).
► It may have digits in groups of 4, separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have 4 or more consecutive repeated digits.

Input Format:
The first line of input contains an integer N.
The next N lines contain credit card numbers.

Output Format:
Print 'Valid' if the credit card number is valid. Otherwise, print 'Invalid'. Do not print the quotes.

Sample Input:
6
4123456789123456
5123-4567-8912-3456
61234-567-8912-3456
4123356789123456
5133-3367-8912-3456
5123 - 3567 - 8912 - 3456

Sample Output:
Valid
Valid
Invalid
Valid
Invalid
Invalid

"""


import re


def my_code():
    for _ in range(int(input())):
        card_num = input()

        # To check if card number starts with 4,5 or 6
        v1 = bool(re.search(r"^[456]", card_num))

        # To check if the card number does not contain any character other than the digits and hyphen
        v2 = not bool(re.search("[^0-9-]", card_num))

        # Take out the digits from card number for further validation
        card_digits = "".join(re.findall(r'\d', card_num))

        # To check if the count of digits in card number is 16
        v3 = len(card_digits) == 16

        # To check if card does not have 4 or more consecutive repeated digits
        v4 = not bool(re.search(r"(\d)\1\1\1", card_digits))

        # If any of the above condition is false then it is Invalid
        if not all([v1, v2, v3, v4]):
            print("Invalid")

        # To check if all the above condition are True and card number does not contain any hyphen then it is Valid
        elif not bool(re.search(r"-", card_num)):
            print("Valid")

        # If all above conditions are True and card number contains hyphen then the number must be split with hyphen in 4 equal length substring
        else:
            card_split = all([len(num) == 4 for num in card_num.split("-")])
            print("Valid") if len(re.findall(r"-", card_num)
                                  ) == 3 and card_split else print("Invalid")


def short_code1():
    pattern = re.compile(
        r'^'
        r'(?!.*(\d)(-?\1){3})'
        r'[456]\d{3}'
        r'(?:-?\d{4}){3}'
        r'$')
    for _ in range(int(input().strip())):
        print('Valid' if pattern.search(input().strip()) else 'Invalid')


def short_code2():
    for _ in range(int(input())):
        cc = input()
        if re.search(r"^([456]\d{3})([ -]?\d{4}){3}$", cc):
            # remove non digits
            cc = re.sub(r"[^\d]", "", cc)
            print('Valid' if not re.search(r'(\d)\1{3}', cc) else 'Invalid')
        else:
            print('Invalid')


if __name__ == "__main__":
    my_code()
