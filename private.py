class Myclass:
    __privVar = 82983
    
    def __privmethod(self):
        print("I am a PRIVATE method")
        
    def hello(self):
        print(f"The value of private variable is: {Myclass.__privVar}")
        self.__privmethod()
        
object= Myclass()

#print(object.__privVar)
object.hello()
#object.__privmethod()