from homework4 import Name, Age, Print, Prent


class Import(Name, Age, Print, Prent):
    def __init__(self, age, name):
        Age.__init__(self, age)
        self.__age = age
        self.name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

aratus = Import(4, 'mark')

print(aratus.age)
print(aratus.name)


