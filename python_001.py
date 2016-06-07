#coding=utf-8
import random
import string
def growninto():
    number=[]
    for x in range(6):
        change=random.randint(65,122)
        if(change%2==0):
                number.append(chr(change))
                
        else:
            newchange=str(change%10)
            number.append(newchange)
    print(number)
    newnumber=('').join(number)
    print(newnumber)
growninto()        
