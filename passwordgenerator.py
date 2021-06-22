base = input('Enter the password base: ')
password = ''
for letter in base:
    if letter in 'Ee':
        password += '@'
    elif letter in 'Aa':
        password += '#'
    elif letter in 'Rr':
        password += '1'
    elif letter in 'Ii':
        password += '9'
    elif letter in 'Oo':
        password += '8'
    elif letter in 'Tt':
        password += '4'
    elif letter in 'Nn':
        password += '?'
    elif letter in 'Ss':
        password += '!'
    else:
        password += letter

print(password)
