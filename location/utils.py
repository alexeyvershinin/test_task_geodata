def get_lst(s):
    """
    Функция преобразовывает полученный из базы данных строку в список со значениями float
    для нанесения корректной разметки полигона на карту
    :param s: str
    :return: list
    """
    s = s.replace("[[", "").replace("]]", "")
    lst = []
    for item in s.split('], ['):
        row = list(map(float, item.split(',')))
        lst.append(row)
    return lst
