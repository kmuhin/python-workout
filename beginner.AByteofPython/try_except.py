try:
    text=input('Enter something: ')
except EOFError:
    print('Why did you make EOF?')
except KeyboardInterrupt:
    print('You canceled operation.')
else:
    print(f'You entered {text}')

