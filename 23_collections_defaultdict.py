"""

Task:
collections.defaultdict()
In this challenge, you will be given 2 integers, N and M. There are N words, which might repeat, in word group A. There are M words belonging to word group B. For each M words, check whether the word has appeared in group A or not. Print the indices of each occurrence of M in group A. If it does not appear, print -1.

Input Format:
The first line contains integers, N and M separated by a space.
The next N lines contains the words belonging to group A.
The next M lines contains the words belonging to group B.

Output Format:
Output M lines.
The Ith line should contain the 1-indexed positions of the occurrences of the Ith word separated by spaces.


Sample Input:
STDIN   Function
-----   --------
5 2     group A size n = 5, group B size m = 2
a       group A contains 'a', 'a', 'b', 'a', 'b'
a
b
a
b
a       group B contains 'a', 'b'
b

Sample Output:
1 2 4
3 5

"""

from collections import defaultdict

if __name__ == "__main__":
    a = list()
    b = list()

    m, n = list(map(int, input().split()))

    for i in range(m):
        a.append(input())
    for i in range(n):
        b.append(input())

    # print(a)
    # print(b)

    d = defaultdict(list)

    for i in range(len(a)):
        if a[i] in b:
            d[a[i]].append(i+1)

    for i in b:
        # print(i)
        if i not in a:
            d[i].append(-1)

    for i in b:
        print(" ".join(list(map(str, d[i]))))
