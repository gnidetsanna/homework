import os
import json
import datetime
import Keys

file_of_users = '/Users/macuser/PycharmProjects/homework/Calculator/jj'


def start():
    first_answer = input('Are u a registrated user? T/F')
    if first_answer == 'T':
        auth()
    elif first_answer == 'F':
        second_answer = input('Do u want to registr? T/F')
        if second_answer == 'T':
            register()
        elif second_answer == 'F':
            calc_short()


def auth():
    def check_user_in_db(login, password):
        # nonlocal file
        with open(file_of_users, 'r') as users:
            list_users = json.load(users)
            for user in list_users:
                if user['login'] == login:
                    if user['password'] == password:
                        return True

            return False

    login = input('Please enter the login: ')
    password = input('Please enter the password: ')

    if check_user_in_db(login, password):
        print('Authorization successful')
        calc_long(login)
    else:
        third_answer = input('You are not in the database, do you want to registr? T/F')
        if third_answer == 'T':
            register()
        else:
            calc_short()


def check_pass(password, confirm_password):
    if password == confirm_password:
        FROM_A = ord('A')
        FROM_Z = ord('Z') + 1
        i = 0
        for letter in password:
            new_letter = ord(letter)
            if FROM_A <= new_letter <= FROM_Z:
                i += 1
                if i >= 2:
                    return True
    else:
        return False


def register():
    repeat_register = True
    user = None
    while repeat_register:
        try:
            login = input('Please enter the login: ')
            password = input('Please enter the password (Pay attention to use min 2 capital letters: ')
            confirm_password = input('Please confirm the password: ')
            if check_pass(password, confirm_password):
                try:
                    user = write_to_db(login=login, password=password)
                    repeat_register = False
                    print('registration successful')
                    calc_long(login)
                except ValueError as e:
                    repeat_register = True
                    print(e)
            else:
                print('incorrect password, juggler')
        except Exception as e:
            print(e)
    return user


def write_to_db(**new_user):
    file = os.path.join(file_of_users)

    def check_user_in_db(login):
        # nonlocal file_of_users
        with open(file_of_users, 'r') as users:
            list_users = json.load(users)
            for user in list_users:
                if user['login'] == login:
                    raise ValueError('user already exists with login {}'.format(login))
                    return True
            return False

    with open(file_of_users, 'r') as file:
        listUsers = json.load(file)
        if len(listUsers) == 0:
            new_user.update(
                {'id': 1})
            new_user.update(
                {'operation_history': []}
            )
        else:
            check_user_in_db(login=new_user['login'])
            new_id = listUsers[-1]['id'] + 1

            new_user.update(
                {'id': new_id})
            new_user.update(
                {'operation_history': []}
            )
            listUsers.append(new_user)
    with open(file_of_users, 'w+') as f:
        json.dump(listUsers, f)
    return new_user


def calc_short():
    repeat_calc = True
    while repeat_calc:
        try:
            a = int(input('Please enter the first number: ').strip())
            operation = input('+ - / * : ').strip()
            if operation == '+' or operation == '-' or operation == '*' or operation == '/':
                b = int(input('Please enter the second number: ').strip())
                if operation in list(Keys.calc_object.keys()):
                    result = Keys.calc_object[operation](a, b)
                    print(result)
            else:
                print('No such operations')
        except Exception as e:
            print(e)
        k = input('Do u want to continue? T/F')
        if k == 'T':
            repeat_calc = True
        else:
            break


def calc_long(login):
    repeat_calc = True
    while repeat_calc:
        try:
            a = int(input('Please enter the first number (if u want to stop input 00): ').strip())
            if a == 00:
                get_history(login)
                break
            operation = input('+ - / * sin cos tan cotan: ').strip()
            if operation == '+' or operation == '-' or operation == '*' or operation == '/':
                b = int(input('Please enter the second number: ').strip())
                if operation in list(Keys.calc_object.keys()):
                    result = Keys.calc_object[operation](a, b)
                    format_res = ('{} {} {} = {}'.format(a, operation, b, result))
            elif operation in list(Keys.calc_object.keys()):
                result = Keys.calc_object[operation](a)
                format_res = ('{}({}) = {}'.format(operation, a, result))

            print(result)
            time = datetime.datetime.now()
            check_id_in_db(time, format_res, login)
        except Exception as e:
            print(e)


def check_id_in_db(time, format_res, login):
    with open(file_of_users, 'r') as users:
        list_users = json.load(users)
        for user in list_users:
            if user['login'] == login:
                user['operation_history'].append({
                     "date": str(time),
                     "operation": format_res})
    with open(file_of_users, 'w+') as f:
        json.dump(list_users, f)
        return list_users


def get_history(login):
    k = input('Do you want to see the history of operations? T/F')
    if k == 'T':
        with open(file_of_users, 'r') as users:
            list_users = json.load(users)
            for user in list_users:
                if user['login'] == login:
                    print(user['operation_history'][:])

    else:
        return False


def main():
    start()


main()
