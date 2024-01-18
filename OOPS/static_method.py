# static methods are used for memory optimization 
# normal method
class example1:

    def display(self, name, email):
        print(name, email)


o1 = example1()
o1.display("pavan", "pavan@gmail.com")


# now lets try with static method
class example2:

    def display(self, name, email):
        print(name, email)

    @staticmethod
    def mentors(menor_list):
        print(menor_list)

    def mentors_list(self, list):
        print(list)

print(30*'*')
o2 = example2()
o2.mentors_list(["pavan", "prashanth"])
o2.mentors(["ravi", "sardar"])              # with object ref we can call static method

example2.mentors(["pavan", "prashanth"])


# now lets try with class method
class example3:

    def display(self, name, email):
        print(name, email)
        example3.mentors(["cap", "tcs"])      #  access static method here

    @classmethod
    def class_method(cls, mentor_list):
        print(mentor_list)

    @staticmethod
    def mentors(mentor_list):
        print(mentor_list)
        example3.class_method(["abc","xyz"])

    def mentors_list(self, list):
        print(list)
        example3.mentors(["ravi", "sardar"])              # accesing sttaic method in normal method

print(30*'*')

example3.class_method(["venkat", "varun"])        # accessing class method
example3.mentors(["pavan", "prashanth"])

o3 = example3()

o3.mentors_list(["manjul", "satya"])
o3.display("pavan", "pavan@gmail.com")