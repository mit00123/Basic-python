class p:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name,self.age)    
class q(p):
    def show(self):
        print("harsh")
a=q("amit",18)
b=p("k",20)     
b.display()
a.display()
a.show()   