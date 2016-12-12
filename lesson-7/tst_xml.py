
from xml.etree import ElementTree

root = ElementTree.parse('xml_people.xml')

print(root)
#root = root.getroot() # получает корневой элемент

# for a in root:
#     print(a, a.tag, a.text)
#
#     for b in a:
#         print(b.tag, b.text


print(root.findtext('age'))


# for a in root.findall('man'):
#     print(a)
#
# from xml.dom import minidom
#
# minidom.Document()
# minidom.Element()
#
# ElementTree.dump()