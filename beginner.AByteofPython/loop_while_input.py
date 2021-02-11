number: int = 10
while True:
    guess: int = int(input('Enter number: '))
    if guess < 10:
        print('Number is less then need')
    elif guess > 10:
        print('Number is more then need')
    else:
        print('You guess, conceived number is: ')
        break


