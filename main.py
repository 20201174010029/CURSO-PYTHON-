# 001 
print('olá mundo')

#002 
n1 = str(input('digite seu nome: '))

print('boas-vindas' ,n1,'!')

#003
deby1= int(input('venha me diga um numero! '))
deby2= int(input('diga outro pfvr! '))

som = deby1 + deby2 

print('sua soma e igual a' ,som,'!')

#004
a= input('digite algo:  ')
print('tipo primitivo é ',type(a))

print('olá sensei!')

#005
n = int(input('digite um numero! '))
a = n -1
s = n +1

print('analisando o valor {} seu antecessor é {} e o seu sucessor é {}'.format(n, a, s))

#006
n = int(input('digite um numero pfvr! '))
d= n*2
t=n*3
r=n**(1/2)
print('o dobro de {} vale {}.'.format(n ,d))
print('o tiplo de {} vale {}.'.format(n, t))
print('raiz quadrada de {} vale {}.'.format(n, r))

#007

a1= float(input('digite a primeira nota do aluno! '))
a2= float(input('digite segunda nota do aluno! '))
media= (a1 + a2)/2
print('a media entre {} é {} é igual a {}...'.format(a1 ,a2 ,media))

#008
medida =float(input('distancia em metro: '))
cm= medida*100
mm= medida*1000
print('a media em {}m corresponde a {}cm e {}mm.'.format(medida ,cm ,mm))

#009

abc= int(input('digite um numero pra ver sua tabuada: '))
print('{} x {} ={}'.format(abc, 1, abc*1))
print('{} x {} ={}'.format(abc, 2, abc*2))
print('{} x {} ={}'.format(abc, 3, abc*3))
print('{} x {} ={}'.format(abc, 4, abc*4))
print('{} x {} ={}'.format(abc, 5, abc*5))
print('{} x {} ={}'.format(abc, 6, abc*6))
print('{} x {} ={}'.format(abc, 7, abc*7))
print('{} x {} ={}'.format(abc, 8, abc*8))
print('{} x {} ={}'.format(abc, 9, abc*9))
print('{} x {} ={}'.format(abc, 10, abc*10))

print('vlwzin!')
#010
real = float(input('quanto dinheiro você tem na carteira R$'))
dolar = real/1.00
print('com {} R$ você pode comprar {} US$'.format(real, dolar))

#011
largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
print(f'Sua parede tem a dimensão de {largura}x{altura} e sua área é de {largura*altura}m².')
print(f'Para pintar essa parede, você precisará de {largura*(altura / 2)}L de tinta.')

print('oizin!')

#012

p = float(input('Qual o preço do produto? '))
x = int(input('De quanto será o desconto? '))
d = (p/100) * x
v = p-d
print('O produto que custava R${:.2f}, com {}% de desconto vai custar R${:.2f}'.format(p, x, v))

#013
p = float(input('Qual é seu salario? '))
x = int(input('De quanto será o aumento? '))
a = (p/100) * x
v = p+a
print('O seu salario que era de R${:.2f},agora com aumento de  {}%  vai fica R${:.2f}'.format(p, x, v))

#014
c=float(input('Informe a temperatura em °C: '))
f=(c*1.8+32)
print('{}°C é equivalente a {}°F'.format(c,f))

#015

d = int(input('Por quantos dias você alugou o carro? '))
km = float(input('Quantos quilômetros você rodou com ele? '))
a = d * 60 + km * 0.15
print(f'Você deve R${a:.2f} de aluguel')

#016
num = float(input('Digite um valor:'))
print('O valor {} tem sua parte inteira {:.0f}'.format(num, num))
print('obrigadu!')

#017
from math import sqrt
print('Calculando a Hipotenusa')
co = float(input('Insira o valor do cateto oposto: '))
ca = float(input('Insira o valor do cateto adjacente: '))

hi = (co ** 2) + (ca ** 2)

hi = sqrt(hi)
print('A hipotenusa desse triângulo é:{:.2f}'.format(hi))

#018

import math
an = float(input('digite o angulo q deseja ? '))
r = math.radians(an)
s = math.sin(r)
c = math.cos(r)
t = math.tan(r)
print('se o angulo for {} \n o seno sera {:.3f} \n o coseno sera{:.3f} \n e a trangente sera {:.3f}'.format(an, s, c, t))
print('valeu !')

#019

from random import choice
a = str(input("1°aluno Nome: "))
b = str(input("2° aluno Nome: "))
c = str(input("3° aluno Nome: "))
d = str(input("4° aluno Nome: "))
escolhido = (a, b, c, d)
print("A pessoa escolhida foi {}".format(choice(escolhido)))
print('ops vc não ser deu bem hehehe!')

#020

from random import shuffle
p = input('Digite o nome do 1° aluno: ')
s = input('Digite o nome do 2° aluno: ')
t = input('Digite o nome do 3° aluno: ')
q = input('Digite o nome do 4° aluno: ')
lista = [p, s, t, q]
emb = shuffle(lista)
print('a ordem foi {}'.format(lista))
print('valeu!')
#021
from playsound import playsound
playsound('arquivo.mp3')

#022

nome = input('Ingresse seu nome completo : ')
print('Seu nome completo é : {}'.format(nome)) 
print('Seu nome em maiúsculas : {}'.format(nome.upper()))
print('Seu nome em minúsculas : {}'.format(nome.lower()))
# Forma 1
separado = nome.split() # lo separo
print(separado) # lo muestro separado
print(''.join(separado)) #lo muestro unido (sem espacios)
print('O cumprimento do nome sem espacios é: {}'.format(len(''.join(separado))))
# Forma 2
print('Cumprimento {}'.format(len(nome.replace(' ',''))))

# Quantas letras tem o primeiro nome
print('Quantidade letras o 1er nome é: {}'.format(len(separado[0])))

#023

n = int(input('Digite um número entre 0 e 9999: '))
n2 = str(int(10000 + n))
print('O número {} possui, {} milhares.'.format(n, n2[1]))
print('O número {} possui, {} centenas. '.format(n, n2[2]))
print('O número {} possui, {} dezenas. '.format(n, n2[3]))
print('O número {} possui, {} unidades.'.format(n, n2[4]))

#024

nome=str(input("Introduza o nome da cidade: ")).strip()
print("santo" in nome.lower())

#025

nome=str(input("diga seu nome completo: ")).strip()
print("silva" in nome.lower())
print('valeu!')

#026

frase = str(input('digite uma frase: ')).strip().lower()
print('a letra a (sem acento) aparece',frase.count('a'),'vezes na frase.')
print('a posição que o a está é',frase.find('a')+1)
print('a letra a apareceu por ultimo na posição',frase.rfind('a')+1)

#027
nome = str(input('digite seu nome: ')).strip().lower()
print('seu nome (sem acento) aparece',nome.count('nome'),'vezes na frase.')
print('a posição que o nome está é',nome.find('a')+1)
print('seu nome apareceu por ultimo na posição',nome.rfind('nome')+1)


