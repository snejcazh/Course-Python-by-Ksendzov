# HW по Python CRUD
#
# Доделать то, что начали на занятии по CRUD
# На занятии мы сделали Create, Read
# Теперь надо доделать Update, Delete.
#
#  1. Сделать функционал для проверки уникальности Email (существует ли такой пользователь) перед добавлением нового пользователя.
#  2. Добавить возможность обновления информации о существующем пользователе.
#  3. Добавить возможность удалить существующего пользователя
#  4. Сделать -- Help для просмотра списка возможных команд с комментариями к ним
#
# Постарайтесь всё сделать через функции.

from create_1 import create_user
from read_1 import user_info, all_users_info
from update_1 import user_update
from delete_1 import user_delete
from help_1 import  help_actions

user_emails = []
users_storage = {}

while True:
    action = input('Please enter action or help to view possible actions: ')

    if action == 'help':
        help_actions()

    elif action == 'create':
        print('action = ', action)

        email = input('Email: ')
        if email in user_emails:
            print('This email is already in our database')
        else:
            name = input('Name: ')
            password = input('Password: ')
            phone = input('Phone: ')

            create_user(email, name, password,
                        phone, user_emails, users_storage)

#            print('user_emails = ', user_emails)
#            print('users_storage = ', users_storage)

    elif action == 'read_all':
        print('action = ', action)
        all_users_info(users_storage)

    elif action == 'read_user':

        user_e = input('Enter user email ')
        message = user_info(user_e, user_emails, users_storage)

        print('action = ', action)
        print('User: ', message)

    elif action == 'update':
        print('action = ', action)
        user_update(user_emails, users_storage)

    elif action == 'delete':
        print('action = ', action)
        user_delete(user_emails, users_storage)

    else:
        print("We don't know such action.")




