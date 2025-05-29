from datetime import datetime

def format_date(date_str):
    day, month, year = map(int, date_str.split('.'))
    date_obj = datetime(year=year, month=month, day=day)

    weekdays = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    months = ["Января", "Февраля", "Марта", "Апреля", "Мая", "Июня",
              "Июля", "Августа", "Сентября", "Октября", "Ноября", "Декабря"]

    weekday = weekdays[date_obj.weekday()]
    month_name = months[month - 1]

    return f"{weekday}, {day} {month_name}, {year} год"

print(format_date("01.09.2021"))