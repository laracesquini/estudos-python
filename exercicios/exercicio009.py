#Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
n = int(input('Digite um número: '))
print('------------')
for i in range(0, 11):
    print('{} X{:2} = {}'.format(n, i, (n*i)))
print('------------')