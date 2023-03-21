"""

Task:
You are given a list of N lowercase English letters. For a given integer K, you can select any K indices (assume 1-based indexing) with a uniform probability from the list.

Find the probability that at least one of the K indices selected will contain the letter: 'a'.

Input Format:
The input consists of three lines.
The first line contains the integer N, denoting the length of the list.
The next line consists of N space-separated lowercase English letters, denoting the elements of the list.
The third and the last line of input contains the integer K, denoting the number of indices to be selected.

Output Format:
Output a single line consisting of the probability that at least one of the  indices selected contains the letter:'a'.
Note: The answer must be correct up to 3 decimal places.

Sample Input:
4 
a a c d
2

Sample Output:
0.8333


"""


# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations

n = int(input())
arr = list(input().split())
k = int(input())

comb = list(combinations(arr, k))

count_a = 0
for item in comb:
    for j in range(k):
        if item[j] == 'a':
            count_a = count_a + 1
            break

# print(len(comb))
# print(count_a)
print(count_a/len(comb))
