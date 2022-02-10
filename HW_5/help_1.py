def help_actions():
    print('You can choose actions from: create, read_user, read_all, update, delete.')
    print()
    while True:
        action = input('If you want to get help on any command, enter its '
                       'name or the first letter of the name, otherwise enter "quit": ')
        if action == 'create' or action == 'c':
            print("Allows you to create a new user. You will need to enter your email, name, password and phone.")
            print()
        elif action == 'read_user' or action == 'ru':
            print("Allows you to view information about a specific user. You will need to enter email.")
            print()
        elif action == 'read_all' or action == 'ra':
            print("Allows you to view information about all users.")
            print()
        elif action == 'update' or action == 'u':
            print("Allows you to update your personal information. You will need to enter your email "
                  "and choose, which information needs to updated.")
            print()
        elif action == 'delete' or action == 'd':
            print("Allows you to delete your account. You will need to enter email.")
            print()
        elif action == 'quit':
            break
        else:
            print("We don't know this command")

