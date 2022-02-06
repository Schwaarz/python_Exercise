# import unittest
# from Test_Case import login_Test
# login_Test.BaiduTest().test01()

list = [1,2,3,4]
print(list[0],list[1])

list2 = {"age1":33,"age2":24,"age3":38}

print(sorted(list2.items(),key=lambda age1:age1[1]))

class Dog():
    def __init__(self,name,age,dz):
        self.name = name
        self.age = age
        self.dz = dz
    def sit(self):
        print(self.name.title() + "蹲下" )
    def roll(self):
        print(self.name.title() + "打滚")
    def dog_age(self):
        print(str(self.age) + "岁")
    def dog_dz(self):
        print(self.dz + "扑")
my_dog = Dog('haha',7,"kan")
my_dog.sit()
my_dog.roll()
my_dog.dog_age()
my_dog.dog_dz()