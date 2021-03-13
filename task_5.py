"""
Задание 5.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях

Подсказка:
Отдельне стопки можно реализовать через:
# 1) созд-е экземпляров стека (если стопка - класс)
# 2) lst = [[], [], [], [],....]
"""


class StackClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        self.elems.append(el)

    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        if self.elems == []:
            return 0
        else:
            return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)


class StackPlates:
    def __init__(self, max_stack):
        self.__max_stack = max_stack
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def push_plates(self, el):
        if el == "plate":
            if (self.elems == [] or self.elems[len(self.elems) - 1].stack_size() == self.__max_stack):
                self.elems.append(StackClass())
                self.elems[len(self.elems) - 1].push_in(el)
            else:
                self.elems[len(self.elems) - 1].push_in(el)

            return "Add plate"
        else:
            return "No a plate"

    def stacks_size(self):
        return len(self.elems)

    def plates_size_in_stack(self):
        if self.elems == []:
            return 0
        else:
            return self.elems[len(self.elems) - 1].stack_size()

    def pop_out(self):
        if self.elems == []:
            return "No elements"
        else:
            plate = self.elems[len(self.elems) - 1].pop_out()
            if not self.elems[len(self.elems) - 1].stack_size():
                self.elems.pop()
            return plate

    def get_val(self):
        if self.elems != []:
            return self.elems[len(self.elems) - 1].get_val()
        else:
            return "No elements"


if __name__ == '__main__':
    plates = StackPlates(4)
    # Добавляем  7 тарелок и одну не тарелку, если это не тарелки, не добавляем
    print("*" * 50)
    print("Добавляем  7 тарелок")
    plates.push_plates("plate")
    plates.push_plates("plate")
    plates.push_plates("plate")
    plates.push_plates("plate")
    plates.push_plates("plate")
    plates.push_plates("plate")
    plates.push_plates("plate")
    print("*" * 50)
    print("Добавляем не тарелку")
    print(plates.push_plates("plate1"))
    print("*" * 50)
    # Смотрим колличество стопок
    print("колличество стопок {}".format(plates.stacks_size()))

    # Смотрим колличество тарелок в стопке
    print("колличество тарелок в последней стопке {}".format(plates.plates_size_in_stack()))

    # Удаляем 3 тарелки
    print("*" * 50)
    print("Удаляем 3 тарелки")
    plates.pop_out()
    plates.pop_out()
    plates.pop_out()
    print("*" * 50)
    # Смотрим колличество стопок
    print("колличество стопок {}".format(plates.stacks_size()))
    # Смотрим колличество тарелок в стопке
    print("колличество тарелок в последней стопке {}".format(plates.plates_size_in_stack()))

    # Удаляем 5 тарелки
    print("*" * 50)
    print("Удаляем 5 тарелки")
    plates.pop_out()
    plates.pop_out()
    plates.pop_out()
    print(plates.pop_out())
    print(plates.pop_out())
    print("*" * 50)
    # Смотрим колличество стопок
    print("колличество стопок {}".format(plates.stacks_size()))
    # Смотрим колличество тарелок в стопке
    print("колличество тарелок в последней стопке {}".format(plates.plates_size_in_stack()))
    # Посмотреть значение в стопке
    print(plates.get_val())
