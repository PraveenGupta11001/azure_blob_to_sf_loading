import xml.etree.ElementTree as ET

def compare_xml(file1, file2):
    # Parse XML files into ElementTree objects
    tree1 = ET.parse(file1)
    tree2 = ET.parse(file2)

    # Get root elements of both trees
    root1 = tree1.getroot()
    root2 = tree2.getroot()

    # Check if the tag names of the root elements are the same
    if root1.tag != root2.tag:
        print("Root tags are different.")
        return False

    # Check if the structures of the trees are the same
    if not compare_elements(root1, root2):
        print("XML structures are different.")
        return False

    print("XML files are identical.")
    return True

def compare_elements(elem1, elem2):
    # Compare tags
    if elem1.tag != elem2.tag:
        return False

    # Compare attributes
    if elem1.attrib != elem2.attrib:
        return False

    # Compare text content
    if elem1.text != elem2.text:
        return False

    # Compare child elements recursively
    children1 = list(elem1)
    children2 = list(elem2)

    if len(children1) != len(children2):
        return False

    for child1, child2 in zip(children1, children2):
        if not compare_elements(child1, child2):
            return False

    return True

# Example usage:
file1 = "pb001BackgroundReportData_0.xml"
file2 = "test.xml"
compare_xml(file1, file2)
