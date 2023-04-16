"""

Task:
You are given an HTML code snippet of N lines.
Your task is to print start tags, end tags and empty tags separately.

Format your results in the following way:
Start : Tag1
End   : Tag1
Start : Tag2
-> Attribute2[0] > Attribute_value2[0]
-> Attribute2[1] > Attribute_value2[1]
-> Attribute2[2] > Attribute_value2[2]
Start : Tag3
-> Attribute3[0] > None
Empty : Tag4
-> Attribute4[0] > Attribute_value4[0]
End   : Tag3
End   : Tag2

Here, the -> symbol indicates that the tag contains an attribute. It is immediately followed by the name of the attribute and the attribute value.
The > symbol acts as a separator of the attribute and the attribute value.

If an HTML tag has no attribute then simply print the name of the tag.
If an attribute has no attribute value then simply print the name of the attribute value as None.

Note: Do not detect any HTML tag, attribute or attribute value inside the HTML comment tags (<!-- Comments -->).Comments can be multiline as well.

Input Format:
The first line contains integer N, the number of lines in a HTML code snippet.
The next N lines contain HTML code.

Output Format:
Print the HTML tags, attributes and attribute values in order of their occurrence from top to bottom in the given snippet.
Use proper formatting as explained in the problem statement.

Sample Input:
2
<html><head><title>HTML Parser - I</title></head>
<body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>

Sample Output:
Start : html
Start : head
Start : title
End   : title
End   : head
Start : body
-> data-modal-target > None
-> class > 1
Start : h1
End   : h1
Empty : br
End   : body
End   : html

"""


from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for attr in attrs:
            print("->", attr[0], ">", attr[1])

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for attr in attrs:
            print("->", attr[0], ">", attr[1])


parser = MyHTMLParser()

for _ in range(int(input())):
    parser.feed(input())


"""

Task:
You are given an HTML code snippet of N lines.
Your task is to print the single-line comments, multi-line comments and the data.

Print the result in the following format:
>>> Single-line Comment
Comment
>>> Data
My Data
>>> Multi-line Comment
Comment_multiline[0]
Comment_multiline[1]
>>> Data
My Data
>>> Single-line Comment:

Note: Do not print data if data == '\n'.

Input Format:
The first line contains integer N, the number of lines in the HTML code snippet.
The next  lines contains HTML code.

Output Format:
Print the single-line comments, multi-line comments and the data in order of their occurrence from top to bottom in the snippet.
Format the answers as explained in the problem statement.

Sample Input:
4
<!--[if IE 9]>IE9-specific content
<![endif]-->
<div> Welcome to HackerRank</div>
<!--[if IE 9]>IE9-specific content<![endif]-->

Sample Output:
>>> Multi-line Comment
[if IE 9]>IE9-specific content
<![endif]
>>> Data
 Welcome to HackerRank
>>> Single-line Comment
[if IE 9]>IE9-specific content<![endif]

"""


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if data.count("\n") == 0:
            print(">>> Single-line Comment")
        else:
            print(">>> Multi-line Comment")
        print(data)

    def handle_data(self, data):
        if data != "\n":
            print(">>> Data")
            print(data)


html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
parser = MyHTMLParser()
parser.feed(html)
parser.close()
