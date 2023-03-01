print("Hello World")

# 例如： 找到在当前目录下，所有 png 格式的文件并打印
import os

for item in os.listdir("D:\Project\PycharmProjects\python_full_stack_Study\CodeExercise"):
    if item.endswith('png'):
        print(item)

# 输出不换行
print("xxxxxx", end="")
print("yyyyyy")

print("欢迎使用联通系统")

user = input("请输入用户名：")
pwd = input("请输入密码：")

if user == "gjc" and pwd == "123":
    print("恭喜你")
    print("登录成功，获得奖励100w。")
else:
    print("登录失败")
    print("你错过的是一个成为年薪百万的机会")
print("程序结束")
