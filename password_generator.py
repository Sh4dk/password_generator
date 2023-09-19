import random
import string
#==========================================================================================
def grs1(length): #gsr = generate random string 
    char = string.ascii_letters #char = character
    rs = ''.join(random.choice(char) for _ in range(length)) #rs = random string
    print('---------------------------------------------------')
    print('your password is: ',end='')
    return rs #UpperLower case letters only password
#==========================================================================================
def grs2(length): 
    char = string.ascii_letters + string.digits
    rs = ''.join(random.choice(char) for _ in range(length))
    print('---------------------------------------------------')
    print('your password is: ',end='')
    return rs #UpperLower case letters + numbers 
#==========================================================================================
def grs3(length):
    char = string.ascii_letters + string.digits +"!;#$%&()*+,-./:;<=>?@[]^_`{|}~"
    rs = ''.join(random.choice(char) for _ in range(length))
    print('---------------------------------------------------')
    print('your password is: ',end='')
    return rs #UpperLower case letters + numbers + symbols
#==========================================================================================
def grs4(length):
    char = string.ascii_uppercase
    rs = ''.join(random.choice(char) for _ in range(length))
    print('---------------------------------------------------')
    print('your password is: ',end='')
    return rs #Uppercase letters only password
#==========================================================================================
def grs5(length):
    char = string.ascii_uppercase + string.digits
    rs = ''.join(random.choice(char) for _ in range(length))
    print('---------------------------------------------------')
    print('your password is: ',end='')
    return rs #Uppercase letters + numbers
#==========================================================================================
def grs6(length):
    char = string.ascii_uppercase + string.digits +"!;#$%&()*+,-./:;<=>?@[]^_`{|}~"
    rs = ''.join(random.choice(char) for _ in range(length))
    print('---------------------------------------------------')
    print('your password is: ',end='')
    return rs #Uppercase letters + numbers + symbols
#==========================================================================================
def grs7(length):
    char = string.ascii_lowercase 
    rs = ''.join(random.choice(char) for _ in range(length))
    print('---------------------------------------------------')
    print('your password is: ',end='')
    return rs #Lowercase letters only password
#==========================================================================================
def grs8(length):
    char = string.ascii_lowercase + string.digits 
    rs = ''.join(random.choice(char) for _ in range(length))
    print('---------------------------------------------------')
    print('your password is: ',end='')
    return rs #Lowercase letters + numbers password
#==========================================================================================
def grs9(length):
    char = string.ascii_lowercase + string.digits + "!;#$%&()*+,-./:;<=>?@[]^_`{|}~"
    rs = ''.join(random.choice(char) for _ in range(length))
    print('---------------------------------------------------')
    print('your password is: ',end='')
    return rs #Lowercase letters + numbers + symbols password
#==========================================================================================
while True:
    a=int(input('how many characters do you want your password to have:'))
    if (128>=a>=4):
        break
    else:
        print('Enter a number between 4 to 128')
numbers=input('do you want to have numbers in your password? (y,n)').lower()
symbols=input('do you want to have symbols in your password? (y,n)').lower()
Upper=input('do you want to have uppercase only letters in your password? (y,n)').lower()
while True:
    if (Upper=='y'):
        Lower='n'
        UpperLower='n'
        break
    elif(Upper!='y'):
        Lower=input('do you want to have lowercase only letters in your password? (y,n)').lower()
        if (Lower=='y'):
            Upper=='n'
            UpperLower='n'
            break
        elif(Lower!='y'):
            UpperLower=input('do you want to have upper and lowercase letters in your password?(y,n)').lower()
            if(UpperLower!='y'):
                print('invalid inputs')
#==========================================================================================
if (UpperLower=='y' and numbers!='y' and symbols!='y'):
    print(grs1(a))
    
if (UpperLower=='y' and numbers=='y' and symbols!='y'):
    print(grs2(a))
    
if (UpperLower=='y' and numbers=='y' and symbols=='y'):
    print(grs3(a))
    
if (Upper=='y' and numbers!='y' and symbols!='y'):
    print(grs4(a))

if (Upper=='y' and numbers=='y' and symbols!='y'):
    print(grs5(a))

if (Upper=='y' and numbers=='y' and symbols=='y'):
    print(grs6(a))
    
if (Lower=='y' and numbers!='y' and symbols!='y'):
    print(grs7(a))
    
if (Lower=='y' and numbers=='y' and symbols!='y'):
    print(grs8(a))

if (Lower=='y' and numbers=='y' and symbols=='y'):
    print(grs9(a))
    
    