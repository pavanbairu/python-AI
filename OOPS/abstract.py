
# abstract method does not contain any body. the imported class should provide its implementation based on their requirement
import abc    # for abstract class
class abstract_class:

    @abc.abstractmethod     # decorating it as abstract method
    def name(self):
        pass

    @abc.abstractmethod
    def mobile(self):
        pass
    
    @abc.abstractmethod
    def address(self):
        pass
    
    @abc.abstractmethod
    def id(self):          # the implementation is not provided for this method in imported classes
        pass

# student_details class implementing the abstract class methods
class student_details(abstract_class):

    # providing the implementations for the methods of an abstract class
    def name(self):
        print("student name is pavan")

    def mobile(self):
        print("student mobile is 12345")

    def address(self):
        print("student address is hyd")


# employee_details class implementing the abstract class methods
class employee_details(abstract_class):

    # providing the implementations for the methods of an abstract class
    def name(self):
        print("employee name is prashanth")

    def mobile(self):
        print("employee mobile is 987654321")

    def address(self):
        print("employee address is wgl")

# created the object for student class and calling the methods
s1 = student_details()
s1.mobile()
s1.name()
s1.address()

# created the object for employee class and calling the methods
e1 = employee_details()
e1.name()
e1.mobile()
e1.address()