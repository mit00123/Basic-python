class car:
    def __init__(self,modelname,year):
        self.model=modelname
        self.year=year
    def display(self):
        print(self.model,self.year)   
c1=car("xuv",2000)
c1.display()


