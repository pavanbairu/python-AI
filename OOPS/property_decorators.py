class example:

    def __init__(self, name, mobile):
        self.name = name
        self.__mobile = mobile

ex1 = example("pavan", 12345)  

# print(ex1.mobile)             cannot access this
print(ex1.name)

print(30*'*')


class example2:

    def __init__(self, name, mobile):
        self.name = name
        self.mobile = mobile

    @property
    def mobile_set(self):
        return self.__mobile


ex2 = example2("prashanth", 987654)
print(ex2.mobile)     # able to access the mobile now

print(30*'*')


class example3:

    def __init__(self, name, mobile):
        self.name = name
        self.mobile = mobile

    @property
    def mobile_access(self):
        return self.__mobile
    

    @mobile_access.setter
    def mobile_access_set(self, mobile):
        if isinstance(mobile, int) and len(str(mobile)) == 10:
            self.__mobile = mobile
        else:
            pass

ex3 = example3("pavan", 89736483)
ex3.mobile_access_set = 1789066
print(ex3.mobile_access)
    
