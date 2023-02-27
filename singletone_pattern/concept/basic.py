# class Singleton(object):
#   __unique_instance = None
#   def __new__(cls, *args, **kwargs):
#     if not isinstance(cls.__unique_instance, cls):
#         cls.__unique_instance = object.__new__(cls, *args, **kwargs)
#     return cls.__unique_instance

# class BaseClass():
#     pass

# class MyClass(Singleton, BaseClass):
#   pass

# class Test():
#     pass

# if __name__ == "__main__":
#   s1 = MyClass()
#   s2 = MyClass()
  
#   t1 = Test()
#   t2 = Test()
  
#   print("t1 == t2", t1 is t2)
#   print("s1 == s2", s1 is s2)
#   print(id(s1) == id(s2))
#   print(id(t1) == id(t2))
#   print("s1 = ", s1)
#   print("s2 = ", s2)
#   print("t1 =", t1)
#   print("t2 =", t2)

class Singleton(object):
  __unique_instance = None
  def __new__(cls, *args, **kwargs):
    if not isinstance(cls.__unique_instance, cls):
        cls.__unique_instance = object.__new__(cls, *args, **kwargs)
    return cls.__unique_instance

class ChocolateBoiler(Singleton):
    __empty = True
    __boiled = False
    
    def fill(self):
        if self.is_empty():
            self.__empty = False
            self.__boiled = False
    
    def drain(self):
        if not self.is_empty() and self.is_boiled():
           self.__empty = True 
    
    def boil(self):
        if not self.is_empty() and not self.is_boiled():
            self.__boiled = True
    
    def is_empty(self):
        return self.__empty
     
    def is_boiled(self):
        return self.__boiled

if __name__ == "__main__":
	s1 = ChocolateBoiler()
	s2 = ChocolateBoiler()
	
	print("is empty ? ", s2.is_empty())
	s1.fill()
	print("is empty ? ", s2.is_empty())