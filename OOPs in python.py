class First:
    def __init__(self,name,age,prof):
        self.name = name
        self.age = age
        self.prof = prof

    def details(self):
        print(self.name + ' is ' + str(self.age) + ' years old and working as '+ self.prof)

class Second(First):
    def __init__(self,name,age,prof):
        # self.lname = lname
        First.__init__(self,name,age,prof)

    def full(self):
        print('N the Last name is ' + self.prof , self.name)

# abc = First()
ab = Second('sut',45,'toyer')
ab.full()
ab.details()
# abc.details()