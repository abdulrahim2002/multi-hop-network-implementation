import os

# list of valid users
valid_users = {
    # username: pin
    "machine 1": '1234',
    "machine 2": '1234',
    "machine 3": '1234',
    "machine 4": '1234'
}

def printUI():
    print('\nABDUL RAHIM(C)--Machine\n'
          'Press 1 to login as machine 1\n'
          'Press 2 to login as machine 2\n'
          'Press 3 to login as machine 3\n'
          'Press 4 to login as machine 4\n'
          'Press 5 to EXIT'
          )

def authenticate(username):
    pin = input('Enter pin: ')
    if username in valid_users and pin == valid_users[username]:
        return True
    return False

def machine1():
    # login to the server
    # ask server the IP address of the next
    # fire machine 1 code
    print('Machine 1')
    os.system('clientm1.bat')

def machine2():
    # login to the server
    # ask server the IP address of the next
    print('Machine 2')
    os.system('clientm2.bat')

def machine3():
    # login to the server
    # ask server the IP address of the next
    print('Machine 3')
    os.system('clientm3.bat')

def machine4():
    # login to the server
    # ask server the IP address of the next
    print('Machine 4')
    os.system('serverm4.bat')

def main():
    printUI()
    choice = input('Enter choice: ')

    if choice == '1'   and authenticate('machine 1'):
        machine1()
    elif choice == '2' and authenticate('machine 2'):
        machine2()
    elif choice == '3' and authenticate('machine 3'):
        machine3()
    elif choice == '4' and authenticate('machine 4'):
        machine4()
    elif choice == '5':
        print('Exiting...')
        exit()
    else:
        print('Incorrect PIN or Invalid choice')
        main()


if __name__ == '__main__':
    main()