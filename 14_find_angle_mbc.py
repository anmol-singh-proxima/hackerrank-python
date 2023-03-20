"""

Task:
ABC is a right triangle, 90 degree at B.
Therefore, angle ABC = 90 degree.
Point M is the midpoint of hypotenuse AC.
You are given the lengths AB and BC.
Your task is to find angle MBC in degrees.

Input Format:
The first line contains the length of side AB.
The second line contains the length of side BC.

Output Format:
Output angle MBC in degrees.


Sample Input:
10
10

Sample Output:
45 degree

Note: Wherever degree is written, it should be degree symbol(not word).

"""

from math import atan, pi

if __name__ == "__main__":
    ab = int(input())
    bc = int(input())
    radian = atan(ab/bc)
    degree = 180/pi * radian
    print("{}{}".format(round(degree), chr(176)))
