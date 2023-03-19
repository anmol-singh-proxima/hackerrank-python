"""

In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

Sample Input:
ABCDCDC
CDC

Sample Output:
2

"""


def count_substring(string, sub_string):
    count = 0
    str_len = len(string)
    sub_str_len = len(sub_string)
    for i in range(str_len - sub_str_len + 1):
        # print(string[i:i+sub_str_len])
        if sub_string in string[i:i+sub_str_len]:
            count = count + 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
