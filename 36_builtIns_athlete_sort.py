"""

Task:
You are given a spreadsheet that contains a list of N athletes and their details (such as age, height, weight and so on). You are required to sort the data based on the Kth attribute and print the final resulting table.
Note that K is indexed from 0 to M-1, where M is the number of attributes.

Note: If two attributes are the same for different rows, for example, if two atheletes are of the same age, print the row that appeared first in the input.

Input Format:
The first line contains N and M separated by a space.
The next N lines each contain M elements.
The last line contains K.

Output Format:
Print the N lines of the sorted table. Each line should contain the space separated elements. Check the sample below for clarity.

Sample Input:
5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1

Sample Output:
7 1 0
10 2 5
6 5 9
9 9 9
1 23 12

Explanation:
The details are sorted based on the second attribute, since K is zero-indexed.

"""

def my_code():
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input())
    max = -9999
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j][k] > arr[j+1][k]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    for i in range(n):
        print(" ".join(map(str, arr[i])))


def short_code():
    n, m = map(int, input().split())
    rows = [input().split() for _ in range(n)]
    k = int(input())
    for row in sorted(rows, key=lambda row: int(row[k])):
        print(" ".join(row))


if __name__ == '__main__':
    my_code()
    short_code()