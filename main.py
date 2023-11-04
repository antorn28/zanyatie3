class Grandparent:
    height = 170
    satiety = 100
    def __init__(self):
        age = 60

class Parent(Grandparent):
    def __init__(self):
        age = 40

class Child(Parent):
    height = 95

    def __init__(self):
        print(self.height)
        #print(self.age)
        print(super().__init__())
        print(self.satiety)

ch = Child()

from Hello import Hello_world

class Hello_world:
    hello = "Hello"
    _hello = "_Hello"
    __hello = "__Hello"
    def hi_print(self):
        print(self.hello)
        print(self._hello)
        print(self.__hello)


my_lst = [1,2,3,4,5]
iterator = iter(my_lst)

print(iterator)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

a = list(range(1,10))
a = a.__iter__()
print(a.__next__())