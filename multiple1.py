class a:
    def speak(self):
        print("a is speak")
class b():  
    def tell(self):
        print("b is speaking")  
    
class c(a,b):
    def said(self):
        print("c is speaking") 
c1=c()
c1.speak()
c1.tell()
c1.said()   
print((issubclass(c,b)))    
print((issubclass(a,b))) 
print((issubclass(b,a))) 
print("*******************************")
print(isinstance(c1,b)) ##c1=object b=subclass