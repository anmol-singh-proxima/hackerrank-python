"""

Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.


Input:

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39


Ouput:

Berry
Harry

"""


if __name__ == '__main__':
    ns_list = []
    lowest = 9999
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if lowest > score:
            lowest = score
        ns_list.append([name, score])

    n = len(ns_list)
    # print(ns_list)

    sec_lowest = 9999
    for i in ns_list:
        if i[1] != lowest and i[1] < sec_lowest:
            sec_lowest = i[1]

    # print(sec_lowest)

    lowest_score_names = []
    for i in ns_list:
        if i[1] == sec_lowest:
            lowest_score_names.append(i[0])

    lowest_score_names.sort()
    for i in lowest_score_names:
        print(i)
