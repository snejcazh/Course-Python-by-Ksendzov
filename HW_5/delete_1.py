def user_delete(user_emails, users_storage):
    email = input('Enter email, which needs to deleted: ')

    if email in user_emails:
        user_emails.remove(email)
        del users_storage[email]

        print(f'You deleted user {email} from our database')

    else:
        print(f'User with email {email} is not in our database')
