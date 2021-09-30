from users_generator.randomengine.parser import Parser
from users_generator.randomengine.loginandpassword import DataAuth

import random
import time


class RandomUserData():

    def __init__(
        self,
        start_date: str = None,
        stop_date: str = None,
        gender: str = None,
    ) -> None:
        """Methods for radom data

        Args:
            start_date: %d%m%Y
            stop_date: %d%m%Y
        """
        self.start_date = start_date
        self.stop_date = stop_date
        self.gender = gender

    def full_random_user(self) -> dir:
        """The method returns random data of a male/female's
        full name,date of birth, isername and password
        Example: dic -> 
        {'gender': , 'surname': , 'fistname': , 'patranymic': , 'date of birth': ,
        'username': , 'password':}
        """
        random_date = self._formation_date()
        gender = random.choice(['male', 'female'])
        surname = random.choice(Parser.get_data(gender=gender)[0])
        firstname = random.choice(Parser.get_data(gender=gender)[1])
        patranymic = random.choice(Parser.get_data(gender=gender)[2])
        if gender == 'male':
            patranymic = patranymic + 'ич'
        else:
            patranymic = patranymic + 'на'
        date_birth = random_date
        username = DataAuth().username(surname)
        password = DataAuth().password(firstname)
        return {
            'gender': gender,
            'surname': surname,
            'firstname': firstname,
            'patranymic': patranymic,
            'date_birth': date_birth,
            'username': username,
            'password': password
        }

    def castom_random_user(self) -> dir:
        """The method returns random data of a male/female's
        full name,date of birth, isername and password
        Example: dic -> 
        {'gender': , 'surname': , 'fistname': , 'patranymic': , 'date of birth': ,
        'username': , 'password':}
        """
        gender = self.gender
        if gender == 'random':
            gender = random.choice(['male', 'female'])
        random_date = self._formation_date(self.start_date, self.stop_date)
        surname = random.choice(Parser.get_data(gender=gender)[0])
        firstname = random.choice(Parser.get_data(gender=gender)[1])
        patranymic = random.choice(Parser.get_data(gender=gender)[2])
        if gender == 'male':
            patranymic = patranymic + 'ич'
        else:
            patranymic = patranymic + 'на'
        date_birth = random_date
        username = DataAuth().username(surname)
        password = DataAuth().password(firstname)
        return {
            'gender': gender,
            'surname': surname,
            'firstname': firstname,
            'patranymic': patranymic,
            'date_birth': date_birth,
            'username': username,
            'password': password
        }

    def _formation_date(
        self,
        start_date: str = None,
        stop_date: str = None
    ) -> str:

        if start_date:
            start = start_date
        else:
            start = '1990-01-01'
        if stop_date:
            stop = stop_date
        else:
            stop = '2010-01-01'

        date_start_sec = time.mktime(time.strptime(start, '%Y-%m-%d'))
        date_stop_sec = time.mktime(time.strptime(stop, '%Y-%m-%d'))
        random_data_sec = random.randint(
            0, date_stop_sec - date_start_sec
        ) + date_start_sec
        return time.strftime('%d.%m.%Y', time.localtime(random_data_sec))
