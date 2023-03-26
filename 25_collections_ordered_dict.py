"""

Task:
You are the manager of a supermarket.
You have a list of N items together with their prices that consumers bought on a particular day.
Your task is to print each item_name and net_price in order of its first occurrence.

Input Format:
The first line contains the number of items, N.
The next N lines contains the item's name and price, separated by a space.

Output Format:
Print the item_name and net_price in order of its first occurrence.

Sample Input:
9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30

Sample Output:
BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20

"""

from collections import OrderedDict


def my_code():
    ordered_dict = OrderedDict()
    n = int(input())
    for i in range(n):
        item_input = list(input().split())
        size = len(item_input)
        item = " ".join([item_input[j] for j in range(size-1)])
        price = int(item_input[size-1])
        if item in ordered_dict:
            ordered_dict[item] = ordered_dict[item] + price
        else:
            ordered_dict[item] = price

    for key, value in ordered_dict.items():
        print(key, value)


def short_code():
    order = OrderedDict()
    for _ in range(int(input())):
        item, space, price = input().rpartition(' ')
        order[item] = order.get(item, 0) + int(price)
    for item, price in order.items():
        print(item, price)


if __name__ == "__main__":
    short_code()


"""

Task:

You are given N words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.
Note: Each input line ends with a "\n" character.

Input Format:
The first line contains the integer, N.
The next N lines each contain a word.

Output Format:
Output 2 lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

Sample Input:
4
bcdef
abcdefg
bcde
bcdef

Sample Output:
3
2 1 1

Explanation:
There are 3 distinct words. Here, "bcdef" appears twice in the input at the first and last positions. The other words appear once each. The order of the first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the output.

"""

occur = OrderedDict()
for i in range(int(input())):
    word = input()
    occur[word] = occur.get(word, 0) + 1

print(len(occur))
for i in occur:
    print(occur[i], end=" ")
