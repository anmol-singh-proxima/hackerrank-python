from collections import deque


def tail(filename, n=10):
    'Print the last n lines of a file'
    d = deque(open(filename), n)
    for i in d:
        print(i, end='')

# tail("Details.txt", 10)


def delete_element(d, n):
    """ Function to delete the element on position 'n' in deque 'd' """
    d.rotate(n-1)
    d.pop()
    d.rotate(-n+1)
    return d


d = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(d)
d = delete_element(d, 5)
print(d)


def replace_element(d, n, e):
    """ Function to replace the element on position 'n' in deque 'd' with the given element 'e' """
    d.rotate(n-1)
    d.pop()
    d.append(e)
    d.rotate(-n+1)
    return d


d = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(d)
d = replace_element(d, 5, 10)
print(d)
