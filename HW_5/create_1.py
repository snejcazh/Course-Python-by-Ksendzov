import re


# def create_user(email, name, password, phone, user_emails, users_storage):
#
#     user_info = [email, name, password, phone]
#     user_emails.append(email)
#     users_storage[email] = {'name': name, 'password': password, 'phone': phone}
#
#     print(user_info)
#     return None


def create_user(user_emails, users_storage):

    email = input('Email: ')
    if email in user_emails:
        print('This email is already in our database')
    else:
        email_validate(email)

        name = input('Name: ')
        name_validate(name)

        password = input('Password: ')
        password_validate(password)

        phone = input('Phone: ')
        phone_validate(phone)

        user_info = [email, name, password, phone]
        user_emails.append(email)
        users_storage[email] = {'name': name, 'password': password, 'phone': phone}

        print('New user:', user_info)
        return None


def email_validate(email):
    while True:
        if email == '':
            email = input('This field should not be empty. Please enter Email: ')
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            email = input('The value is incorrectly. Please enter Email: ')
        else:
            return email


def name_validate(name):
    while True:
        if name == '':
            name = input('This field should not be empty. Please enter your name: ')
        elif len(name) > 16:
            name = input('The value is too long. Please enter your name: ')
        elif not re.match(r"^[a-zA-Z]+$", name):
            name = input('The value is incorrectly. Please enter name: ')
        else:
            return name


def password_validate(password):
    while True:
        if len(password) < 8 or len(password) >= 30:
            password = input("Make sure your password is at lest 8 letters and less than 30. "
                             "Please enter a correct password: ")
        elif re.search('[0-9]',password) is None:
            password = input("Make sure your password has a number in it. Please enter a correct password: ")
        elif re.search('[A-Z]',password) is None:
            password = input("Make sure your password has a capital letter in it. Please enter a correct password: ")
        elif re.search('[a-z]',password) is None:
            password = input("Make sure your password has a lowercase letter in it. Please enter a correct password: ")
        else:
            return password


def phone_validate(phone):
    while True:
        if not re.match(r'^\+7[0-9]{10}$', phone):
            phone = input('The value is incorrectly. Please enter phone: ')
        else:
            return phone
