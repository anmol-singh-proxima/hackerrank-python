"""

Task:
You are given a polynomial P(x) of a single indeterminate (or variable), x.
You are also given the values of x and k. Your task is to verify if P(x) = k.

Input Format:
The first line contains the space separated values of x and k.
The second line contains the polynomial P.

Output Format
Print True if P(x) = k. Otherwise, print False.

Sample Input:
1 4
x**3 + x**2 + x + 1

Sample Output:
True

Explanation:
P(1) = 1^3 + 1^2 + 1 + 1 = 4 = k
Hence, the output is True.

"""

x, k = map(int, input().split())
# print(eval(input()) == k)
polynomial = input()
if eval(polynomial) == k:
    print("True")
else:
    print("False")
