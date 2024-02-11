import os
import random
import string

class PasswordGenerator:
    def __init__(self):
        self.options_dict = self.Options_Dict()
        self.dir_path = self.path()

    def Options_Dict(self):
        options_dict = {
            1: ['lower'],
            2: ['numbers'],
            3: ['symbols'],
            4: ['upper'],
            5: ['upper', 'lower'],
            6: ['upper', 'numbers'],
            7: ['upper', 'symbols'],
            8: ['upper', 'lower', 'numbers'],
            9: ['upper', 'lower', 'symbols'],
            10: ['upper', 'numbers', 'symbols'],
            11: ['upper', 'lower', 'numbers', 'symbols'],
            12: ['lower', 'numbers'],
            13: ['lower', 'symbols'],
            14: ['lower', 'numbers', 'symbols'],
            }
        return options_dict
    
    def Print_Options(self):
        print('----------------------------')
        print('Select what you prefer to be in your password:')
        print('1. LowerCase letters only')
        print('2. Numbers only ')
        print('3. Symbols only')
        print('4. UpperCase letters only')
        print('5. UpperCase with LowerCase letters')
        print('6. UpperCase letters with Numbers')
        print('7. Uppercase letters with Symbols')
        print('8. Uppercase and LowerCase letters with Numbers')
        print('9. Uppercase and LowerCase letters with Symbols')
        print('10. Uppercase letters with Symbols and Numbers')
        print('11. Uppercase and LowerCase letters with Symbols and Numbers')
        print('12. LowerCase letters with Numbers')
        print('13. LowerCase letters with Symbols')
        print('14. LowerCase letters with Numbers and Symbols')
        print('----------------------------')
    def option_selected(self):
        while True:
            try:
                option = int(input('Enter the option number: '))
                if option in self.options_dict:
                    return option
                else:
                    print('Invalid option. Please try again.')
            except ValueError:
                print("Please enter a valid number.")

    def password_length_input(self):
        while True:
            try:
                password_length = int(input('Enter the length of the password: '))
                if  4 <= password_length <=  256:
                    return password_length
                else:
                    print('Type a number between  4 and  256')
            except ValueError:
                print("Please enter a valid number.")

    def password_generation_function(self, length, options):
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
        return password


    def path(self):
        dir_path = os.path.dirname(os.path.realpath('History.txt'))
        return dir_path

    def CreateHistoryFile(self):
        if not os.path.exists(self.dir_path):
            with open('History.txt', 'x'):
                pass

    def AddPasswordInText(self, password):
        with open('History.txt', 'a') as f:
            f.write(password + '\n')

    def run(self):
        self.Print_Options()
        option = self.option_selected()
        length = self.password_length_input()
        password = self.password_generation_function(length, self.options_dict[option])
        print('Your password is:', password)
        self.CreateHistoryFile()
        self.AddPasswordInText(password)
        with open('History.txt', 'r') as generated_passwords:
            print('you have generated', len(generated_passwords.readlines()), 'passwords')

generator = PasswordGenerator()
generator.run()

