def main():
    name = input('tell me your name: ')
    hello(name)
    
def hello(to):
    print('hello',to)
    
main() 



'''
程序一开始即设定主函数main，在主函数中调用函数，即使这个函数还没有被定义（所以，程序运行并不是简单线性的，先定义再调用，而是可以提前调用尚未定义的函数，但是，这个提前可以提前多远呢，如果这是一个上万行的程序，一开始就调用一个在九千行才定义的函数，这可行吗？）

但是变量的调用是有范围限定的。即实参（变量）有其作用域(scope)，在某个范围内被定义的变量，只能在这个范围内被调用，不能跨函数传递。例如，主函数中的name，不能hello函数直接调用，hello函数可重新定义name.

'''

# return
# 设定两个函数，一个是主函数，一个是被调用的函数，主函数用到次函数返回的值
def main_s():
    x = int(input('x is: '))
    print('the square of x is:', square(x)) # 调用接下来定义的函数square()
    
def square(n): 
    return n*n
    # return n**2
    # return pow(n,2)
    
main_s()


def hello():
    name = input("comment vous vous appellez? ")
    print('hello',name)
hello()
# 未知变量，是作为"参数"parameter在函数之前定义比较合适呢，还是在函数内定义比较好呢？

# 形参和实参，default参数
def hello(to = 'tout le monde'):# 当定义函数时，给定参数一个具体的值，这个值就是这个参数的默认设定，如果用户没有输入参数值，那么函数就会自动调用这个默认值。（类似于print()里，默认用逗号链接两个变量，以及变量之间用空格分开）函数有初始设定值，那就意味着，用户可以跳过不输入这个变量。
    print('hello,', to)

hello() # 直接调用函数，不给参数赋值
name = input('comment tu t\'appelles: ')
hello(name) # name在这里是实参

