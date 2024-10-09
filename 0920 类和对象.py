class Point():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def move(self):
        print('move')
    def draw(self):
        print('draw')
point1=Point(3,4)
point1.move()
point1.draw()
point1.x=1
print(point1.x) #这是这个对象特有的属性
point2=Point(5,6)
point2.x=2
print(point2.x)
print(point1.a) #这个值可以在外部更新

class Pearson():
    def calling(self,name):
        self.name=name
        print(self.name)
    def talk(self):
        print(f'nice to meet u')
momo=Pearson()
momo.calling('momo')
momo.talk()

class Mammal():
    def walk(self):
        print('walk')
class Dog(Mammal):
    def sound(self):
        print('wangwangwang')
class Cat(Mammal):
    def sound(self):
        print('mewmewmew')
pang=Dog()
pang.walk()
pang.sound()
mo=Cat()
mo.walk()
mo.sound()