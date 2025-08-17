import pygame
import random






def atakeskese(ataque, defesa):
    return {
                'scratch': 1*ataque-defesa,
                'quick attack': 2*ataque-defesa,
                'flamethrower': ((2*ataque)-defesa)*elemento('fogo'),
                'surf': ((2*ataque)-defesa)*elemento('agua')
            }



class pokemon:
    def __init__(self, tipo, movimentos, velocidade, ataque, defesa, vida):
        self.tipo = tipo
        self.movimentos = movimentos
        self.velocidade = velocidade
        self.ataque = ataque
        self.defesa = defesa
        self.vida = vida

    def atacar(self):
        print('')
        for j in range(len(self.movimentos)):
            print(self.movimentos[j])
        escl = input('escolha um ataque: ')
        for k in range(len(self.movimentos)):
            if escl == self.movimentos[k]:
                print(elemento('fogo'))
                b.vida -= atakeskese(self.ataque, self.defesa)[escl]
                print(b.vida)
    
    # def elemento(self, tipo_do_ataque):
    #     if b.tipo == 'agua':
    #         match tipo_do_ataque:
    #             case 'agua':
    #                 return 1
    #             case 'fogo':
    #                 return 2
    #             case 'planta':
    #                 return 0.5
    #     if b.tipo == 'fogo':
    #         match tipo_do_ataque:
    #             case 'agua':
    #                 return 0.5
    #             case 'fogo':
    #                 return 1
    #             case 'planta':
    #                 return 2
    #     if b.tipo == 'planta':
    #         match tipo_do_ataque:
    #             case 'agua':
    #                 return 2
    #             case 'fogo':
    #                 return 0.5
    #             case 'planta':
    #                 return 1



class inimigo(pokemon):
    def __init__(self, tipo, movimentos, velocidade, ataque, defesa, vida):
        super().__init__(tipo, movimentos, velocidade, ataque, defesa, vida)
    def atacar(self):
        escl = random.choice(self.movimentos)
        for k in range(len(self.movimentos)):
            if escl == self.movimentos[k]:
                a.vida -= atakeskese(self.ataque,self.defesa)[escl]

        


charizardattack = ['scratch', 'quick attack', 'flamethrower']
aguaattack = ['scratch', 'quick attack', 'surf']
b = inimigo('agua', aguaattack, 2, 2, 2, 10)
a = pokemon('fogo', charizardattack, 2, 2, 2, 10)

def elemento(tipo_do_ataque):
        if b.tipo == 'agua':
            match tipo_do_ataque:
                case 'agua':
                    return 1
                case 'fogo':
                    return 0.5
                case 'planta':
                    return 2
        if b.tipo == 'fogo':
            match tipo_do_ataque:
                case 'agua':
                    return 2
                case 'fogo':
                    return 1
                case 'planta':
                    return 0.5
        if b.tipo == 'planta':
            match tipo_do_ataque:
                case 'agua':
                    return 0.5
                case 'fogo':
                    return 2
                case 'planta':
                    return 1



while True:
    a.atacar()
    print(b.vida)
    b.atacar()
    print(a.vida)
    if a.vida <= 0:
        print('você perdeu')
        break
    elif b.vida <= 0:
        print('você ganhou')
        break