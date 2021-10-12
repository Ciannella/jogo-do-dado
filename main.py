from random import randint
from time import sleep
""" jogo do dado """

def borda(msg):
    print('-' * len(msg))
    print(msg)
    print('-' * len(msg))


jogador = computador = ''

borda('jogo do dado')
print('Tente ganhar do computador')
print('-=' *30)
v = e = d= 0
while True:
    resp = input('Deseja rolar o dado? [S]sim, [N]não: ').strip().upper()[0]
    print()
    while resp not in 'SsNn':
        print('Digite apenas sim ou não')
        resp = input(">>>").strip().upper()[0]
    if resp in 'Ss':
        jogador = randint(1,6)
        computador = randint(1,6)
        if jogador > computador:
            v+=1
            print(f'Você tirou {jogador} e a maquina {computador}')
            print('Detonou a maquina')
        elif jogador < computador:
            d+=1
            print(f'Você tirou {jogador} e a maquina {computador}')
            print('Chame o exterminador do futuro pois a maquina te superou')
        else:
            e+=1
            print(f'Você tirou {jogador} e a maquina {computador}')
            print('Ah não deu EMPATE!')

    else:
        break
print('-=' * 20)
print('Encerrando o jogo...')
sleep(1.5)
print(f"""Você ganhou da maquina {v} vezes
empatou {e} e foi detonado {d} vezes""")