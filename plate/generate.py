from flask_restful import Resource, reqparse
from random import choice


class Generate(Resource):

    def __generate_num_car_licenses_plates(self, amount: int) -> list:
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


    def get(self, amount):
        
        if amount > 0 and isinstance(amount, int):
            plates = self.__generate_num_car_licenses_plates(amount)
        else:
            plates = None

        return {
            'plates' : plates
        }