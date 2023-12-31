import xml.etree.ElementTree as ET

# Tạo một element gốc là root
root = ET.Element("company")

# Tạo các elements con và thêm vào root
giamdoc = ET.SubElement(root, "giamdoc")
giamdoc.text = "Hung"

diachi = ET.SubElement(root, "diachi")
diachi.text = "123 ABC Street"

dienthoai = ET.SubElement(root, "dienthoai")
dienthoai.text = "555-1234"

maso = ET.SubElement(root, "maso")
maso.text = "123456789"

# Tạo một object ElementTree
tree = ET.ElementTree(root)

# Ghi tài liệu XML ra file
tree.write("company.xml")
