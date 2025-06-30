import pet, re, time, os, interactions
from pet import PetClass


pattern = r'^[A-Za-z]+$'
while True:
    nomePet=(input("Digite o nome que deseja dar ao seu pet: "))
    if re.fullmatch(pattern, nomePet):
        print(f"Parabéns, seu bichinho se chama {nomePet}!")
        break
    else:
        os.system('cls')
        print("Entrada inválida. Tente novamente.")
my_pet=PetClass(nomePet)



while True:
    option_menu = int(input(f"O que deseja realizar com {nomePet}?\n"
        "[1] Alimentar\n"
        "[2] Brincar\n"
        "[3] Colocar para dormir\n"
        "[4] Mostrar status\n"
        "[5] Sair do jogo\n"))
    os.system('cls')


    match option_menu:
        case 1:
            interactions.feeding_action(my_pet)
            print(f'Você alimentou {my_pet}, sua fome diminuiu.')
        case 2:
            interactions.playing_action(my_pet)
            print(f'Você brincou com {my_pet}, sua felicidade aumentou.')
        case 3:
            print(f'Voc<UNK> colocou {nomePet} para dormir.')
        case 4:
            print(pet.PetClass.show_states(my_pet))
            os.system('cls')
        case 5:
            print('Saindo...')
            break