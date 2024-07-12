import json


def create_tree_json(current_level, max_level):
    if current_level < max_level:
        children = [
            {
                "value": f"layer-{current_level + 1}-node-{i}",
                "label": f"layer-{current_level + 1}-node-{i}",
                "children": create_tree_json(current_level + 1, max_level)
            }
            for i in range(5)  # 每层3个节点
        ]
        return children
    else:
        return []


max_level = 8  # 树的最大层数
tree_json = [{
    "value": "root",
    "label": "root",
    "children": create_tree_json(1, max_level)
}]

# 打开文件用于写入，如果文件不存在将会被创建
with open('tree.json', 'w', encoding='utf-8') as file:
    # 将文本写入文件
    file.write(json.dumps(tree_json))
