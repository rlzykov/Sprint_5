from random import randint


class UserProfile:
    user_name = 'Пудж'
    email = f'pudge.hookov@rak.com'
    password = f'12345Xyz'


class RandomData:
    user_name = 'Тест'
    email = f'test{randint(0, 999)}@rak.com'
    password = f'{randint(1000, 9999)}Xyz'
