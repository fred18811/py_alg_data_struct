"""
Задание 3.

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
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""

company_profit = {"Canon": 456165168, "HP": 12189461, "Lenovo": 216541613210, "Asus": 312584151, "Acer": 65141144}

###############################################################
def get_max_sum_1(company_data):
####Сложность: O(n)
    max_profit = {}                                 # O(1)
    copy_dict = company_data.copy()                 # O(n)

    for k in range(3):                              # O(1)
        max_numb = None                             # O(1)
        name_comp = None                            # O(1)
        for k in copy_dict:                         # O(n)
            if max_numb is not None:                # O(1)
                if max_numb >= copy_dict[k]:        # O(1)
                    max_numb = copy_dict[k]         # O(1)
                    name_comp = k                   # O(1)
            else:
                max_numb = copy_dict[k]             # O(1)
                name_comp = k                       # O(1)
        copy_dict.pop(name_comp)                    # O(1)
        max_profit[name_comp] = max_numb            # O(1)
    return max_profit                               # O(1)


#################################################################
def get_max_sum_2(company_data):
####Сложность: O(n log n)
    max_profit = list(company_data.items())             # O(n)
    max_profit.sort(key=lambda i: i[1])                 # O(n log n)
    max_profit = max_profit[:3]                         # O(b-a)
    max_profit = dict(max_profit)                       # O(n)
    return max_profit                                   # O(1)


#################################################################
def get_max_sum_3(company_data):
####Сложность: O(n log n)
    copy_dict = company_data.copy()                             # O(n)
    max_profit = {}                                             # O(1)
    sorted_keys = sorted(copy_dict, key=copy_dict.get)          # O(n log n)
    for w in range(3):                                          # O(1)
        max_profit[sorted_keys[w]] = copy_dict[sorted_keys[w]]  # O(1)
    return max_profit                                           # O(1)


#################################################################


print(company_profit)

####Первый вариант
print(get_max_sum_1(company_profit))

####Второй вариант
print(get_max_sum_2(company_profit))

####Третий вариант
print(get_max_sum_3(company_profit))


"""
Первое решение эффектривнее, 
т.к. у решения линейная зависимость,
что эффективнее чем логарифмическая зависимость
"""