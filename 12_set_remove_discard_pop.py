"""

Task:
You have a non-empty set S, and you have to execute N commands given in N lines.
The commands will be pop, remove and discard.

Input Format:
The first line contains integer M, the number of elements in the set S.
The second line contains M space separated elements of set S. All of the elements are non-negative integers, less than or equal to 9.
The third line contains integer N, the number of commands.
The next N lines contains either pop, remove and/or discard commands followed by their associated value.

Output Format:
Print the sum of the elements of set S on a single line.


Sample Input:
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5

Sample Output:
4  [Any number because of randomness of pop() in set]

"""

n = int(input())
s = set(map(int, input().split()))
n = int(input())
for i in range(n):
    command = input().split()
    if command[0] == "pop":
        s.pop()
    else:
        ele = int(command[1])
        if command[0] == "remove":
            s.remove(ele)
        elif command[0] == "discard":
            s.discard(ele)
sum = sum(list(s))
print(sum)
