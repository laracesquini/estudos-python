#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
n = float(input('Digite a quantidade de dinheiro: '))
print('Com esse valor é possível comprar {:.2f} dólares.'.format(n/4.96))