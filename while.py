number = 9
guess_count = 3

# while loop also has optional else statement
while guess_count > 0:
    num = int(input("Guess:"))
    if num == number:
        print("You Won!")
        is_Guess = True
        break
    guess_count -= 1
else:
    print("Sorry, you Lost!")

# car game
is_started = False
is_stopped = False
while True:
    command = input().lower()
    if command == 'start':
        if not is_started:
            print(' Ready to go ...')
            is_started = True
            is_stopped = False
        else:
            print('car already started')
    elif command == 'stop':
        if not is_stopped:
            print('car has stopped!')
            is_stopped = True
            is_started = False
        else:
            print('car already stopped')

    elif command == 'help':
        print('''
start: to start the car
stop: to stop the car
quit: to quit the game''')
    elif command == 'quit':
        break

    else:
        print("I don't know this...")
