"""

Task:

You are given a function f(X) = X^2. You are also given K lists. The Ith list consists of Ni elements.

You have to pick one element from each list so that the value from the equation below is maximized:

S = (f(X1) + f(X2) + ______ + f(Xk)) % M


Xi denotes the element picked from the Ith list . Find the maximized value Smax obtained.

% denotes the modulo operator.

Note that you need to take exactly one element from each list, not necessarily the largest element. You add the squares of the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the answer to the problem.


Input Format

The first line contains 2 space separated integers K and M.
The next K lines each contains an integer Ni, denoting the number of elements in the Ith list, followed by Ni space separated integers denoting the elements in the list.


Output Format:
Output a single integer denoting the value Smax.

Sample Input:
3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 

Sample Output:
206

"""


from itertools import product

if __name__ == "__main__":
    k, m = list(map(int, input().split()))

    arr = list()
    for i in range(k):
        numbers = list(map(int, input().split()))
        del numbers[0]
        arr.append(numbers)
    comb = list(product(*arr))
    # print(arr)
    # print(comb)

    s = -99999999
    for item in comb:
        sum_sq = 0
        for i in range(k):
            sum_sq = sum_sq + pow(item[i], 2)
        mod = sum_sq%m
        if mod > s:
            s = mod

    print(s)
