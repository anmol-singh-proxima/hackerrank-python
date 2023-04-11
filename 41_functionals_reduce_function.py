"""

Task:
Given a list of rational numbers,find their product.

Input Format:
First line contains N, the number of rational numbers.
The Ith of next N lines contain two integers each, the numerator(Ni) and denominator(Di) of the Ith rational number in the list.

Output Format:
Print only one line containing the numerator and denominator of the product of the numbers in the list in its simplest form, i.e. numerator and denominator have no common divisor other than 1.

Sample Input:
3
1 2
3 4
10 6

Sample Output:
5 8

Explanation:
Required product is (1/2) x (3/4) x (10/6) = 5/8

"""

from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x, y: x*y, fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)