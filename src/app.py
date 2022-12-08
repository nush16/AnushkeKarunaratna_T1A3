import time

# Menu options
menu_options = ('h', 'x', 's')

while True:
    print()
    print('Menu')
    print('h = help')
    print('x = exit')
    print('s = start')

    print()
    user_input = input('Enter an option: ')

    if user_input in menu_options:
        break

    else:
        print()
        print('option not available')


