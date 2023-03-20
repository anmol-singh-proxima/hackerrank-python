"""

itertools.product()
This tool computes the cartesian product of input iterables.
It is equivalent to nested for-loops.
For example, product(A, B) returns the same as ((x,y) for x in A for y in B).

Input Format:
The first line contains the space separated elements of list A.
The second line contains the space separated elements of list B.

Both lists have no duplicate integer elements.

Output Format:
Output the space separated tuples of the cartesian product.

Sample Input:
1 2
3 4

Sample Output:
(1, 3) (1, 4) (2, 3) (2, 4)

"""


from itertools import combinations_with_replacement
from itertools import combinations
from itertools import permutations
from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

prod = list(product(a, b))

for x in prod:
    print(x, end=" ")


"""

itertools.permutations(iterable [, R])
This tool returns successive R length permutations of elements in an iterable.
If R is not specified or is None, then R defaults to the length of the iterable, and all possible full length permutations are generated.
Permutations are printed in a lexicographic sorted order. So, if the input iterable is sorted, the permutation tuples will be produced in a sorted order.

Task:
You are given a string S.
Your task is to print all possible permutations of size K of the string in lexicographic sorted order.

Input Format:
A single line containing the space separated string S and the integer value K.

Output Format:
Print the permutations of the string S on separate lines.

Sample Input:
HACK 2

Sample Output:
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH

"""


word, r = input().split()
lst = list(word)
lst.sort()
word = "".join(lst)
p = list(permutations(word, int(r)))
for i in p:
    print("".join(i))


"""

itertools.combinations(iterable, R)

This tool returns the R length subsequences of elements from the input iterable.
Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

Task:
You are given a string S.
Your task is to print all possible combinations, up to size K, of the string in lexicographic sorted order.

Input Format:
A single line containing the string S and integer value K separated by a space.


Output Format:
Print the different combinations of string S on separate lines.

Sample Input:
HACK 2

Sample Output:
A
C
H
K
AC
AH
AK
CH
CK
HK

"""


word, k = input().split()

lst = list(word)
lst.sort()
word = "".join(lst)
k = int(k)

for i in range(1, k+1):
    comb = list(combinations(word, i))
    for j in comb:
        print("".join(j))


"""

itertools.combinations_with_replacement(iterable, R)

This tool returns R length subsequences of elements from the input iterable allowing individual elements to be repeated more than once.
Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

Task:
You are given a string S.
Your task is to print all possible size K replacement combinations of the string in lexicographic sorted order.

Input Format:
A single line containing the string S and integer value K separated by a space.


Output Format:
Print the combinations with their replacements of string S on separate lines.

Sample Input:
HACK 2

Sample Output:
AA
AC
AH
AK
CC
CH
CK
HH
HK
KK

"""


word, r = input().split()
lst = list(word)
lst.sort()
word = "".join(lst)
r = int(r)

p = list(combinations_with_replacement(word, r))
for i in p:
    print("".join(i))
