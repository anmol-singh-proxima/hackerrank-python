"""

Task:
You are given a date. Your task is to find what the day is on that date.

Input Format:
A single line of input containing the space separated month, day and year, respectively, in MM DD YYYY format.

Output Format:
Output the correct day in capital letters.

Sample Input:
08 05 2015

Sample Output:
WEDNESDAY

"""

import calendar


def my_code():
    cal = calendar.Calendar(firstweekday=0)

    month, day, year = list(map(int, input().split()))
    days = ['monday', 'tuesday', 'wednesday',
            'thursday', 'friday', 'saturday', 'sunday']

    for i in cal.itermonthdays2(year, month):
        if i[0] == day and i[1] >= 0 and i[1] <= 6:
            print(days[i[1]].upper())


def short_code():
    m, d, y = map(int, input().strip().split())
    print(calendar.day_name[calendar.weekday(y, m, d)].upper())


if __name__ == "__main__":
    my_code()
    short_code()
