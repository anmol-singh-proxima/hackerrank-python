"""

Task:
There is a horizontal row of N cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if cube[i] is on top of cube[j] then sideLength[j] >= sideLength[i].
When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print Yes if it is possible to stack the cubes. Otherwise, print No.

Example 1:
blocks = [1,2,3,8,7]
Result: No
After choosing the rightmost element, 7, choose the leftmost element, 1. After than, the choices are 2 and 8. These are both larger than the top block of size 1.

Example 2:
blocks = [1,2,3,7,8]
Result: Yes
Choose blocks from right to left in order to successfully stack the blocks.

Input Format:
The first line contains a single integer T, the number of test cases.
For each test case, there are 2 lines.
The first line of each test case contains N, the number of cubes.
The second line contains N space separated integers, denoting the sideLengths of each cube in that order.

Output Format:
For each test case, output a single line containing either Yes or No.

Sample Input:
STDIN        Function
-----        --------
2            T = 2
6            blocks[] size n = 6
4 3 2 1 3 4  blocks = [4, 3, 2, 1, 3, 4]
3            blocks[] size n = 3
1 3 2        blocks = [1, 3, 2]

Sample Output:
Yes
No

"""


t = int(input())
for _ in range(t):
    n = int(input())
    q = list(map(int, input().split()))
    f = 0
    r = n-1
    flag = True
    # print(q, f, r)
    max = 1 * pow(2, 31)
    count = 0
    while(True):
        count = count + 1
        if f > r:
            break
        if q[f] <= max and q[r] <= max:
            # print("both - ", end="")
            if q[f] >= q[r]:
                max = q[f]
                f = f+1
                # print("f")
            elif q[r] > q[f]:
                max = q[r]
                r = r-1
                # print("r")
            else:
                print("nothing")
        elif q[f] <= max:
            max = q[f]
            f = f+1
            # print("f")
        elif q[r] <= max:
            max = q[r]
            r = r-1
            # print("r")
        else:
            flag = False
            break
        # print("f:", f, "r:", r, "max:", max)
    # print("count:", count)
    if flag:
        print("Yes")
    else:
        print("No")
