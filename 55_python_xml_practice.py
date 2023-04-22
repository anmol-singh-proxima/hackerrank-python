import os
import xml.etree.ElementTree as etree

XML_Data = """
<feed xmlns="http://www.w3.org/2005/Atom" xml:lang="en">
    <title>dive into mark</title>
    <subtitle>currently between addictions</subtitle>
    <id>tag:diveintomark.org,2001-07-29:/</id>
    <updated>2009-03-27T21:56:07Z</updated>
    <link rel="alternate" type="text/html" href="http://diveintomark.org/"/>
    <entry>
        <author>
            <name>Mark</name>
            <uri>http://diveintomark.org/</uri>
        </author>
        <title>Dive into history, 2009 edition</title>
        <link rel="alternate" type="text/html" href="http://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition"/>
        <id>tag:diveintomark.org,2009-03-27:/archives/20090327172042</id>
        <updated>2009-03-27T21:56:07Z</updated>
        <published>2009-03-27T17:20:42Z</published>
        <category scheme="http://diveintomark.org" term="diveintopython"/>
        <category scheme="http://diveintomark.org" term="docbook"/>
        <category scheme="http://diveintomark.org" term="html"/>
        <summary type="html">Putting an entire chapter on one page sounds bloated, but consider this &mdash; my longest chapter so far would be 75 printed pages, and it loads in under 5 seconds&hellip; On dialup.</summary>
    </entry>
    <entry>
        <author>
            <name>Mark</name>
            <uri>http://diveintomark.org/</uri>
        </author>
        <title>Accessibility is a harsh mistress</title>
        <link rel="alternate" type="text/html" href="http://diveintomark.org/archives/2009/03/21/accessibility-is-a-harsh-mistress"/>
        <id>tag:diveintomark.org,2009-03-21:/archives/20090321200928</id>
        <updated>2009-03-22T01:05:37Z</updated>
        <published>2009-03-21T20:09:28Z</published>
        <category scheme="http://diveintomark.org" term="accessibility"/>
        <summary type="html">The accessibility orthodoxy does not permit people to question the value of features that are rarely useful and rarely used.</summary>
    </entry>
    <entry>
        <author>
            <name>Mark</name>
        </author>
        <title>A gentle introduction to video encoding, part 1: container formats</title>
        <link rel="alternate" type="text/html" href="http://diveintomark.org/archives/2008/12/18/give-part-1-container-formats"/>
        <id>tag:diveintomark.org,2008-12-18:/archives/20081218155422</id>
        <updated>2009-01-11T19:39:22Z</updated>
        <published>2008-12-18T15:54:22Z</published>
        <category scheme="http://diveintomark.org" term="asf"/>
        <category scheme="http://diveintomark.org" term="avi"/>
        <category scheme="http://diveintomark.org" term="encoding"/>
        <category scheme="http://diveintomark.org" term="flv"/>
        <category scheme="http://diveintomark.org" term="GIVE"/>
        <category scheme="http://diveintomark.org" term="mp4"/>
        <category scheme="http://diveintomark.org" term="ogg"/>
        <category scheme="http://diveintomark.org" term="video"/>
        <summary type="html">These notes will eventually become part of a tech talk on video encoding.</summary>
    </entry>
</feed>
"""


def read_xml():
    file_root = os.getcwd()
    file_name = 'Extra_Files/feed.xml'
    file_path = os.path.join(file_root, file_name)
    file_obj = open(file_path, "r")
    # parser = etree.XMLParser(encoding="utf-8")
    # tree = etree.parse(file_obj, parser)
    tree = etree.parse("feed.xml")
    root = tree.getroot()
    print(root)
    return root


def get_xml():
    file = os.path.join(os.getcwd(), 'Extra_Files/feed.xml')
    xml = open(file, "r").read()
    # print(xml)
    print(type(xml))
    # tree = etree.ElementTree(etree.fromstring(xml))
    # print(tree)
    # root = tree.getroot()
    # return root


def xml_functionalities(root):
    print(root.tag)
    print(root.attrib)
    print(len(root))
    for child in root:
        print(child.tag)
        print(child.attrib)


if __name__ == "__main__":
    # root = read_xml()
    # root = get_xml()
    # print(root)
    get_xml()
    # xml_functionalities(root)