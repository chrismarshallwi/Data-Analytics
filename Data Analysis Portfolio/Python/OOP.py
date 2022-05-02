class Computer():

    retreivalMethod = 'Writing.../-'
    cachingAbility = True

    def __init__(self, os, ram, hardrive, processor, keyboard):

        self.os = os
        self.ram = ram 
        self.hardrive = hardrive
        self.processor = processor
        self.keyboard = keyboard

# remember that methods are things that the class (Computer in this case), can do

    def storeData(self):
        print('Retreiving Data...: ')
        return Computer.retreivalMethod

    def retreiveData(self):
        print('a computer matches words in query against a DB index: ')
        print('retreival speed...: ')
        return (self.ram + self.hardrive) / (self.processor)

    def processData(self):
        print('The current process method speed is: ')
        return self.hardrive / self.processor

iMac = Computer('Monterey',8,256,52,True)
surface = Computer('Windows 10',16,512,26,False)
macbook = Computer('Catalina',16,256, 12, True)
surfacebook = Computer('Windows 10',8,512,16,False)

# inheritance for above class

class Laptop(Computer):
    def mobility(self):
        print('Laptops are mobile')

class Desktop(Computer):
    def immobility(self):
        print('Desktops are not mobile')

macbook = Laptop(os='Catalina',ram=16,hardrive=256,processor=12,keyboard=True)
surfacebook = Laptop(os='Windows 10',ram=16,hardrive = 512, processor = 16, keyboard = True)
iMac = Desktop(os='Monterey',ram=8,hardrive=512,processor=16,keyboard=False)
surface = Desktop(os='Windows 11', ram=16, hardrive=256,processor=9,keyboard=True)

print(surfacebook.os,surface.os, macbook.processData(),macbook.retreiveData())


















    







    


















    