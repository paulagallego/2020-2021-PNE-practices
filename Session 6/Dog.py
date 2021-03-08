class Dog:
    def __init__(self, the_name, the_age): #will create an instance of the class, whenever you choose a class Dog element, will firstly execute the init function (called 'constructor')
        self.name = the_name #class atributes
        self.age = the_age

    def set_name(self, name):
        self.name = name
        print('This is {}, and I am sitting down here'.format(self.name))
    def set_age(self, the_age):
        self.age = the_age
    def rollover(self):
        pass
    def sitdown(self):
        print('Yes, i will sit down')
    #def jump(self):
        #print('Yes, i will jump') # if not added, the dog wont jump
    #pass
    #self: when we create a function inside the class it is necessary, it's a handeler of the object (refers to the specific object)

ares = Dog.sitdown()
ares = Dog('ares', 10) #one object belonging to the class 'Dog'#number stands for age
#print(ares)
toby = Dog('toby', 21)
#pass
#print toby
ares.set_name('trueno') #now we can access the info inside ares obj and change it
ares.set_age(10)
ares.rollover()

#ares = toby
#black = Dog('toby', 21)
#black.name = 'troy'
#print('toby is ares')
#pass # used for the debugger, just to be able to debug with redpoint in toby = dog