
from random import choice


def generate_num_car_license_plates(amount: int) -> list:
    car_license_plates_alphabet = {
        'numbers' : ''.join(list(map(str, range(10)))),
        'letters' : 'АВЕКМНОРСТУХ'
    }

    plates = []
    for i in range(amount):
        numbers = []
        letters = []
        
        for _ in range(3):
            numbers.append(choice(car_license_plates_alphabet['numbers']))
            letters.append(choice(car_license_plates_alphabet['letters']))
        
        plates.append(''.join(letters[0:1]+numbers[:]+letters[1:]))

    return plates

