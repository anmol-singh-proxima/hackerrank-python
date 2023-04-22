import os
import xml.etree.ElementTree as etree

# Read the XML file and find the root element of it
file = os.path.join(os.getcwd(), 'Extra_Files/feed_only_xml.xml')
parser = etree.XMLParser(encoding="utf-8")
tree = etree.parse(file, parser)
root = tree.getroot()

# Print tags and attributes of root and its children
print(root.tag)
print(root.attrib)
print(len(root))
for child in root:
    print(child.tag)
    print(child.attrib)
    print(len(child.attrib))

# Finding certain children in root
entries = root.findall('{http://www.w3.org/2005/Atom}entry')
print(entries)
for entry in entries:
    title = entry.find('{http://www.w3.org/2005/Atom}title')
    print(title.tag)
print(entries[0].find('page'))


# Finding in the descendants of the root
all_links = tree.findall('.//{http://www.w3.org/2005/Atom}link')
for link in all_links:
    print(link, " => ", link.attrib)
