import xml.dom.minidom as minidom
import xml.etree.ElementTree as ET


# Tạo một Document mới
doc = minidom.Document()

# Tạo một element gốc là root
root = doc.createElement("students")
doc.appendChild(root)

# Tạo danh sách sinh viên
students = [
    {"maSV": "SV001", "tenSV": "Nguyen Van A", "namsinh": "2000", "lop": "12A", "gioitinh": "Nam"},
    {"maSV": "SV002", "tenSV": "Tran Thi B", "namsinh": "2001", "lop": "11B", "gioitinh": "Nữ"},
    {"maSV": "SV003", "tenSV": "Le Van C", "namsinh": "2002", "lop": "10C", "gioitinh": "Nam"},
]

# Tạo các elements con cho từng sinh viên và thêm vào root
for student in students:
    student_element = ET.SubElement(root, "student")
    
    maSV_element = ET.SubElement(student_element, "maSV")
    maSV_element.text = student["maSV"]
    
    tenSV_element = ET.SubElement(student_element, "tenSV")
    tenSV_element.text = student["tenSV"]
    
    namsinh_element = ET.SubElement(student_element, "namsinh")
    namsinh_element.text = student["namsinh"]
    
    lop_element = ET.SubElement(student_element, "lop")
    lop_element.text = student["lop"]
    
    gioitinh_element = ET.SubElement(student_element, "gioitinh")
    gioitinh_element.text = student["gioitinh"]

# Tạo một object ElementTree
tree = ET.ElementTree(root)

# Ghi tài liệu XML vào file
with open("students.xml", "w", encoding="utf-8") as file:
    doc.writexml(file, indent="  ", addindent="  ", newl="\n", encoding="utf-8")
