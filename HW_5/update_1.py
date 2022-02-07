def user_update(user_emails, users_storage):
    user_for_update = input("Enter user's' email ")
    item_for_update = input("Enter, which item needs to be updated: email, name, password or phone ")

    if item_for_update == 'email':
        update_email(user_for_update, user_emails, users_storage)

    elif item_for_update == 'name':
        update_name(user_for_update, users_storage)

    elif item_for_update == 'password':
        update_password(user_for_update, users_storage)

    elif item_for_update == 'phone':
        update_phone(user_for_update, users_storage)


def update_email(email, user_emails, users_storage):
    new_email = input('Enter new email: ')

    user_emails[user_emails.index(email)] = new_email
    users_storage[new_email] = users_storage.pop(email)

    print(f'You updated email from {email} to {new_email}')


def update_name(email, users_storage):
    new_name = input('Enter new name: ')

    print(f'You updated name from {users_storage[email]["name"]} to {new_name}')
    users_storage[email]['name'] = new_name


def update_password(email, users_storage):
    new_password = input('Enter new password: ')

    print(f'You updated name from {users_storage[email]["password"]} to {new_password}')
    users_storage[email]["password"] = new_password


def update_phone(email, users_storage):
    new_phone = input('Enter new password: ')

    print(f'You updated name from {users_storage[email]["phone"]} to {new_phone}')
    users_storage[email]["phone"] = new_phone
