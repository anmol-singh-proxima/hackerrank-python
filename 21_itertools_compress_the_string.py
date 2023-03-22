"""

Task:
In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools.
You are given a string S. Suppose a character 'C' occurs consecutively X times in the string. Replace these consecutive occurrences of the character 'C' with (X,C) in the string.

Input Format:
A single line of input consisting of the string s.

Output Format:
A single line of output consisting of the modified string.

Sample Input:
1222311

Sample Output:
(1, 1) (3, 2) (1, 3) (2, 1)

Explanation:
First, the character 1 occurs only once. It is replaced by (1,1). Then the character 2 occurs three times, and it is replaced by (3,2) and so on.
Also, note the single space within each compression and between the compressions.

"""


from itertools import groupby

if __name__ == "__main__":
    s = input()
    def key_func(x): return x
    occurence = list()

    for key, group in groupby(s, key_func):
        key = int(key)
        occur = len(list(group))
        occurence.append((occur, key))

    # for i in occurence:
    #     print(i, end=" ")
    print(" ".join(map(str, occurence)))
