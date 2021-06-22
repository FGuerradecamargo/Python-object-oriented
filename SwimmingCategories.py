print('-' * 20)
print('Swimming Categories'.center(20))
print('-' * 20)
while True:
    age = int(input('Enter your age: '))
    if 5 <= age <= 7:
        print('Childish A')
        break
    elif 8 <= age <= 10:
        print('Childish B')
        break
    elif 11 <= age <= 13:
        print('Juvenile A')
        break
    elif 14 <= age <= 17:
        print('Juvenile B')
        break
    else:
        print('Enter a valid between 5 and 17!')
        print('-' * 20)
