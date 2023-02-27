print("Hello World")

# 例如： 找到在当前目录下，所有 png 格式的文件并打印
import os

for item in os.listdir("D:\Project\PycharmProjects\python_full_stack_Study\CodeExercise"):
    if item.endswith('png'):
        print(item)

# 输出不换行
print("xxxxxx", end="")
print("yyyyyy")

