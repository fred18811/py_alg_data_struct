"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
"""

user_data = {"Anna":{"pass":"GGefdg!34f","active":1},"Den":{"pass":"fdgewgv43","active":0},"Georgy":{"pass":"ggrvwefqwe","active":1}}
login = "Den"
passwd = "fdgewgv43"


###############################################################
def get_access_1(data, log, passwd):
####Сложность: O(n)
    if log in data:                                 # O(n)
        if data[log]["pass"] is passwd:             # O(1)
            if data[log]["active"]:                 # O(1)
                return "Access allowed"             # O(1)
            else:
                return "Account is not activated, are you want to activate it?"    # O(1)
        else:
            return "Password not incorrect"         # O(1)
    else:
        return "Access denied"                      # O(1)


###############################################################
def get_access_2(data, log, passwd):
####Сложность: O(1)
    try:
        if data[log] and data[log]["pass"] is passwd:                               # O(1)
            if data[log]["active"]:                                                 # O(1)
                return "Access allowed"                                             # O(1)
            else:
                return "Account is not activated, are you want to activate it?"     # O(1)
        else:
            return "Password not incorrect"                                         # O(1)
    except KeyError:
        return "Access denied"                                                      # O(1)


###############################################################
def get_access_3(data, log, passwd):
####Сложность: O(n^2)
    if log in data:                                                                     # O(n)
        for key in data:                                                                # O(n)
            if data[log]["pass"] is passwd:                                             # O(1)
                if data[log]["active"]:                                                 # O(1)
                    return "Access allowed"                                             # O(1)
                else:
                    return "Account is not activated, are you want to activate it?"     # O(1)
        else:
            return "Password not incorrect"                                             # O(1)
    else:
        return "Access denied"                                                          # O(1)


###############################################################

####Первый вариант
print(format(get_access_1(user_data, "Den", "fdgewgv43")))

####Второй вариант
print(format(get_access_2(user_data, "Anna", "GGefdg!34f")))

####Третий вариант
print(format(get_access_3(user_data, "Georgy", "5435gre")))


"""
Второе решение эффективнее, 
т.к. у решения константная зависимость, 
что эффективнее чем линейная и квадратичная зависимости
"""