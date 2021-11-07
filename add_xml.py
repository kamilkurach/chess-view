'''Skript makes xml file for images without bboxes.'''
import os

out_folder_path = '/home/yacotaco/Dokumenty/dev/ChessView/data/copy/xml'
folder = os.listdir('/home/yacotaco/Dokumenty/dev/ChessView/data/copy')

jpg = []
xml = []
count = 0

def xml_body(filename, out_folder_path):
    xml_body ="""
<annotation>
    <folder>images</folder>
    <filename>{0}.jpg</filename>
    <path>{1}/{2}.jpg</path>
    <source>
        <database>Unknown</database>
    </source>
    <size>
        <width>960</width>
        <height>544</height>
        <depth>3</depth>
    </size>
    <segmented>0</segmented>
</annotation>""".format(filename, out_folder_path, filename)
    return xml_body

for file in folder:
    if file.endswith('.jpg'):
        jpg.append(file.split('.')[0])
    elif file.endswith('.xml'):
        xml.append(file.split('.')[0])

for file in jpg:
    if file not in xml:
        count+=1
        filename = file
        body = xml_body(filename, out_folder_path)
        filename = "{0}.xml".format(file)
        with open(os.path.join(out_folder_path, filename), 'w') as f:
            f.write(body)
            f.close

print("{0} xml files added".format(count))
