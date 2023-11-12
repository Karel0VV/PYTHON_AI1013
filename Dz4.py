class BaseClass:
   def __init__(self, base_attr):
       self.base_attr = base_attr
   def base_method(self):

       print("метод базового класу")
class ChildClass1(BaseClass):
   def __init__(self, base_attr, child1_attr):

       super().__init__(base_attr)

       self.child1_attr = child1_attr
   def child1_method(self):

       print("метод першого дочірнього класу")
class ChildClass2(BaseClass):

   def __init__(self, base_attr, child2_attr):

       super().__init__(base_attr)

       self.child2_attr = child2_attr

def child2_method(self):
    print("метод другого дочірнього класу")