def user_info(email, user_emails, users_storage):
    if email in user_emails:
        message = f'User_email = {email}, \n' \
                  f'User_info: {users_storage[email]}'

    else:
        message = f'No user with email: {email}'

    return message


def all_users_info(users_storage):

    if not users_storage:
        print("At the moment the database is empty")

    else:
        for k, v in users_storage.items():

            user_email = 'User_email: ' + k
            user_info_1 = 'User_info', v

            print(user_email, '\n', *user_info_1)