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

2
6
4 3 2 1 3 4
3
1 3 2

Sample Output:
Yes
No

"""


from collections import deque


def using_collection_module():
    t = int(input())
    for i in range(t):
        size = int(input())
        top = 2**31
        d = deque(list(map(int, input().split())))
        for j in range(len(d)):
            if d[0] >= d[len(d)-1] and d[0] <= top:
                top = d.popleft()
            elif d[len(d)-1] <= top:
                top = d.pop()
            else:
                print('No')
                break
        if len(d) == 0:
            print('Yes')


def using_for_and_while_loop():
    t = int(input())

    for _ in range(t):
        num, cubes = int(input()), list(map(int, input().split()))
        yes_no = "Yes"

        while len(cubes) > 1:
            if cubes[0] >= cubes[-1]:
                larger_num = cubes[0]
                cubes.pop(0)
            else:
                larger_num = cubes[-1]
                cubes.pop(-1)
            if larger_num < cubes[0] or larger_num < cubes[-1]:
                yes_no = 'No'
                break

        print(yes_no)


def piling(d):
    while d:
        large = None
        if d[-1] > d[0]:
            large = d.pop()
        else:
            large = d.popleft()
        if len(d) == 0:
            return "Yes"
        if d[-1] > large or d[0] > large:
            return "No"


def using_if_else_statement():
    for i in range(int(input())):
        n = int(input())
        d = deque(map(int, input().split()))
        print(piling(d))


def my_code():
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


def my_code_v2():
    t = int(input())
    for _ in range(t):
        n = int(input())
        q = list(map(int, input().split()))
        f = 0
        r = n-1
        flag = True
        max = 1 * pow(2, 31)
        while(f < r):
            if f > r:
                break
            if q[f] <= max and q[f] >= q[r]:
                max = q[f]
                f = f+1
            elif q[r] <= max:
                max = q[r]
                r = r-1
            else:
                flag = False
                break
        if flag:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    # using_collection_module()
    my_code_v2()
