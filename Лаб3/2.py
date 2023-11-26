# TODO Напишите функцию find_common_participants
def find_common_participants(i, j, k = ","):
    res1 = i.split(k)
    res2 = j.split(k)
    res3 = set(res1)
    res4 = set(res2)
    res5 = res3.intersection(res4)
    res6 = list(res5)
    return sorted(res6)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
