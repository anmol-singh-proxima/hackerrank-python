"""



"""


import re

def my_code():
    pattern = '#[0-9abcdef]{3,6}'
    braces_flag = False
    for _ in range(int(input())):
        string = input()
        print(string)
        if re.match("}", string):
            braces_flag = False
        if braces_flag:
            matches = re.findall(pattern, string, flags=re.I)
            print(matches)
            # print("\n".join(matches or ""))
        if re.match("{", string):
            braces_flag = True


def other_code():
    for _ in range(int(input())):
        matches = re.findall(r':?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})', input())
        if matches:
            print(*matches, sep='\n')


if __name__ == "__main__":
    my_code()
    other_code()