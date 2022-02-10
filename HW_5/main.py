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

print("Hello! To interact with our application, you can use the following commands: \n"
      "create, read_user, read_all, update, delete, help (to view possible actions) or quit (to close the program). \n"
      "For quick access you can enter the first letters of the commands: c, ru, ra, u, d, h, q.")
while True:
    action = input('Please enter action: ')

    if action == 'help' or action == 'h':
        help_actions()

    elif action == 'create' or action == 'c':
        print('action = create')

        create_user(user_emails, users_storage)

    elif action == 'read_all' or action == 'ra':
        print('action = read_all')
        all_users_info(users_storage)

    elif action == 'read_user' or action == 'ru':

        user_e = input('Enter user email ')
        message = user_info(user_e, user_emails, users_storage)

        print('action = read_user')
        print('User: ', message)

    elif action == 'update' or action == 'u':
        print('action = update')
        user_update(user_emails, users_storage)

    elif action == 'delete' or action == 'd':
        print('action = delete')
        user_delete(user_emails, users_storage)

    elif action == 'quit' or action == 'q':
        break

    else:
        print("We don't know such action.")




