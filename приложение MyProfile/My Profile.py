# MyProfile app

SEPARATOR = '------------------------------------------'

# user profile
name = ''  # Имя пользователя
age = 0  # Возраст пользователя
phone = ''  # Телефон пользователя
email = ''  # Электронный адресс пользователя
adress = ''  # Почтовый адресс пользователя
index = ''  # Индекс пользователя
info = ''  # Дополнительная информация о пользователе
# info business
individual_taxpayer_number = 0  # ИНН предпринимателя
primary_state_registration_number = 0  # ОГРНИП предпринимателя
bank_identification_code = 0  # БИК
payment_account = 0  # Расчетный счет
correspondent_account = 0  # Коореспондентский счет
name_bank = ''  # Название банка


def general_info_user(name_parameter, age_parameter, phone_parameter, email_parameter, index_parametr, adress_parametr,
                      info_parameter):
    print(SEPARATOR)
    print('Имя:    ', name_parameter)
    if 11 <= age_parameter % 100 <= 19:
        years_parameter = 'лет'
    elif age_parameter % 10 == 1:
        years_parameter = 'год'
    elif 2 <= age_parameter % 10 <= 4:
        years_parameter = 'года'
    else:
        years_parameter = 'лет'

    print('Возраст:', age_parameter, years_parameter)
    print('Телефон:', phone_parameter)
    print('E-mail: ', email_parameter)
    print('Индекс: ', index_parametr)
    print('Почтовый адресс: ', adress_parametr)
    if info:
        print('')
        print('Дополнительная информация: ')
        print(info_parameter)


print('Приложение MyProfile для предпринимателей')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    # main menu
    print(SEPARATOR)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')

    option = int(input('Введите номер пункта меню: '))
    if option == 0:
        break

    if option == 1:
        # submenu 1: edit info
        while True:
            print(SEPARATOR)
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Информация о предпринимателе')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            elif option2 == 1:
                # input general info
                name = input('Введите имя: ')
                while 1:
                    # validate user age
                    age = int(input('Введите возраст: '))
                    if age > 0:
                        break
                    print('Возраст должен быть положительным')

                user_phone = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                phone = ''
                for check in user_phone:
                    if check == '+' or ('0' <= check <= '9'):
                        phone += check

                email = input('Введите адрес электронной почты: ')
                user_index = input('Введите индекс: ')
                index = ''
                for check in user_index:
                    if '0' <= check <= '9':
                        index += check
                adress = input('Введите почтовый адресс: ')
                info = input('Введите дополнительную информацию:\n')

            elif option2 == 2:
                # input business
                primary_state_registration_number = input('Введите номер ОГРНИП: ')
                while len(primary_state_registration_number) != 15 or (not primary_state_registration_number.isdigit()):
                    print('Номер ОГРНИП введен не верно.')
                    primary_state_registration_number = input('Повторите ввод ОГРНИП:')
                primary_state_registration_number = int(primary_state_registration_number)
                individual_taxpayer_number = int(input('Введите ИНН: '))
                payment_account = input('Введите расчетный счет: ')
                while len(payment_account) != 20 or (not payment_account.isdigit()):
                    print('Номер расчетного счета введен не верно.')
                    payment_account = input('Повторите ввод расчетного счета:')
                payment_account = int(payment_account)
                name_bank = input('Введите название банка: ')
                bank_identification_code = int(input('Введите БИК: '))
                correspondent_account = int(input('Введите корреспондентский счёт: '))
            else:
                print('Введите корректный пункт меню')
    elif option == 2:
        # submenu 2: print info
        while True:
            print(SEPARATOR)
            print('ВЫВЕСТИ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Вся информация')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            elif option2 == 1:
                general_info_user(name, age, phone, email, index, adress, info)

            elif option2 == 2:
                general_info_user(name, age, phone, email, index, adress, info)

                # print sbusiness info
                print('')
                print('Информация о предпринимателе')
                print('ОГРНИП:', primary_state_registration_number)
                print('ИНН: ', individual_taxpayer_number)
                print('Расчетный счет: ', payment_account)
                print('Название банка: ', name_bank)
                print('БИК: ', bank_identification_code)
                print('Корреспондентский счет: ', correspondent_account)
            else:
                print('Введите корректный пункт меню')
    else:
        print('Введите корректный пункт меню')