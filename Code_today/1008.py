# 建立一个打招呼的函数，当用户输入名字的时候，和对方打招呼
def greeting():
    name = input("what's your name? ")
    print('hello,', name) # print()函数可以使用逗号链接多个变量，变量与变量之间默认有一个空格
greeting()
    
def hello(name):
    print('bonjour, '+ name) #在python中，可以使用"+"链接字符串，这就是为什么要在双引号之间保留一个空格
    return('zero') #这个函数的返回值是文本'zero'
nom=input("comment tu t'appelles?' ")
hello(nom)

# 三个连续的单引号或者双引号开始多行注释
'''
print(greeting()) # 输出none
print(hello('wheat')) # 输出zero

text=input('whatever') #input函数输出的结果是一个字符串
print(type(text))
number=input()


查阅python的官方文档，参看print()函数的官方解释
print(*object, sep=' ', end='\n')
*object:可以输入无数个对象
sep=' '：对象之间默认有一个空格
end='\n':函数结束后默认切换下一行
可以通过修改这些参数来调整函数输出的结果
'''
print('hello','wheat', 3, sep='🐷', end='')
print('it looks great!')

print('hello,\'whatever\'') # '\'这是一个转义字符，说明当下的情况要特别处理，此处表示单引号不意味着结束，要直接引用。
