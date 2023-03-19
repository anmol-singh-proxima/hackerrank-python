"""

You are given a valid XML document, and you have to print the maximum level of nesting in it. Take the depth of the root as 0.

Input Format

The first line contains N, the number of lines in the XML document.
The next N lines follow containing the XML document.

Output Format

Output a single line, the integer value of the maximum level of nesting in the XML document.

"""


import sys
import xml.etree.ElementTree as etree
maxdepth = 0


def count_level(elem, level):
    level = level + 1
    new_level = 0
    flag = False
    for i in range(len(elem)):
        # print(len(elem[i]), elem[i].text)
        if len(elem[i])>0:
            lvl = count_level(elem[i], level)
            if lvl > new_level:
                new_level = lvl
            # print("new_level:", new_level)
    if new_level > level:
        level = new_level
    # print("level:", level)
    return level


def depth(elem, level):
    global maxdepth
    # your code goes here
    if len(elem) > 0:
        maxdepth = count_level(elem, 0)
    else:
        maxdepth = 0


if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
