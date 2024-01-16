class First:
    def __init__(self,name,age,prof):
        self.name = name
        self.age = age
        self.prof = prof
        self.Second = Second()
        self.Third = Third()
        print(self.Second.lname, self.Third.timar)

    def details(self):
        print(self.name + ' is ' + str(self.age) + ' years old and working as '+ self.prof)

class Second(First):
    def __init__(self):
        self.lname = 'noob'


    def full(self):
        print('N the Last name is ' + self.lname , self.name)


class Third:
    def __init__(self):
        self.timar = 'yuta 90'
abc = First('ssiya',457,'waiter')
# ab = Second()
# ab.full()
# ab.details()
abc.details()