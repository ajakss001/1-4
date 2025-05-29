def date(date_string):
    parts = date_string.split('-')
    date_dict = {
        'year': parts[0],
        'month': parts[1],
        'day': parts[2]
    }
    return date_dict

date_string = '2025-12-31'
result = date(date_string)
print(result)