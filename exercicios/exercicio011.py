#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
l = float(input('Digite a largura da parede: '))
a = float(input('Digite a altura da parede: '))
print('Para pintar essa parede, é necessário {} litros de tinta.'.format((l*a)/2))