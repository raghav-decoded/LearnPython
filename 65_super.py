'''
Instance variable in child class
Instance variable in parent class
Class variable in child class
Class variable in parent class

class Parent_Class(object):
      def __init__(self):
            pass

class Child_Class(Parent_Class):
     def __init__(self):
           super().__init__()
'''

class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "Special"

class B(A):
    classvar1 = "I am in class B"

    def __init__(self):
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance var in class B"
        # super().__init__()
        # print(super().classvar1)


a = A()
b = B()

print(b.special, b.var1, b.classvar1)
