import re

def is_plate(plate):
    plate = str(plate)
    pattern = r'[А-Я][0-9]{3}[А-Я]{2}'
    return len(plate) == 6 and re.search(pattern, plate)

