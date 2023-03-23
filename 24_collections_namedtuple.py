"""

Task:
Dr. John Wesley has a spreadsheet containing a list of student's IDs, MARKS, CLASS and NAME.
Your task is to help Dr. Wesley calculate the average marks of the students.

Input Format:
The first line contains an integer N, the total number of students.
The second line contains the names of the columns in any order.
The next N lines contains the IDs, MARKS, CLASS and NAME, under their respective column names.

Output Format:
Print the average marks of the list corrected to 2 decimal places.

Sample Input:

TESTCASE 01:
5
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6   

TESTCASE 02:
5
MARKS      CLASS      NAME       ID        
92         2          Calum      1         
82         5          Scott      2         
94         2          Jason      3         
55         8          Glenn      4         
82         2          Fergus     5

Sample Output:

TESTCASE 01
78.00

TESTCASE 02
81.00

"""


from collections import namedtuple

def four_lines_code():
    n = int(input())
    Student = namedtuple('Student', input().split())
    print(sum([int(Student(*(input().split())).MARKS) for _ in range(n)])/n)


def long_explanatory_code():
    n = int(input())
    columns = input().split()
    Student = namedtuple('Student', columns)
    marks = []
    for _ in range(n):
        marks.append(int(Student(*(input().split())).MARKS))
    total = sum(marks)
    average = total/n
    print(average)


def solve_without_namedtuple():
    n = int(input())
    columns = list(input().split())
    marks_pos = -1
    for i in range(len(columns)):
        if columns[i] == "MARKS":
            marks_pos = i
            break
    total_marks = 0
    for i in range(n):
        details = input().split()
        total_marks = total_marks + int(details[marks_pos])
    average = total_marks/n
    print(average)


if __name__ == "__main__":
    four_lines_code()