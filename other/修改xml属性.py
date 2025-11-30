from lxml import etree

xml_path = '/Users/huanghaoming/Documents/GitHub/nba-watch-face/app/src/main/res/raw/watchface.xml'
# 解析 XML 文件
parser = etree.XMLParser(remove_blank_text=True)
tree = etree.parse(xml_path, parser)
root = tree.getroot()

# 查找所有的 <Font> 元素，并设置它们的 family 属性
for font in root.xpath('.//Font'):
    font.attrib['family'] = 'timberwolves'  # 替换为你要设置的字体名称

# 将修改后的 XML 写回文件
tree.write(xml_path, pretty_print=True,
           xml_declaration=True, encoding='utf-8')

xml_path = '/Users/huanghaoming/Documents/GitHub/nba-watch-face/app/src/main/res/raw/watchface.xml'
# 解析 XML 文件
parser = etree.XMLParser(remove_blank_text=True)
tree = etree.parse(xml_path, parser)
root = tree.getroot()

# 查找所有的 <Font> 元素，并设置它们的 family 属性
for font in root.xpath('.//SequenceImages'):
    font.attrib['frameRate'] = '45'  # 替换为你要设置的字体名称

# 将修改后的 XML 写回文件
tree.write(xml_path, pretty_print=True,
           xml_declaration=True, encoding='utf-8')
