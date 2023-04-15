"""

Task:
You are given a string S.
S contains alphanumeric characters only.
Your task is to sort the string S in the following manner:
- All sorted lowercase letters are ahead of uppercase letters.
- All sorted uppercase letters are ahead of digits.
- All sorted odd digits are ahead of sorted even digits.

Input Format:
A single line of input contains the string S.

Output Format:
Output the sorted string S.

Sample Input:
Sorting1234

Sample Output:
ginortS1324

"""


def my_code():
    string = sorted(input())
    lower = ""
    upper = ""
    odd = ""
    even = ""
    for i in string:
        if i.islower():
            lower = lower + i
        elif i.isupper():
            upper = upper + i
        elif i.isdigit() and i in '02468':
            even = even + i
        elif i.isdigit() and i in '13579':
            odd = odd + i
    print(lower+upper+odd+even)


def short_code():
    print(*sorted(input(), key=lambda c: (c.isdigit() -
          c.islower(), c in '02468', c)), sep='')


def short_code_described():
    sorted_tuple_list = sorted(
        [(c.isdigit() - c.islower(), c in '02468', c) for c in input()])
    sorted_list = [item[2] for item in sorted_tuple_list]
    print("".join(sorted_list))


if __name__ == "__main__":
    my_code()
    short_code()
    short_code_described()
