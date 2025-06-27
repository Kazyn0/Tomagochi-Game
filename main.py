import pet, re, time, os, interactions

pattern = r'^[A-Za-z]+$'


while True:
    nomePet=input("Digite o nome que deseja dar ao seu pet: ")
    if re.fullmatch(pattern, nomePet):
        print(f"Parabéns, seu bichinho se chama {nomePet}!")
        break
    else:
        os.system('cls')
        print("Entrada inválida. Tente novamente.")


myPet=pet.PetClass(nomePet)
ShowStates=pet.PetClass.show_states(myPet)


while True:
    os.system('cls')
    time.sleep(1.5)
    option_menu = int(input(f"O que deseja realizar com {nomePet}?\n"
                        "[1] Alimentar\n"
                        "[2] Brincar\n"
                        "[3] Colocar para dormir\n"
                        "[4] Mostrar status\n"
                        "[5] Sair do jogo\n"))

    match option_menu:
        case 1:
            print(f'Você alimentou com {nomePet}.')
        case 2:
            print(f'Voc<UNK> brincou com {nomePet}.')
        case 3:
            print(f'Voc<UNK> colocou {nomePet} para dormir.')
        case 4:
            print('ENTROU AQUI')
            print(pet.PetClass.show_states(myPet))
        case 5:
            print('Saindo...')
            break