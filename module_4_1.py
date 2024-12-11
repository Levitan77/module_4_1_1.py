# Домашняя работа по уроку "Модули и пакеты"

# Задача "А как делить?":

# Пункты задачи:
# 1 Создайте модули fake_math и true_math.
# 2 Напишите функции divide в обоих методах. Разница между этими функциями - возвращаемое значение.
# 3 Создайте модуль module_4_1 (если ещё не создан), импортируйте в него функции divide из модулей fake_math и true_math,
#   назвав их разными именами на своё усмотрение, чтобы не было конфликтов имён, при помощи оператора as.
# 4 Запустите эти функции в модуле module_4_1, передав первым аргументом произвольное число отличное от 0,
#   вторым аргументом - 0
# 5 Выведи результаты вызовов этих функций на экран(в консоль).

from fake_math import divide as fk_div
from true_math import divide as tr_div
print('result1 = ', fk_div(12, 4))
print('result2 = ', fk_div(12, 0))
print('result3 = ', tr_div(13, 5))
print('result4 = ', tr_div(13, 0))