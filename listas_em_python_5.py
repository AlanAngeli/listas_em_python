secreto = "Pugui"
digitadas = []
chances = 3

print("Vcoê tem", chances, "chances para acertar a palavra secreta!")
print("Dica da palavra secreta: é um nome!")

while True:
    if chances <= 0:
        print("Você perdeu!")
        break


    letra = input("Digite uma letra: ")
    print()


    if len(letra) > 1:
        print("Isso não vale! Digite apenas uma letra ou número.")
        continue

    digitadas.append(letra)


    if letra in secreto:
        print("A letra", letra, "existe na palavra secreta!")
    else:
        print("A letra não existe na palavra secreta.")
        chances -= 1
        if chances != 0:
            print("Você tem", chances,"chances")
        elif chances == 0:
            print("Você não tem mais chances!")

        digitadas.pop() #remove da lista o último elemento digitado



    secreto_temporario = ""

    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += "*"
    print()
    print("Palavra secreta: ", secreto_temporario)
    if secreto_temporario == secreto:
        print("Você acertou!", secreto_temporario, "é a palavra secreta!")
        break

