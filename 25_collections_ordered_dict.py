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
