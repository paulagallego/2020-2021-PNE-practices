#import Seq0
class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        #Initialize the sequence with the value passed as argument when creating the object
        self.strbases = strbases
        if self.is_valid_sequence():
            print('New sequence created!')
        else:
            self.strbases = 'Error'
            print('INCORRECT sequence detected')
        #another way of doing is_valid_sequence_2:
                #Add the function to seq0
            #if Seq0.is_valid_sequence(strbases):
                #print('New sequence created')
                #self.strbases = strbases
    #the order of the functions inside the class isnt relevant
    #@staticmethod
    #def print_text(text): #we create a method inside the class but it does not require the method to work. #static functions don't need the 'self' attribute
        #here we can add any code but anything related to the class attribute
        #print(text)
    def is_valid_sequence(self): #if we need the class attributes to work with this function, we need to add 'self' as an argument of the function
        for i in self.strbases:
            if i != 'A' and i !='C' and i != 'G' and i != 'T':
                return False
        return True
        #print(self.strbases)
    #def static_function(): #static functions don't need the 'self' attribute
    @staticmethod
    def is_valid_sequence_2(bases):
        for i in strbases:
            if i != 'A' and i !='C' and i != 'G' and i != 'T':
                return False
        return True

    def __str__(self):
        """Method called when the object is being printed"""
        #-- We just return the string with the sequence
        return self.strbases
    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)
class Gene(Seq):
    """This class is derived from the Seq Class
        All the objects of class Gene will inherit
        the methods from the Seq class
    """
    def __init__(self, strbases, name=""):
        #--Call first the Seq initilizer and then the
        #--Gene init method
        super().__init__(strbases)
        self.name = name
        print('New gene created')
    def __str__(self):
        """Print the Gene name along with the sequence"""
        return self.name + "-" + self.strbases
#Main program
#Create an object of the Class Seq
s1 = Seq('AGTACACTGGT') #this elem has a determinate 'self', which is unique to it (p.e. g will have a different 'self')
#Create another object of the Class Seq
#g = Gene('CGTAAC', 'FRAT1')
s2 =  Seq('ERRPS')

#-- Printing the objects
print(f'Sequence 1: {s1}')
#print(f'Length: {s1.len()}')
print(f'Sequence 2: {s2}')
#print(f'Length: {g.len()}')
#print('Testing...')
#s1.print_bases() #when using class methods, we write the name of the instance of the class (s1) followed by the function we wanna use
#Seq.static_function('Hello')#when using static methods, we directly write the class(Seq)
#if the function we want to use only implies elem of a given class, we place it inside that class
#however, if that function uses elem of several classes, we should place it in the Seq0 (general functions place)