"""

Task:
When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to view this new post on their news feed. Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.

Since sometimes posts are published and viewed in different time zones, this can be confusing. You are given two timestamps of one such post that a user can see on his newsfeed in the following format:
Day dd Mon yyyy hh:mm:ss +xxxx

Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.

Input Format:
The first line contains T, the number of testcases.
Each testcase contains 2 lines, representing time t1 and time t2.

Output Format:
Print the absolute difference (t1 - t2) in seconds.

Sample Input:
2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000

Sample Output:
25200
88200

"""


import os
from datetime import datetime, date


def time_delta_my_code(t1, t2):
    """
    This function does the work without using much of the datetime module, but it's not giving proper result now.
    """
    t1_list = t1.split()
    t2_list = t2.split()

    # Get year, month and day of both the times
    t1_month = datetime.strptime(t1_list[2][:3], '%b').month
    t2_month = datetime.strptime(t2_list[2][:3], '%b').month
    t1_year = int(t1_list[3])
    t2_year = int(t2_list[3])
    t1_day = int(t1_list[1])
    t1_day = int(t2_list[1])

    # Calculate the difference in number of days between both the times
    d1 = date(2021, 10, 20)
    d2 = date(2021, 2, 20)
    day_diff = abs(d2-d1).days * 24 * 60 * 60
    # print(day_diff)

    # Calculate the time difference between both the times
    t1_hr, t1_min, t1_sec = list(map(int, t1_list[4].split(':')))
    t2_hr, t2_min, t2_sec = list(map(int, t2_list[4].split(':')))
    hr_diff = t1_hr - t2_hr
    min_diff = t1_min - t2_min
    sec_diff = t1_sec - t2_sec
    time_diff = (hr_diff*60 + min_diff)*60 + sec_diff
    # print(time_diff)

    # Calculate the difference in the timezone of both the times
    t1_timezone = t1_list[5][0]
    t2_timezone = t2_list[5][0]
    t1_timezone_hrs = int(t1_list[5][1:3])
    t2_timezone_hrs = int(t2_list[5][1:3])
    t1_timezone_min = int(t1_list[5][3:])
    t2_timezone_min = int(t2_list[5][3:])
    timezone_hrs_diff = 0
    timezone_min_diff = 0
    if t1_timezone == t2_timezone:
        timezone_hrs_diff = abs(t1_timezone_hrs - t2_timezone_hrs)
        timezone_min_diff = abs(t1_timezone_min - t2_timezone_min)
    elif t1_timezone != t2_timezone:
        timezone_hrs_diff = abs(t1_timezone_hrs + t2_timezone_hrs)
        timezone_min_diff = abs(t1_timezone_min + t2_timezone_min)
    timezone_diff = (timezone_hrs_diff*60 + timezone_min_diff)*60

    # Calculate the total time difference in seconds and return it
    if t1_timezone == '+':
        return day_diff + time_diff - timezone_diff
    elif t1_timezone == '-':
        return day_diff + time_diff + timezone_diff


def time_delta_short_code():
    time_format = "%a %d %b %Y %H:%M:%S %z"
    d1 = datetime.strptime(t1, time_format)
    d2 = datetime.strptime(t2, time_format)
    time_diff = round(abs(d1 - d2).total_seconds())
    return time_diff


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta_short_code(t1, t2)
        fptr.write(str(delta) + '\n')
    fptr.close()
