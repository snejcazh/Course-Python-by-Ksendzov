from create_1 import email_validate, name_validate, password_validate, phone_validate


def user_update(user_emails, users_storage):
    user_for_update = input("Enter user's email: ")
    if user_for_update in user_emails:
        temp = "yes"
        while temp == "yes":
            item_for_update = input("Enter, which item needs to be updated: email, name, password or phone: ")

            if item_for_update == 'email':
                user_for_update = update_email(user_for_update, user_emails, users_storage)

            elif item_for_update == 'name':
                update_name(user_for_update, users_storage)

            elif item_for_update == 'password':
                update_password(user_for_update, users_storage)

            elif item_for_update == 'phone':
                update_phone(user_for_update, users_storage)

            else:
                print("We don't know such action.")
                continue

            temp = input("Do you want to update something else? Write 'yes' or 'no' ")
    else:
        print(f'User with email {user_for_update} is not in our database')


def update_email(email, user_emails, users_storage):
    new_email = input('Enter new email: ')

    new_email = email_validate(new_email)
    user_emails[user_emails.index(email)] = new_email
    users_storage[new_email] = users_storage.pop(email)

    print(f'You updated email from {email} to {new_email}')
    return new_email


def update_name(email, users_storage):
    new_name = input('Enter new name: ')

    new_name = name_validate(new_name)
    print(f'You updated name from {users_storage[email]["name"]} to {new_name}')
    users_storage[email]['name'] = new_name


def update_password(email, users_storage):
    new_password = input('Enter new password: ')

    new_password = password_validate(new_password)
    print(f'The password has been changed')
    users_storage[email]["password"] = new_password


def update_phone(email, users_storage):
    new_phone = input('Enter new phone: ')

    new_phone = phone_validate(new_phone)
    print(f'You updated phone from {users_storage[email]["phone"]} to {new_phone}')
    users_storage[email]["phone"] = new_phone
