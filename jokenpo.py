from random import randint  # importa a biblioteca
itens = ['pedra', 'papel', 'tesoura']  # array com os objetos
computador = randint(0, 2)
print('''suas opções:
[0]pedra
[1]papel
[2]tesoura''')
jogador = int(input('Qual a sua jogada: '))
print('-' * 12)
print('O computdor jogou: {}'.format(itens[computador]))
print('o jogador escolheu: {}'.format(itens[jogador]))
print('-' * 12)


if computador == 0:  # computador jogou pedra
    if jogador == 0:
        print('empate')
    elif jogador == 1:
        print('jogador venceu')
    elif jogador == 2:
        print('computador venceu')
    else:
        print('jogada invalida!')
elif computador == 1:  # computador jogou papel
    if jogador == 0:
        print('computador venceu')
    elif jogador == 1:
        print('empate')
    elif jogador == 2:
        print('jogador venceu')
    else:
        print('jogada invalida!')
elif computador == 2:  # computador jogou tesoura
    if jogador == 0:
        print('jogador venceu')
    elif jogador == 1:
        print('computador venceu')
    elif jogador == 2:
        print('empate')
    else:
        print('jogada invalida!')
