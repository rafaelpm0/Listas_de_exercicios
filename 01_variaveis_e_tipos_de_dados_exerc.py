"""
Neste projeto, sera resolvido todos os 51 exercicios propostos no curso Python. Variaveis e tipo de dados.
Irei colocar cada exercicio nos comentário.

Resolucao exercicio 1:
Faça um programa que leia um numero inteiro e o imprima

exercicio_01 = input('Digite um numero interiro:')
print(f'O numero é {exercicio_01}')
# print('\nO numero é {0}'.format(exercicio_01)) ex de pular linha \n e {} .format{variavel}, mais parecido com c


Resolucao exercicio 2:
Faça um programa que leia um numero real e o imprima

exercicio_02 = int(input('Digite um numero real:'))
print(f'O numero real é {exercicio_02}')
print('O numero real é {0}'.format(exercicio_02))


Resolução Exercicio 03:

Peça para o usuário digitar três valores inteiros e imprima a soma deles

a = int(input('Digite três numero interos e será apresentada a soma.\nPrimeiro numero: '))
b = int(input('Segundo numero: '))
c = int(input('Terceiro numero: '))

print(f'A soma dos três numeros é: {a+ b+ c}')


Resolução Exercicio 04:

Leia um numero real e irá retornar o quadrado desse numero

exercicio_04 = float(input('Digite um numero real e irá retornar o quadrado deste numero. Numero: '))
print(f'O quadrado do numero é: {exercicio_04 ** 2}')


Resolução Exercicio 05:
Leia um numero real e imprima a quinta parte desse numero

exercicio_05 = float(input('Digite um numero real e será impresso sua quinta parte. Numero: '))
print(f'A quinta parte é: {exercicio_05 / 5}')


Resolução Exercicio 06:
Leia uma temperatura em Celsius e apresente convertida em graus Fahrenheit

exercicio_06 = float(input("Digite a temperatura em graus Celsius e ela será devolvia em Fahrenheit. Cº: "))
print(f'A temperatura em grau Fº é: {((exercicio_06*(9.0/5.0))+32.0)}')


Resolução Exercicio 07:
Leia uma temperatura em Fahrenheit e apresente convertida em graus Celsius

exercicio_07 = float(input("Digite a temperatura em graus Fahrenheit e ela será devolvia em Celsius. Cº: "))
print(f'A temperatura em grau Cº é: {5.0* ((exercicio_07- 32.0)/ 9.0)}')


Resolução Exercicio 08:
Leia uma temperatura em Kelvin e apresente convertida em graus Celsius

exercicio_08 = float(input("Digite a temperatura em graus Kelvin e ela será devolvia em Censius. Kº: "))
print(f'A temperatura em grau Cº é: {exercicio_08- 273.15}')


Resolução Exercicio 09:
Leia uma temperatura em Censius e apresente convertida em graus Kelvin

exercicio_09 = float(input("Digite a temperatura em graus Censius e ela será devolvia em Kelvin. Cº: "))
print(f'A temperatura em grau Cº é: {exercicio_09+ 273.15}')


Resolução Exercicio 10:
Leia uma velocidade em Km/h e a presentea convertida para m/s

exercicio_10 = float(input('Digite a velocidade em Km/h e ela irá sair em m/s. Velocidade: '))
print(f'A velocidade convertida é de {exercicio_10/ 3.6}')


Resolução Exercicio 11:
Leia uma velocidade em m/s e a presentea convertida para Km/h

exercicio_11 = float(input('Digite a velocidade em m/s e ela irá sair em Km/h. Velocidade: '))
print(f'A velocidade convertida é de {exercicio_11* 3.6}')


Resolução Exercicio 12:
Leia uma velocidade em milhas e a presentea convertida para Km/h

exercicio_12 = float(input('Digite o valor em milhas e ela irá sair em quilometros. \nDistancia: '))
print(f'A distancia convertida é para {exercicio_12* 1.61}')


Resolução Exercicio 13:
Leia uma velocidade em Km/h e a presentea convertida para milhas

exercicio_13 = float(input('Digite o valor em quilometros e ela irá sair em milhas. \nDistancia: '))
print(f'A distancia convertida é para {exercicio_13/ 1.61}')


Resolução Exercicio 14:
Leia um angulo em graus e apresente-o convertido em radianos. Adote π como 3.14

exercicio_14 = float((input('Digite o valor em graus e será convertido em radianos. \nGraus: ')))
print(f'Radianos: {(exercicio_14*(3.14/ 180))}')


Resolução Exercicio 15:
Leia um angulo em radianos e apresente-o convertido em graus. Adote π como 3.14

exercicio_15 = float((input('Digite o valor em radianos e será convertido em graus. \nRadianos: ')))
print(f'Graus: {(exercicio_15*(180/ 3.14))}')


Resolução Exercicio 16:
Leia o valor de um comprimeiro em radianos e apresente-o convertido em polegadas

exercicio_16 = float((input('Digite o valor em centimetros e será convertido em polegadas. \nCentimetros: ')))
print(f'Polegadas: {exercicio_16/ 2.54}')


Resolução Exercicio 17:
Leia o valor de um comprimeiro em polegadas e apresente-o convertido em radianos

exercicio_17 = float((input('Digite o valor em polegadas e será convertido em centimetros. \nPolegadas: ')))
print(f'Centimetros: {exercicio_17* 2.54}')


Resolução Exercicio 18:
Leia um valor em litros e presente-o em metros cúbicos

exercicio_18 = int((input('Digite o valor em L e será convertido em M³. \nM³: ')))
print(f'Litros: {exercicio_18* 1000}')


Resolução Exercicio 19:
Leia um valor em metros cúbicos e presente-o em litros

exercicio_19 = int((input('Digite o valor em M³ e será convertido em L. L: ')))
print(f'Metros cúbicos: {exercicio_19/ 1000}')
..

Resolução Exercicio 20:
Leia um valor de massa em quilogramas e apresente-o convertido em libras

exercicio_20 = int((input('Digite o valor em Quilogramas e será convertido em Libras. \nLibras:')))
print(f'Libras: {exercicio_20/ 0.45}')


Resolução Exercicio 21:
Leia um valor de massa em libras e apresente-o convertido em quilogramas

exercicio_21 = int((input('Digite o valor em Libras e será convertido em Quilogramas. \nQuilograma:')))
print(f'Libras: {exercicio_21* 0.45}')


Exercicio 28:
Faça a leitura e de três numeros reais e apresente a soma dos quadrados

print("Digite três numeros reais e será apresentado a soma dos quadradros dos numeros.")
valor1 = int(input('Digite valor 1: '))
valor2 = int(input('Digite valor 2: '))
valor3 = int(input('Digite valor 3: '))
print(f'A soma dos quadrados é: {(valor1** 2) + (valor2** 2) + (valor3** 2)}')


Exercicio 29:
Leia quatro notas, calcule a média aritimetica e imprima o resultado (exercicio feito após o termina do curso)

lista = []
for i in range(4):
    lista.append(int(input(f'Digite a {i+1}º nota: ')))
media_a = sum(lista)/len(lista)
print(media_a)

Exercicio 30 não vou fazer, é apenas conversão de valores. Já teve até demais.


Exercicio 31:
Leia um numero inteiro e retorne seu sucessor e antecessor.

exercicio_31 = int(input('Digite um numero inteiro, será retornado seu antecessor e sucessor.\nNumero: '))
print(f'Antecessor: {exercicio_31-1}\nSucessor: {exercicio_31+1}')


Exercicio 32:
Leia um numero interiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro

exercicio_32 = int(input('Digite um numero inteiro para retonar o triplo de seu sucessor, mais o antecessor de'
                         'seu dobro. Valor:  '))
print(f'Resultado: {(((exercicio_32*3)+1)+ ((exercicio_32*2)-1))}')

#Exercicio 33 e 34 é apenas area de quadrado e circulo. Fiz muito disso em c


Resolucao exercicio 35:

#import math

print("Digite o valor dos catetos 'a' e 'b' para que seja calculada a hipotenusa.")
a = int(input('Cateto a: '))
b = int(input('Cateto b: '))
exercicio_35 = ((a ** 2) + (b ** 2))
exercicio_35 = (exercicio_35 ** 0.5)   # mais facil tirar a raiz por ** 0.5 do que import math
#print(f'A hipotenusa é: {math.sqrt(exercicio_35)}')
print(f'A hipotenusa é: {exercicio_35}')


# Exercicio 36 vou pular é apenas volume de cilindro area * (raio ** 2 ) * altura
# Exercicio 37, 38 vou pular é apenas porcetagem, multiplicar valor total por porcetagem.

Exercicio 39:
A importancia de 780 mil será dividade entre três ganhadores de um concurso. Sendo ganhador a 46%, b 32% e c o restante.

premio = 780_000
a = 0.46 * premio
b = 0.32 * premio
c = (1 - 0.46 - 0.32) * premio

print(f'O ganhador a recebeu: {a}\nO ganhador b recebeu: {b}\nO ganhador c recebeu: {round(c, 1)}')


Resolução Exercicio 40:

exercicio_40 = int(input('Digite a quantidade de dias trabalhados e irá retornar a quantidade o valor líquido do '
                         'salário e o imposto retido. Dias trabalhados: '))
print(f'Salário líquido: {round((exercicio_40*0.92*30), 3)}. Imposto retido:{round((exercicio_40*0.08*30), 3)}.')


# Irei pular exercicios 41 a 43, apenas porcetagem

Exercicio 44
Recebe a alutra do degrau de uma escada e a altura que o usuário deseja alcançar subindo a escada. Calcule e mostre
quantos degraus o usuário deverá subir para atingir seu objetivo.

degrau = float(input('Digite a altura do degrau em centimetros: ')) / 100
altura = float(input('Digite a altura em metros que deseja alcançar: '))

quant_degraus = altura // degrau
resto = altura % degrau

print(f'Deverá ter {quant_degraus} degraus e faltou {resto} para se chegar a altura desejada.')


Exercicio 45:
Faça um programa para converter uma letra maiscula em letra minuscula. Use a tablela ASCII para resolver o problema

exercicio_45 = input('Digite uma letra maiuscula e será retornado-a minuscula: ')
exercicio_45 = (ord(exercicio_45) + 32)
exercicio_45 = chr(exercicio_45)
print(exercicio_45)


Resolução Exercicio 46:
Faça um programa que leia um numero inteiro positivo de três digitos (de 100 a 000)

exercicio_46 = int(input('Digite uma sequencia de numeros entre 100 e 999 e, será devolvida seu inverso: '))
while (exercicio_46 < 100) or (exercicio_46 > 999):
    exercicio_46 = int(input('Digite novamente, deverá ser entre 100 e 999: '))
print(f'Inverso: {(str(exercicio_46)[::-1])}')


Resolução Exercicio 47:
Leia um numero de 4 dígitos (de 1000 a 9999) e imprima um dígito por linha

exercicio_47 = input('Digite um numero(de 1000 a 9999) para ser impresso: ')
while (int(exercicio_47) < 1000) or (int(exercicio_47) > 9999):
    exercicio_47 = input('Digite novamente, numero fora do limite: ')
for letra in exercicio_47:
    print(f'{letra}')


Exercicio 49:

hora_inicial = input('Digite o horario do inicio do experimento, no formato 00:00:00: ')
duracao = int(input('Digite a duração do experimento em segundos: '))
h = (int(hora_inicial[0:2]) * 3600)
m = (int(hora_inicial[3:5]) * 60)
s = int(hora_inicial[6:8])

nova_hora = h + m + s + duracao
hora = int((nova_hora/3600))
minuto = int((nova_hora-h)/60)
segundo = int((nova_hora-h-m))

print(f'O horario de termino é: {hora}:{minuto}:{segundo}')


# Resolução após estuda biblioteca datetime

import datetime

hora_inicial = input('Digite o horario do inicio do experimento, no formato 00:00:00: ')

duracao = datetime.timedelta(seconds=int(input('Digite a duração do experimento em segundos: ')))

hora_formatada = datetime.datetime.strptime(hora_inicial, '%H:%M:%S')

hora_final = (hora_formatada + duracao)

print(hora_final)

Exercicio 50:

premio = float(input('Digite o valor do premio da loteria: '))
compra = []
print('Informe quanto cada um dos três amigos pagou no bolão.')
for i in range(3):
    compra.append(float(input(f'O {i+1}º pagou: ')))

valor_bolao = sum(compra)
for i in range(3):
    porcetagem = (compra[i]/valor_bolao)
    recebido = premio * porcetagem
    print(f'O {i+1} amigo recebeu {recebido}, que equivale a {porcetagem*100}%')



"""














