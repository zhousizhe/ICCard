import xml.etree.ElementTree as elementTree
def getValue(model_, paraName_, value_):
    tree = elementTree.parse('./default.xml')  # 读取配置文件
    root = tree.getroot()  # 获得根节点
    for model in root.findall(model_):
        # print(model)
        for paraName in model.findall(paraName_):
            # print(paraName)
            for value in paraName.findall(value_):
                # print(value.text, value.tag, value.get('default'))
                result = value.text
    return result

def setValue(model_, paraName_, value_1, value_2):
    tree = elementTree.parse('./default.xml')  # 读取配置文件
    root = tree.getroot()  # 获得根节点
    for model in root.findall(model_):
        # print(model)
        for paraName in model.findall(paraName_):
            # print(paraName)
            for value in paraName.findall(value_1):
                value.text = str(value_2)
    tree.write('./default.xml', encoding='utf-8', xml_declaration=True)