import random

class PetClass:
    def __init__(self, name):
        self.name = name
        self.age = random.randint(1,15)
        self.happiness = random.randint(1, 100)
        self.hunger = random.randint(1, 100)
        self.tiredness = random.randint(1, 100)

    def __str__(self):
        return f"Pet {self.name}"

    def show_states(self):
        print(f'A felicidade do seu bichinho está em {self.happiness}.')
        print(f'A fome do seu bichinho está em {self.hunger}.')
        print(f'O cansaço do seu bichinho está em {self.tiredness}.')
        print(f'O seu bichinho tem {self.age} anos.')

    def feeding_class(self, quantidade):
        self.hunger -= quantidade
        if self.hunger < 0:
            self.hunger = 0