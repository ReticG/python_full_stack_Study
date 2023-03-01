# 基于 while 循环 + 计数 实现，输出5次，我爱我的祖国。
# num = 0
# while num < 5:
#     print("我爱我的祖国")
#     num += 1

# 循环输出 1~10 所有的整数
# num = 1
# while num <= 10:
#     print(num)
#     num += 1

# 循环输出 10~1 所有的整数
# num = 10
# while num >= 1:
#     print(num)
#     num -= 1

# 猜数字，给3次机会
# print("开始")
# count = 1
# while count <= 3:
#     num = int(input("请输入你要猜的数字："))
#     if num > 66:
#         print("大了")
#     elif num < 66:
#         print("小了")
#     else:
#         print("正确")
#         break()
#     count += 1
# print("结束")

# 猜数字，一直猜，直到猜对为止
# print("开始")
# flag = True
# while flag:
#     num = int(input("请输入你猜的数字："))
#     if num > 66:
#         print("大了")
#     elif num < 66:
#         print("小了")
#     else:
#         print("正确")
#         flag = False
# print("结束")

# print("开始")
# while True:
#     num = int(input("请输入你猜的数字："))
#     if num > 66:
#         print("大了")
#     elif num < 66:
#         print("小了")
#     else:
#         print("正确")
#         break
# print("结束")

# 输出 1~10，不要7
# num = 1
# while num <= 10:
#     if num == 7:
#         num += 1
#         continue
#     else:
#         print(num)
#         num += 1

# 字符串格式化
# text = "my name is {0}, {1} years' old".format("retic", 21)
# print(text)