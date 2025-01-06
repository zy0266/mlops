from prefect import flow, task

# 定义一个简单的任务
@task
def say_hello(name: str):
    print(f"Hello, {name}!")

# 定义一个工作流
@flow
def hello_flow(name: str):
    say_hello(name)

# 运行工作流
if __name__ == "__main__":
    hello_flow("World")
from prefect import flow
from prefect import Client
from prefect.schedules import IntervalSchedule
from datetime import timedelta

# 创建一个定期执行的调度，每隔5分钟执行一次
schedule = IntervalSchedule(interval=timedelta(minutes=5))

@flow(schedule=schedule)
def hello_flow():
    print("Hello, Prefect!")

# 连接到 Prefect 服务器，确保连接正确的API地址
client = Client(api_url="http://127.0.0.1:4200/api/")

# 注册工作流到 Prefect 服务器
hello_flow.register(project_name="My Prefect Project")

# 如果你希望立即运行工作流，可以手动调用流
# hello_flow()


