from datetime import datetime


def formatting_date(date_string):
    """
    Преобразует в списке даты в формат ДД.ММ.ГГГГ
    :param operations: Исходный список
    :return: Список с отформатированными датами
    """
    date_object = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%f")

    return date_object.strftime("%d.%m.%Y")


def mask_number(number):
    """
    Маскирует номер карты
    :param card_number: Номер карты
    :return: Замаскированный номер карты
    """
    parts = number.split()
    type_ = ' '.join(parts[0:-1])
    number_ = parts[-1]

    if 'Счет' in number:
        return "{} {}".format(type_, "**" + number_[-4:])

    return "{} {} {} **** {}".format(type_, number_[:4], number_[4:6] + "**", number_[-4:])
