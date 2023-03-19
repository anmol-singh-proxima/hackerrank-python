"""

Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be N x M. (N is an odd natural number, and M is 3 times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.


Sample Input:
9 27


Sample Output:
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------

"""


def design_door_mat(m, n):
    string = "WELCOME"
    a = 1
    
    # Loop for printing first half
    for i in range(m//2):
        str = ""
        for j in range(a):
            str = str + ".|."
        print(str.center(n, "-"))
        a = a + 2

    print(string.center(n, "-"))
    a = a - 2
    
    # Loop for printing second half
    for i in range(m//2):
        str = ""
        for j in range(a):
            str = str + ".|."
        print(str.center(n, "-"))
        a = a - 2
           

if __name__ == '__main__':
    m, n = list(input().split())
    design_door_mat(int(m), int(n))
