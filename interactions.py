import pet

def feeding(my_pet):
    food_choice=input(f'Qual alimento deseja dar para {my_pet}?\n'
        '[1] Ração\n'
        '[2] Petisco\n'
        '[3] Frango\n'
        '[4] Voltar para o menu principal\n')
    match food_choice:
        case '1':
            pet.PetClass.feeding(20)
        case '2':
            pet.PetClass.feeding(5)
        case '3':
            pet.PetClass.feeding(10)
        case '4':
            print('voltando...')