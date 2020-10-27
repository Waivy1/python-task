class FirstLastName:
    last_name = 'Popovych'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return f'you are {self.name} {self.last_name}'
