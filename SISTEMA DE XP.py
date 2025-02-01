vida = 100
nivel = 1
ataque = 17
XP = 0
XPN = 30
while True:
    xpg = int(input("Escreve um numero para dar xp: "))
    XP = XP + xpg
    print(XP)

    if XP >= XPN:
        nivel += 1
        vida += 15
        ataque += 5
        print(f'***Prabens!! Subeste para nivel  {nivel}***\n'
              f'***A tua vida aumentou de {vida - 2} para {vida}***\n'
              f'***E agora tiras {ataque} de dano em vez de {ataque - 1}***')
        XP -= XPN
        XPN += 10

"""
Mdif = randint(0,3)
Mvida = Mdif + vida
Mnivel = Mdif + nivel
Mataque = (Mdif / 2) + ataque
while True:
    op = str(input('Opções: Ataque, Fugir'))
    if op == Ataque:
        Mvida -= ataque
    elif op == "Fugir":
        print('fugiste')
        break
"""





