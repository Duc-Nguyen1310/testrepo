import random

def generate_password(length = 12, uppercase = True, lowercase = True, digits = True, specialchar = True):
    char_pool = ''
    if uppercase:
        char_pool += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if lowercase:
        char_pool += 'abcdefghijklmnopqrstuvwxyz'
    if digits:
        char_pool += '0123456789'
    if specialchar:
        char_pool += '!@#$%^&*()-_+='
    if not char_pool:
        raise ValueError('At least one character type must be selected.')
    password = ''.join(random.choice(char_pool) for _ in range(int(length)))
    return password

if __name__ == "__main__":
    length = input('Enter password length: ')
    if not length.isdigit():
        print('Please enter a valid number for length.')
        exit()
    elif int(length) < 4:
        print('Password length must be at least 4.')
        exit()
    elif int(length) > 100:
        print('Password length must not exceed 100.')
        exit()
    uppercase_choice = input('Include uppercase letters? (y/n): ').lower() == 'y'
    lowercase_choice = input('Include lowercase letters? (y/n): ').lower() == 'y'
    digits_choice = input('Include digits? (y/n): ').lower() == 'y'
    specialchar_choice = input('Include special characters? (y/n): ').lower() == 'y'
    
    password = generate_password(length, uppercase_choice, lowercase_choice, digits_choice, specialchar_choice)
    print(f'Generated Password: {password}')
    