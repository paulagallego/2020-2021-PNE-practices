#Function for calculating the sum of the N first integer numbers

def sumn(n):
    res = 0
    for i in range(1, n+1):
        res += i
    return res

#the main program starts here
print('sum of the 20 first integers: ', sumn(20))
print('sum of the 100 first integers: ', sumn(100))