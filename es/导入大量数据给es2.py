import requests
import json
import time
from datetime import datetime
from tqdm import tqdm
import random
from faker import Faker

fake = Faker()


class ESBulkInserter:
    def __init__(self, es_host="http://localhost:9200", index_name="test_large_data"):
        self.es_host = es_host
        self.index_name = index_name
        self.session = requests.Session()

    def create_index(self):
        """创建ES索引"""
        mapping = {
            "mappings": {
                "properties": {
                    "user_id": {"type": "keyword"},
                    "address": {"type": "keyword"},
                    "country": {"type": "keyword"}
                }
            }
        }

        url = f"{self.es_host}/{self.index_name}"
        response = self.session.put(url, json=mapping)

        if response.status_code in [200, 201]:
            print(f"索引 {self.index_name} 创建成功")
        elif response.status_code == 400 and "resource_already_exists_exception" in response.text:
            print(f"索引 {self.index_name} 已存在")
        else:
            print(f"创建索引失败: {response.text}")

    def bulk_insert(self, total_records=1000000, batch_size=10000):
        """批量插入数据"""
        print(f"开始插入 {total_records} 条数据...")

        url = f"{self.es_host}/_bulk"
        batch_count = (total_records + batch_size - 1) // batch_size

        start_time = time.time()

        for batch_num in range(batch_count):
            batch_data = []
            start_idx = batch_num * batch_size
            end_idx = min((batch_num + 1) * batch_size, total_records)

            # 准备批量数据
            for i in range(start_idx, end_idx):
                # 添加操作头
                batch_data.append(json.dumps({"index": {
                    "_index": self.index_name,
                    "_id": str(i + 1),
                }}))
                # 添加数据
                data = {
                    "user_id": f'{i:0>8}',
                    "address": fake.address(),
                    "country": fake.country(),
                }
                batch_data.append(json.dumps(data))

            # 构建批量请求体
            bulk_body = "\n".join(batch_data) + "\n"

            # 发送批量请求
            headers = {"Content-Type": "application/json"}
            response = self.session.post(url, data=bulk_body, headers=headers)

            if response.status_code == 200:
                result = response.json()
                if result.get("errors"):
                    errors = [item for item in result["items"] if item["index"].get("error")]
                    print(f"批次 {batch_num + 1} 有 {len(errors)} 个错误")
                else:
                    print(f"批次 {batch_num + 1}/{batch_count} 完成: {end_idx}/{total_records}")
            else:
                print(f"批次 {batch_num + 1} 失败: {response.text}")
                break

            # 进度显示
            progress = (batch_num + 1) / batch_count * 100
            print(f"进度: {progress:.1f}%")

        end_time = time.time()
        total_time = end_time - start_time
        print(f"数据插入完成! 总耗时: {total_time:.2f} 秒")
        print(f"平均速度: {total_records / total_time:.2f} 条/秒")

    def check_index_stats(self):
        """检查索引统计信息"""
        url = f"{self.es_host}/{self.index_name}/_count"
        response = self.session.get(url)
        if response.status_code == 200:
            count = response.json()["count"]
            print(f"索引 {self.index_name} 当前文档数量: {count}")
        else:
            print(f"获取统计信息失败: {response.text}")


# 使用示例
if __name__ == "__main__":
    # 初始化ES插入器
    es = ESBulkInserter(
        es_host="http://localhost:9200",  # 修改为您的ES地址
        index_name="t_user_info_detail"
    )

    # 1. 创建索引
    es.create_index()

    # 2. 批量插入100万数据
    es.bulk_insert(total_records=10000000, batch_size=10000)

    # 3. 检查结果
    es.check_index_stats()
