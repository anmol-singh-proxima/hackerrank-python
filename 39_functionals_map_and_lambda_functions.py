"""

Task:
Let's learn some new Python concepts! You have to generate a list of the first N fibonacci numbers, 0 being the first number. Then, apply the map function and a lambda expression to cube each fibonacci number and print the list.

Input Format:
One line of input: an integer N.

Output Format:
A list on a single line containing the cubes of the first N fibonacci numbers.

Sample Input:
5

Sample Output:
[0, 1, 1, 8, 27]

"""


def cube(x): return x**3


def fibonacci1(n):
    fib_num = [0, 1]
    for i in range(2, n):
        fib_num.append(fib_num[i-1]+fib_num[i-2])
    return fib_num[0:n]


def fibonacci2(n):
    a, b, c = 0, 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci1(n))))
    print(list(map(cube, fibonacci2(n))))
