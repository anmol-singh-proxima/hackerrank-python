"""

Task:

There is an array of N integers. There are also 2 disjoint sets, A and B, each containing M integers.
You like all the integers in set A and dislike all the integers in set B.
Your initial happiness is 0. For each I integer in the array, if I belongs to A, you add 1 to your happiness. If I belongs to B, you add -1 to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since A and B are sets, they have no repeated elements. However, the array might contain duplicate elements.


Input Format

The first line contains integers N and M separated by a space.
The second line contains N integers, the elements of the array.
The third and fourth lines contain M integers, A and B, respectively.

Output Format

Output a single integer, your total happiness.


Sample Input:
3 2
1 3 5
1 3
5 0

Sample Output:
1

"""


def long_version():
    m, n = list(map(int, input().split()))
    arr = set(input().split())
    a_set = set(input().split())
    b_set = set(input().split())
    happiness = 0
    for i in arr:
        if i in a_set:
            happiness = happiness+1
        if i in b_set:
            happiness = happiness-1
    print(happiness)


def short_version():
    n, m = input().split()
    array = input().split()
    A = set(input().split())
    B = set(input().split())
    print(sum([(i in A) - (i in B) for i in array]))


if __name__ == "__main__":
    short_version()
