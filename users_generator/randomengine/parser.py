

class Parser():

    @staticmethod
    def get_data(gender: str):

        if gender == 'male':
            with open('users_generator/randomengine/data/firstname_male.txt', 'r') as f:
                firstname = [firstname.rstrip() for firstname in f]
            with open('users_generator/randomengine/data/surname_male.txt', 'r') as f:
                surname = [surname.rstrip() for surname in f]
        elif gender == 'female':
            with open('users_generator/randomengine/data/firstname_female.txt', 'r') as f:
                firstname = [firstname.rstrip() for firstname in f]
            with open('users_generator/randomengine/data/surname_female.txt', 'r') as f:
                surname = [surname.rstrip() for surname in f]

        with open('users_generator/randomengine/data/patronymic.txt', 'r') as f:
            patronymic = [patronymic.rstrip() for patronymic in f]

        return [surname, firstname, patronymic]

