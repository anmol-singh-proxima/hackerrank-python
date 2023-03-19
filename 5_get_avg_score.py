"""

The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.


Input:

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika


Output:

56.00

"""


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    for name in student_marks:
        if name == query_name:
            m = len(student_marks[name])
            avg = 0.0
            sum = 0.0
            for marks in student_marks[name]:
                sum = sum + marks
            avg = sum/m
            print("%.2f" % avg)
        # print(name, student_marks[i])


