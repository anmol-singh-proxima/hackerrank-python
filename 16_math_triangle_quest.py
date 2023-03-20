"""

Task:
You are given a positive integer N. Print a numerical triangle of height N-1 like the one below:

1
22
333
4444
55555
......

Can you do it using only arithmetic operations, a single for loop and print statement?
Use no more than two lines (The first line is the for-statement)

Sample Input:
5

Sample Output:
1
22
333
4444


"""


for i in range(1, int(input())):
    [print(i, end="") for x in range(i)].append(print())
