"""

Task:

You are given a set A and N other sets.
Your job is to find whether set A is a strict superset of each of the N sets.
Print True, if A is a strict superset of each of the N sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.


Input Format:
The first line contains the space separated elements of set A.
The second line contains integer N, the number of other sets.
The next N lines contains the space separated elements of the other sets.

Output Format:
Print True if set A is a strict superset of all other N sets. Otherwise, print False.


Sample Input:
1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12

Sample Output:
False

"""


if __name__ == "__main__":
    a = set(map(int, input().split()))
    n = int(input())
    count = 0
    for i in range(n):
        b = set(map(int, input().split()))
        flag = True
        for j in b:
            if j not in a:
                flag = False
                break
        if flag:
            for j in a:
                if j not in b:
                    count = count + 1
                    break
    if count == n:
        print(True)
    else:
        print(False)
