import string
import random
import os
def generate_password(length, options):
    char = ''
    for option in options:
        if option == 'upper':
            char += string.ascii_uppercase
        elif option == 'lower':
            char += string.ascii_lowercase
        elif option == 'numbers':
            char += string.digits
        elif option == 'symbols':
            char += "!;#$%&()*+,-./:;<=>?@[]^_`{|}~"
    
    if char == '':
        return "Invalid options selected. Please try again."
    
    password = ''.join(random.choice(char) for _ in range(length))
    
    dir_path = os.path.dirname(os.path.realpath('History.txt'))
    if not os.path.exists(dir_path):
        with open('History.txt', 'x'):
            pass
    with open('History.txt', 'a') as f:
        f.write(password + '\n')
    
    return password

options_dict = {
    1: ['upper', 'lower'],
    2: ['upper', 'lower', 'numbers'],
    3: ['upper', 'lower', 'numbers', 'symbols'],
    4: ['upper', 'lower', 'symbols'],
    5: ['upper'],
    6: ['upper', 'numbers'],
    7: ['upper', 'numbers', 'symbols'],
    8: ['upper', 'symbols'],
    9: ['lower'],
    10: ['lower', 'numbers'],
    11: ['lower', 'numbers', 'symbols'],
    12: ['lower', 'symbols'],
    13: ['numbers'],
    14: ['symbols']
}

print('----------------------------')
print('Select an option:')
print('1. Upper and Lowercase letters')
print('2. Upper and Lowercase letters with Numbers')
print('3. Upper and Lowercase letters with Numbers and Symbols')
print('4. Upper and Lowercase letters with Symbols')
print('5. Uppercase letters only')
print('6. Uppercase letters with Numbers')
print('7. Uppercase letters with Numbers and Symbols')
print('8. Uppercase letters with Symbols only')
print('9. Lowercase letters only')
print('10. Lowercase letters with Numbers')
print('11. Lowercase letters with Numbers and Symbols')
print('12. Lowercase letters with Symbols only')
print('13. Symbols only')
print('14. Numbers only')
print('----------------------------')

while True:
    option = int(input('Enter the option number: '))
    if option in options_dict:
        break
    else:
        print('Invalid option. Please try again.')

password_length = int(input('Enter the length of the password: '))

password = generate_password(password_length, options_dict[option])
print('Your password is:', password)

