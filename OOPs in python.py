class First:
    def __init__(self,name,age,prof):
        self.name = name
        self.age = age
        self.prof = prof

    def details(self):
        print(self.name + ' is ' + str(self.age) + ' years old and working as '+ self.prof)

class Second(First):
    def __init__(self,name,age,prof,lname):
        self.lname = lname
        First.__init__(self,name,age,prof)

    def full(self):
        print('N the Last name is ' + self.lname , self.name)

abc = First('siut',457,'hoyer')
ab = Second('sut',45,'toyer','suari')
ab.full()
ab.details()
abc.details()