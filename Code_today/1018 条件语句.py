# and
score = int(input('score is: '))
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')
    
# 判断用户输入值是奇数还是偶数
# bool 布尔值

# 通过条件语句判断
def parity(number):
    if number%2 == 0: # bool
        print('even')
    else:
        print('odd')

parity(0)

# 通过布尔值判断
def main(): # 主函数不做计算，直接调用判断奇偶的函数，通过这个函数返回的值（一个布尔值）来决定输出
    digt = int(input())
    if is_odd(digt):
        print('odd')
    else:
        print('even')
        
def is_odd(x):
    if x%2 == 1:
        return True # bool
    else:
        return False
        
# 一种专属于python的语言
def is_even(x):
    return True if x%2 == 0 else False
    
# 因为 x%2 == 0 这个表达式本身就是一个布尔值（也就是说这个表达式虽然看上去比较复杂，但是其"真面目"是True或者False，所以可以写成一个终极简洁版本
def s_is_even(x):
    return x%2 == 0
    
# 将开始创造的main更新为更简洁的版本
def main_2(x):
    return "even" if x%2 == 0 else "odd"


main()
print(is_even(8))
print(s_is_even(9))
print(main_2(3))

