"""

Task:
You are given a positive integer N.
Your task is to print a palindromic triangle of size N.

For example, a palindromic triangle of size 5 is:

1
121
12321
1234321
123454321

Note:
You can't take more than two lines (The first line is a for-statement)
You have to complete the code using exactly one print() statement.
You can't use str() or string

Sample Input:
5

Sample Output:
1
121
12321
1234321
123454321


"""


for i in range(1,int(input())+1):
    # print(*range(1,i+1), *range(i-1, 0, -1))
    # print(''.join(str(x) for x in range(1,i)) + ''.join(str(x) for x in range(i,0,-1)))
    # [print(x, end="") for x in range(1,i)].append([print(x, end="") for x in range(i,0,-1)].append(print()))
    pass