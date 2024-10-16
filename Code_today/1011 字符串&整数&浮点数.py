name = input('what\'s your name? ')
# 去除字符串之前和之后的的空格
name = name.strip() # 这是一个方法（method）(方法和函数的区别是？)，通常表现为变量名.方法名()。然而函数的表现形式是没有变量名。方法由类别定义，直接调用即可。函数从新开始创造？
# 首字母大写
# name = name.capitalize()
# 所有单词开头大写
name = name.title()
print(name)

# 方法叠加
name = input("what's your name? ").strip().title()
print(name)

# 分割字符串
first, middle, last = name.split(' ')
print(first,middle,last)
print('hello', middle, last)

# 可利用python文档查询相关函数、方法、变量等等知识。总而言之，你想要知道的一切都在官方文档里，如果这里还是没有你想要找到的答案，就去论坛（GitHub等等）

# 变量是否都要被命名。如果这个变量只会用到一次，可以不用单独命名，如果将来还会用到，可以单独命名。
# 整数 int
# 浮点（小数）float
x = float(input('input x '))
y = float(input('input y '))
z = x / y
# round(number,ndigit)：四舍五入。后面是保留小数的位数
z = round(z,1)
print(f'{z:,}') # 将数字格式化