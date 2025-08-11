class car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def say_hi(self):
        print('car make is', self.make)
        print('car model name is', self.model)
        print('car making year is', self.year)

p = car('Kia.','Seltos.',2007)  
p1 = car('kia','Sonet',2008) 
p.say_hi()
print('\n')
p1.say_hi()