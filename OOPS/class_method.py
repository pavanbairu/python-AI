# in general we pass the arguments to the class by object creation
class example:

    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def display(self):
        print(self.name, self.email)
    
obj = example("pavan","pavan@gmail.com")
obj.display()


# now we pass using the class method

class example2:

    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    @classmethod                               # decorating it as class method so that we can pass input to the class
    def details(cls, name1 , email1):       # these email1 and name1 are assigning to init variables email and name
        return cls(name1, email1)
    
    def display(self):
        print(self.name, self.email)

obj2 = example2.details("prashanth", "prashanth@gmail.com")   # calling classmethod with classname
obj2.display()
print(obj2.name)    # emai1 from details method is assigned to init variable 
print(obj2.email)


# class level variables 
class example3:

    mobile_number = 7383787

    def __init__(self, name, email):
        self.name = name
        self.email = email

    @classmethod
    def change_mobile(cls, mobile):             # changing the mobile number
        cls.mobile_number = mobile
    
    @classmethod                               # decorating it as class method so that we can pass input to the class
    def details(cls, name1 , email1):       # these email1 and name1 are assigning to init variables email and name
        return cls(name1, email1)
    
    def display(self):
        print(self.name, self.email, example3.mobile_number)

print(example3.mobile_number)   # we can directly access the class level variables using class name without any object

obj3 = example3.details("sardar", "sardar@123")
print(30*'*')
obj3.display()    # we will get the mobile number as well

print(30*'*')
obj4 = example3.change_mobile(123456)
obj3.display()    # we will get the updated above mobile number


# with init obj and class method
class example5:

    mobile_number = 7383787

    def __init__(self, name, email):
        self.name = name
        self.email = email

    @classmethod
    def change_mobile(cls, mobile):             # changing the mobile number
        cls.mobile_number = mobile
    
    @classmethod                               # decorating it as class method so that we can pass input to the class
    def details(cls, name1 , email1):       # these email1 and name1 are assigning to init variables email and name
        return cls(name1, email1)
    
    def display(self):
        print(self.name, self.email, example3.mobile_number)


obj5 = example5("ravi", "ravi@gmail.com")
obj5.display()  # we will above details as it is ravi

print(30*'*')

obj5.details("venkat", "venkat@gmail.com")
obj5.display()      # still we get ravi details only
print(30*'*')


# creating an external method
def course_details(cls, course):
    print("this course details are", course)

# now i want to add this above method to example5 class

example5.course_details = classmethod(course_details)
example5.course_details("dev")      # with class method
print(30*'*')

obj6 = example5("bedi", "bedi@gmail.com")
obj6.course_details("prod")         # with object refernce


# if i want to delete any variable from class then
del example5.mobile_number


# if try to access will get error type object 'example5' has no attribute 'mobile_number'
del example5.mobile_number

# if delete the method then
delattr(example5, "details")

# get error 'example5' object has no attribute 'details'
obj6.details()

