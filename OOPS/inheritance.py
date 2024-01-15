# example of multilevel inheritance
class example1:

    def test1(self):
        print("this is test1 from example1")

    
class example2(example1):       # inheriting the example1 class properties

    def test2(self):
        print("this is test2 from example2")


class example3(example2):         # inheriting the example2 class properties

    def test3(self):
        print("this is test3 from example3")


ex3 = example3()
ex3.test1()         # with object of example3 class. we can access test1 from class1
ex3.test2()         # with object of example3 class. we can access test2 from class2
ex3.test3()


# example of multiple inheritance

class sample1:

    def dummy1(self):
        print("this is dummy1 from sample1 class")

    def test(self):
        print("this is test method from sample1 class")


class sample2: 

    def dummy2(self):
        print("this is dummy2 from sample2 class")

    def test(self):
        print("this is test method from sample2 class")


class sample3(sample1, sample2):  # inherting the sample1 and sample2 classes in sample3 class

    def dummy3(self):
        print("this is dummy3 from sample3 class")


s3 = sample3()
s3.dummy1()     # with object of sample3 class. we can access dummy1 from sample1
s3.dummy2()    # with object of sample3 class. we can access dummy2 from sample2
s3.dummy3()
s3.test()      # method is available in both sample1 and sample2 classes