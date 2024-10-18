def judge():
    x = int(input('x is: '))
    y = int(input('y is: '))
    if x > y:
        print('x est plus grand que y.')
    elif x < y:
        print('x est petit que y.')
    else:
        print('x est aussi que y.')
    
judge()

def judge_2():
    x = int(input('x is: '))
    y = int(input('y is: '))
    if x > y or x < y: # 这里可以直接问 x == y or x != y
        aussi_pas(x,y)
    else:
        aussi(x,y)

def aussi(a,b):
    return print(f'{a} is equal to {b}.')

def aussi_pas(a,b):
    return print(f'{a} is unequal to {b}.')

judge_2()
# 这个例子中，单独定义函数比直接在条件语句中定义函数更复杂。但是如果本身要执行的语句就很复杂，单独定义会更好。
