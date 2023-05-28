"""

Task:
There is an array of N integers. There are also 2 disjoint sets, A and B, each containing M integers.
You like all the integers in set A and dislike all the integers in set B.
Your initial happiness is 0. For each I integer in the array, if I belongs to A, you add 1 to your happiness. If I belongs to B, you add -1 to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since A and B are sets, they have no repeated elements. However, the array might contain duplicate elements.


Input Format:
The first line contains integers N and M separated by a space.
The second line contains N integers, the elements of the array.
The third and fourth lines contain M integers, A and B, respectively.

Output Format:
Output a single integer, your total happiness.

Sample Input:
3 2
1 3 5
1 3
5 0

Sample Output:
1

"""


def my_code():
    m, n = list(map(int, input().split()))
    arr = set(input().split())
    a = set(input().split())
    b = set(input().split())
    happy = 0
    for i in arr:
        happy = happy+1 if i in a else happy
        happy = happy-1 if i in b else happy
    print(len(a))
    print(len(b))
    print(happy)


def short_version():
    n, m = input().split()
    array = input().split()
    A = set(input().split())
    B = set(input().split())
    print(sum([(i in A) - (i in B) for i in array]))


def code_for_file():
    f = open("./Test_Cases/11_count_happiness_test_case_2.txt", "r")
    m, n = list(map(int, f.readline().split()))
    print(m, n)
    arr = set(f.readline().split())
    a = set(f.readline().split())
    b = set(f.readline().split())
    happy = 0
    # for i in arr:
    #     happy = happy+1 if i in a else happy
    #     happy = happy-1 if i in b else happy
    # happiness = sum([1 if i in a else (-1 if i in b else 0) for i in arr])
    happiness = sum([(i in a) - (i in b) for i in arr])
    print(len(arr))
    print(len(a))
    print(len(b))
    print(happiness)


if __name__ == "__main__":
    # my_code()
    code_for_file()
