from prefect import task

@task
def fetch_data_from_api():
    # 模拟从 API 获取数据
    print("Fetching data from API...")
    return {"data": "some data from API"}

@task
def process_data(data):
    # 数据处理
    print(f"Processing data: {data}")
    return f"Processed {data}"

@task
def store_data(data):
    # 存储数据到数据库或文件
    print(f"Storing data: {data}")
from prefect import Flow

with Flow("Data Processing Flow") as flow:
    data = fetch_data_from_api()
    processed_data = process_data(data)
    store_data(processed_data)

# 启动工作流
flow.run()

