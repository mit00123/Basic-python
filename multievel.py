class a:
    def speak(self):
        print("a is speak")
class b(a):  
    def tell(self):
        print("b is speaking")  
    
class c(a):
    def said(self):
        print("c is speaking") 
c1=c()
c1.speak()
c1.tell()
c1.said()               