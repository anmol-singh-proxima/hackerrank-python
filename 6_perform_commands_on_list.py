"""

Consider a list (list = []). You can perform the following commands:

1. insert i e: Insert integer e at position i.
2. print: Print the list.
3. remove e: Delete the first occurrence of integer e.
4. append e: Insert integer e at the end of the list.
5. sort: Sort the list.
6. pop: Pop the last element from the list.
7. reverse: Reverse the list.

Initialize your list and read in the value of N followed by N lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.


Sample Input:

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print


Sample Output:

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]

"""


if __name__ == '__main__':
    N = int(input())
    a_list = []
    for i in range(N):
        get_in = input()
        # print(get_in)
        input_list = get_in.split(" ")
        # print("input_list:", input_list)
        if input_list[0] == 'insert':
            index = int(input_list[1])
            ele = int(input_list[2])
            a_list.insert(index, ele)
        elif input_list[0] == 'remove':
            ele = int(input_list[1])
            a_list.remove(ele)
        elif input_list[0] == 'append':
            ele = int(input_list[1])
            a_list.append(ele)
        elif input_list[0] == 'sort':
            a_list.sort()
        elif input_list[0] == 'pop':
            a_list.pop()
        elif input_list[0] == 'reverse':
            a_list.reverse()
        elif input_list[0] == 'print':
            print(a_list)
        else:
            print("")
