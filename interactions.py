import pet,os

def feeding_action(my_pet):
    food_choice=input(f'Qual alimento deseja dar para {my_pet}?\n'
        '[1] Ração\n'
        '[2] Petisco\n'
        '[3] Frango\n'
        '[4] Voltar para o menu principal\n')
    os.system('cls')
    match food_choice:
        case '1':
            pet.PetClass.feeding_class(my_pet, 20)
        case '2':
            pet.PetClass.feeding_class(my_pet, 5)
        case '3':
            pet.PetClass.feeding_class(my_pet, 10)
        case '4':
            print('voltando...')

def playing_action(my_pet):
    toy_choice=input(f'Qual brinquedo deseja dar para {my_pet}?\n'
        '[1] Bolinha\n'
        '[2] Graveto\n'
        '[3] Voltar para o menu principal\n')
    os.system('cls')
    match toy_choice:
        case '1':
            pet.PetClass.playing_class(my_pet, 10)
        case '2':
            pet.PetClass.playing_class(my_pet, 5)
        case '3':
            print('voltando...')