#possíveis operações com print
nome = input('Digite o seu nome: ')
print('Olá {:20}!'.format(nome)) #coloca o nome em 20 espaços
print('Olá {:<20}!'.format(nome)) #alinha a direita
print('Olá {:>20}!'.format(nome)) #alinha a esquerda
print('Olá {:^20}!'.format(nome)) #centraliza o nome
print('Olá {:=^20}!'.format(nome)) # preenche o que sobrou com sinais de '='