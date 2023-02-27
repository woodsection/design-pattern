from threading import Thread

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
	s1 = Thread(ChocolateBoiler())
	s2 = Thread(ChocolateBoiler())
	
    # print(s1)
    # print(s2)
	# print("is empty ? ", s2.is_empty())
	# s1.fill()
	# print("is empty ? ", s2.is_empty())