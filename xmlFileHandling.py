import xml.etree.ElementTree as ET

#write xml file
root = ET.Element("students")

student = ET.SubElement(root, "student")
ET.SubElement(student, "name").text = "Alice"
ET.SubElement(student, "age").text = "25"

tree = ET.ElementTree(root)
tree.write("data.xml")

#read xml filex
tree = ET.parse("data.xml")
root = tree.getroot()

for student in root.findall("student"):
    name = student.find("name").text
    age = student.find("age").text
    print(name, age)
