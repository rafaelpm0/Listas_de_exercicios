"""
Resolução Exercicio 01:
Faça um programa que possua um vetor denominado A que armazene 6 números inteiros. O programa deve executar
os seguintes passos:

1 - Adicionar 6 elementos a esse vetor A:
2 - Armazena em uma variável a soma dos vetores nos respectivo indices 0, 1 e 5.
3 - Atribuir ao indice 4, o valor 100.
4 - Mostrar o valor do vetor A em cada linha.

a = []

a.extend([1, 0, 5, -2, -5, 7])
print(a)

b = a[0] + a[1] + a[5]
print(b)

a[4] = 100
print(a)


Exercicio 2:
Crie um programa que lê 6 valores e, em seguida mostre na tela os valores lidos

#forma 1

a = []
b = 0

for i in range(0, 6):
    b = int(input(f'Numero {i}: '))
    a.append(b)

print(a)

#forma 2

a = []

while len(a) < 6:
    b = int(input(f'Numero {len(a)}: '))
    a.append(b)

print(a)

Exercicio 3:
Lê 10 números e calcular o quadrado deles e armazenar em outro vetor

num = []
quadrado = []
entrada = 0

for i in range(0, 10):
    entrada = input(f'Digite o {i+1}º numero: ')

    while not entrada.isnumeric():
        entrada = input(f'Digite o {i+1}º numero, lembrando de ser real e use ponto ao inves de virgula: ')

    num.append(float(entrada))
    quadrado.append(float(entrada) ** 2)

for i in range(0, 10):
    print(f'O {i+1}º numero foi de {num[i]} e seu quadrado é {quadrado[i]}')

# apos curso

num = [int(input()) for _ in range(10)]
lista = [{x: x**2} for x in num]
print(num)    #não vou fazer os textos, apenas reduzi as coisas
print(lista)


Exercicio 4:
 Faça um programa que leia um vetor de 8 posições e, em seguida, leia também dois valores X e Y quaisquer
 correspondentes a duas posições no vetor. Ao final seu pograma deverá escrever a soma dos valores encontrados nas
pesperctivas posições X e Y.

vetor = []
soma = []

for i in range(8):
    vetor.append(int(input(f'Digite o {i} numero: ')))

print('Digite duas posições nos vetores para somar seus valores:')

for c in range(2):
    soma.append(int(input(f'Escolha a {c} posição: ')))

print(f'A soma é de: {vetor[soma[0]] + vetor[soma[1]]}')


Exercico 5:
Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele possui

def numerico(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


array = []
entrada = 0

for i in range(10):
    entrada = input(f'Digite o {i+1} numero real: ')
    while numerico(entrada) is False:
        if entrada.isnumeric():
            pass
        else:
            entrada = input('Numero real invalido, troque a virugala por ponto: ')
    if int(entrada) % 2 == 0:
        array.append(entrada)

    print(f'Os Numeros pares foram: {array}')

#Não sei que merda eu tava na cabeça, mas segue uma resolução decente

entrada = [int(input(f'Informe um numero {x+1}º: ')) for x in range(10)]
entrada = len([x for x in entrada if (x % 2) == 0])
print(f'O numero de numeros pares é de {entrada}')


Exercicio 6:
Faça um vetor com 10 posições. Imprima o maior e menor numero

import random
vetor = []

for i in range(10):
    vetor.append(random.randint(1, 100))

print(vetor)
print(f'O maior valor é {max(vetor)} e o menor {min(vetor)}')


Exercicio 7:
Escreva um programa que leia 10 numeros inteiros e os armazene em um vetor. Imprima o vetor, o maior elemente e a
posição que ele se encontra

import random
vetor = []

for i in range(10):
    vetor.append(random.randint(1, 100))

print(vetor)
print(f'O maior valor é {max(vetor)} na posição {vetor.index(max(vetor))} e o menor {min(vetor)} na posição'
      f' {vetor.index(min(vetor))}')



Exercicio 8:
Crie um programa que lê 6 numeros inteiros e, em seguida, mostre na tela os valores lidos na ordem inversa


vetor = []

for i in range(6):
    vetor.append(input('Digite um numero: '))

print(vetor[::-1])


Exercicio 9:
Crie um programa que le 6 valores interios pares e, em mostre na tela os valores invertidos

vetor = []

for i in range(6):
    entrada_par = int(input('Digite um numero par: '))
    if (entrada_par % 2) == 0:
        vetor.append(int(entrada_par))
    else:
        pass

print(vetor[::-1])


Exercicio 10:
Faça um para ler a nota da prova de 15 alunos e, armazene num vetor. Calcule e imprima a media geral


def numerico(x):
    try:
        int(x)
        return True
    except ValueError:
        return False


vetor = []
entrada = 0

for i in range(15):
    entrada = input(f'Entre com a nota do {i+1}º aluno: ')

    while numerico(entrada) is False:
        if numerico(entrada):
            break
        else:
            entrada = input(f'Entre com a nota do {i+1}º aluno, digite um numero real positivo: ')

    vetor.append(int(entrada))

print(f'A media foi de : {round(sum(vetor)/len(vetor), 2)}')


Exercicio 11:
Faça um programa que preencha um vetor com 10 numeros reais, calcule e mostre a quantidade de numeros negativos
e a soma dos numeros positivos

import random
vetor = []
soma = 0
neg = 0

for i in range(10):
    vetor.append(random.randint(-100, 100))

for a in vetor:
    if a >= 0:
        soma += a
    else:
        neg += 1

print(f'A soma dos positivos é {soma} e a quantidade de negativos é {neg}')
print(vetor)


Exercicio 12:
Faça um programa ler 5 valores e, em seguida, mostrar todos os valores lidos juntamente com o maior, o menor
e a média dos valores

array = []


for i in range(5):
    array.append(float(input(f'Digite um numero. {i+1}/5: ')))

print(f'O maior numero foi de {max(array)}, o menor de {min(array)} e a media foi de {sum(array)/5}')


Exercicio 13:
Faça um programa ler 5 valores e, em seguida, mostrar todos os valores lidos juntamente com o maior e o menor


array = []


for i in range(5):
    array.append(input(f'Digite um numero. {i+1}/5: '))
for a in range(5):
    array[a] = int(array[a])

print(f'O maior numero esta na posição {array.index(max(array))}, o menor numero esta na posição'
      f' {array.index(min(array))}')


Exercicio 14:
Faça um progama que leia 10 posições e verifique se existem valores iguais e os escreva na tela


vetor = []
duplicado = set()

for i in range(10):
    vetor.append(input(f'Digite {i+1}/10 valores e será retornado se há numeros iguais: '))

for valor in vetor:
    if vetor.count(valor) >= 2:
        duplicado.add(valor)

print(f'Os valores duplicados foram: {duplicado}')


Exercicio 15:
Leia um vetor com 20 números inteiros. Escreva os elementos do vetor eliminando elementos repetidos

vetor = []


for i in range(20):
    vetor.append(int(input(f'Digite um numero inteiro {i+1}/20: ')))

unicos = set(vetor)

print(f'Os numeros unicos são: {unicos}')


Exercicio 16:
Faça um programa que leia um vetor de 5 posições e depois um código inteiro. Se for 1, mostre o vetor na ordem direta;
se for 2, mostre o vetor na ordem inversa. Caso o código seja diferente de 1 ou 2, escreva uma mensagem informando
que o código é inválido.

vetor = []
menu = 0

for i in range(5):
    vetor.append(input(f'Digite um numero real, {i + 1}/5: '))

menu = input('Digite [1] para ver os valores digitados na ordem direta. Digite [2] para ver os valores digitados na'
             'ordem inversa.\nMenu: ')

while (menu != '1') and (menu != '2'):
    menu = input('Valor invalido. Digite novamente: ')

if menu == '1':
    print(vetor)
elif menu == '2':
    vetor.reverse()
    print(vetor)


Exercicio 17:
Leia um vetor de 10 posições e atribua o valor 0 para todos os elementos negativos

import random
vetor = []
entrada = 0

for i in range(10):
    entrada = random.randint(-100, 100)
    print(entrada)  # para verificar quais o numeros negativos
    if entrada < 0:
        vetor.append(0)
    else:
        vetor.append(entrada)
print(vetor)    # para verificar se o resultado esta como esperado


Exercicio 18:
Faça um programa que leia um vetor de 10 numeros. Leia um número x. Conte os múltiplos de um número inteiro x num
vetor e mostre-os na tela


import random
vetor = []
conta = 0

for i in range(10):
    vetor.append(random.randint(1, 100))

entrada = int(input('Digite um numero e será verificado seus multiplos em 10 numeros aleatórios: '))

for x in vetor:
    if x % entrada == 0:
        print(f'Numeros multiplo: {x}')
    else:
        conta += 1
if conta == 10:
    print(f'Nenhum numero é multiplo')


Exercicio 19:
Faça um vetor de tamanho 50 preenchido com o seguite valor (i+5 *i)%(i+1). Sendo i a posição do elemento no vetor.
Em seguida imprima o valor na tela

vetor = []

for i in range(0, 50):
    vetor.append((i+5*i) % (1+i))
print(vetor)


Exercicio 20:
Escreva um programa que leia números inteiros no intervalor de [0,50] e os armazene em um vetor de 10 posições.
Preencha um segundo vetor com apenas os números ímpares do primeiro vetor. Imprima os dois vetores, 2 elementos por
linha

import random
impar = []


vetor = [random.randint(0, 50) for _ in range(50)]

for i in vetor:
    if i % 2 != 0:
        impar.append(i)

print(f'Lista: {vetor}\nNumeros impares: {impar}')


Exercicio 21:
Faça um programa que receba do usuário dois vetores A e B, com 10 números inteiros cada. Crie um novo vetor denominado
C calculado C = A - B. Mostre na tela os dados do vetor C


import random

a = random.sample(range(0, 20), 10)
b = random.sample(range(0, 20), 10)
c = []

for i in range(0, 10):
    c.append((a[i] - b[i]))

print(f'Lista a {a}\nLista b {b}\ne Lista c (a-b): {c}')

Exercicio 22:


import random

a = random.sample(range(0, 20), 10)
b = random.sample(range(0, 20), 10)
c = []
contaa = 0  # Contador do indice a e b, tentei usar uma lista, mas ele não aceita lista como indexador de uma lista
contab = 0


for i in range(0, 20):
    if i % 2 == 0:
        c.append(a[contaa])
        contaa += 1
    else:
        c.append(b[contab])
        contab += 1

print(a)
print(b)
print(c)

Exercicio 23:

import random

x = random.sample(range(0, 50), 5)
y = random.sample(range(0, 50), 5)


print(x)
print(y)

for i in range(0, len(x)):

    print(f'O produto escalar de indice {i} é {x[i] * y[i]}')

Exercicio 24:

import random

alunos = {}  # Dicionario  para armazear os valores

for i in range(10):
    alunos[i+1] = random.uniform(1.40, 2.10).__round__(2)

print(alunos)

for chave, valor in alunos.items():
    if valor == max(alunos.values()):
        print(f'O indice do maior aluno é o {chave}º da lista com  altura {valor}.')
    elif valor == min(alunos.values()):
        print(f'O menor aluno é o {chave}º da lista com altura de {valor}')

Exercicio 25:

def ultimo7(x):
    x = str(x)
    if x[(len(x)-1):(len(x)+1)] == '7':
        return False
    else:
        return True


conta = 0
array = []


while len(array) < 100:
    if (conta % 7 != 0) and ultimo7(conta):
        array.append(conta)
    conta += 1

print(array)

Exercicio 26:

import random


numero = random.sample(range(1, 50), 2)
media = sum(numero)/len(numero)
somatorio = []
resultado = 0

for i in numero:
    somatorio.append((i - media) ** 2)

resultado = ((1/(len(numero)-1)) * sum(somatorio)) ** 0.5

print(resultado)

Exercicio 27:

import random

vetor = random.sample(range(1, 11), 10)
count = 0

print(vetor)

for i in vetor:
    if i == 1:
        print(f'O numero {i} é primo e seu indexador é {vetor.index(i)}')
    for a in range(1, 11):
        if (i % a) == 0:
            count += 1
    if count == 2:
        print(f'O numero {i} é primo e seu indexador é {vetor.index(i)}')
    count = 0

Exercicio 28:

import random


v = []
v1 = []
v2 = []

for i in range(0, 10):
    v.append(random.randint(0, 100))
    if v[i] % 2 == 0.00:
        v2.append(i)
    else:
        v1.append(i)

print(f'Foram armazeados {len(v1)} elementos impares em v1, sendo eles: {v1}')
print(f'Foram armazeados {len(v2)} elementos pares em v1, sendo eles: {v2}')

Exercicio 29 -  não vou fazer, mistura preguiçosa de outros exercicios

Exercicio 30:

import random

a = set(random.sample(range(1, 50), 10))
b = set(random.sample(range(1, 50), 10))

print(a)
print(b)

print(a.intersection(b))

Exercicio 31:

import random

a = set(random.sample(range(1, 50), 10))
b = set(random.sample(range(1, 50), 10))

print(a)
print(b)

print(a.union(b))

Exercicio 32:

import random

a = random.sample(range(1, 100), 5)
b = random.sample(range(1, 100), 5)

for i in range(len(a)):
    print(f'A soma dos numeros de posição {i+1} é de {a[i]+b[i]}')
    print(f'A multiplicacao dos numeros de posição {i + 1} é de {a[i] * b[i]}')

print(f'A diferença dos vetores é de {set(a).difference(set(b))}')
print(f'A união dos vetores é de {set(a).union(set(b))}')
print(f'A interseção dos vetores é de {(set(a).intersection(set(b)))}')

Exercicio 33:

import random

a = []

for i in range(15):
   a.append(random.randint(0, 5))

print(a)

for i in a:
    if i == 0:
        a.pop(a.index(i))

print(a)

Exercicio 34:

vetor = []
entrada = 0
contador = 0

for c in range(10):
    if len(vetor) == 0:
        entrada = int(input('Digete um numero real: '))
        vetor.append(entrada)
    else:
        entrada = int(input('Digete um numero real: '))
        for b in range(len(vetor)):
            if vetor[b] != entrada:
                contador += 1
        if contador != len(vetor):
            while contador != len(vetor):
                contador = 0
                entrada = int(input('Numero repitido, digite outro: '))
                for d in range(len(vetor)):
                    if vetor[d] != entrada:
                        contador += 1

        vetor.append(entrada)
        contador = 0

print(vetor)

Exercicio 35:

a = int(input('Informe um número menor que 10000: '))
b = int(input('Informe outro número menor que 10000: '))

vetor_a = []
vetor_b = []


if a < 10_001 and b < 10_001:
    a = str(a)
    b = str(b)

    for v in a:
        vetor_a.append(int(v))

    for c in b:
        vetor_b.append(int(c))

    vetor_a.sort()
    vetor_b.sort()

    print(f'A soma de {vetor_a} com {vetor_b} é de {sum(vetor_a) + sum(vetor_b)}')

else:
    print('Valores informados incorretos')

Exercicio 36:
import random


vetor = random.sample(range(50), 10)
print(vetor)
vetor.sort()
print(vetor)

Exercicio 37:

import random


vetor = random.sample(range(0, 11), 11)
vetor_t = []

print(vetor)

vetor.sort()

print(vetor)

for des in range((len(vetor)-1), 5, -1):
    vetor_t.append(vetor[des])
    vetor.pop()

vetor.extend(vetor_t)

print(vetor)

Exercicio 38:

vetor = []

for i in range(10):
    vetor.append(int(input('Digite um numero 1/{i}: ')))
    vetor.sort()
    print(f'Valores ordenados: {vetor}')

Exercicio 39:

def fat(x):
    if x <= 1:  # Por ser triangulo de pascal foi preciso colocar <= assim corrige o valor zero do triangulo q é 1
        return 1
    else:
        return x*fat(x-1)


def pascal(linha, coluna):

    lin = fat(linha)
    col = fat(coluna)
    lc = fat(linha - coluna)

    return int(lin/(col * lc))


n = int(input('Digite o numero de linhas do triangulo de pascal: '))

for li in range(n):
    for co in range(li+1):
        print(pascal(li, co), end=' ')
    print('')

Exercicio 39 - Solução do coleguinha. OBS: exercictar mais matriz, fiz o mais dificil huehue

numero = int(input('Digite um numero: '))

matriz = [[x for x in range(numero)] for x in range(numero)]

for i in range(numero):
    for j in range(i + 1):
        if j == i or j == 0:
            matriz[i][j] = 1
        else:
            matriz[i][j] = matriz[i - 1][j - 1] + matriz[i - 1][j]

        print(matriz[i][j], end=' ')
    print()

A PARTIR DAQUI É TUDO EXERCICIO PARTE 2

Exercicio 1:

import random

matriz = []
contador = 0

for lin in range(4):
    temp = []
    for col in range(4):
        temp.append(random.randint(1, 20))
        if temp[col] > 10:
            contador += 1
    matriz.append(temp)


print(matriz)
print(f'Nesta matriz existem {contador} maiores que 10')

Exercicio 02:
matriz = []

for linha in range(5):
    temp = []
    for coluna in range(5):
        if linha == coluna:
            temp.append(1)
        else:
            temp.append(0)

    matriz.append(temp)

for a in matriz:
    print(a)

Exercicio 03:

t = []

for linha in range(5):
    temp = []
    for coluna in range(5):
        temp.append(linha*coluna)
    t.append(temp)
print(t)

Exercicio 4:

import random

matriz = []
n = int(input('Digite um numero para gerar uma matriz X - X aletoria e retornar o maior valor: '))

for linha in range(n):
    temp = []
    for coluna in range(n):
        temp.append(random.randint(1, 200))
    matriz.append(temp)

temp.clear()

for linha in range(2):
    temp = [0, 0, 0]
    for coluna in range(2):
        if matriz[linha][coluna] > temp[2]:
            temp = [linha, coluna, matriz[linha][coluna]]

print(matriz)
print(f' O maior numero foi {temp[2]}, na linha {temp[0]} e coluna {temp[1]}')

Outra forma de resolver coleguinha

import random

matriz = []
n = 4

for linha in range(n):
    temp = []
    for coluna in range(n):
        temp.append(random.randint(1, 200))
    matriz.append(temp)


print(matriz)
maior = max(max(linha) for linha in matriz)

Outro coleguinha precoce (porra conteudo de 2 unidades na frente, não fode!!)

import random

matriz = []
n = 4

for linha in range(n):
    temp = []
    for coluna in range(n):
        temp.append(random.randint(1, 200))
    matriz.append(temp)


print(matriz)
maior = max(max(linha) for linha in matriz)
posicao = [str(matriz.index(linha)) + str(linha.index(n)) for linha in matriz for n in linha if n == maior]

print(maior, posicao)

Exercicio 5:

matriz = [list(range(5)), list(range(5, 10)), list(range(10, 15)), list(range(15, 20)), list(range(20, 25))]

n = int(input('Digite um numero de 0 a 24 para buscar na lista e será informada sua posição: '))

contador = 0

for linha in range(5):
    for coluna in range(5):
        if matriz[linha][coluna] == n:
            print(f'Posição do numero, linha {linha} e coluna {coluna}')
        else:
            contador += 1

if contador != 24:
    print('Valor não encontrado')

Exercicio 6:

import random

matriz_1 = [[random.randint(1, 10) for coluna in range(4)] for linha in range(4)]
matriz_2 = [[random.randint(1, 10) for coluna in range(4)] for linha in range(4)]
matriz_r = []

for linha in range(4):
    temp = []
    for coluna in range(4):
        if matriz_1[linha][coluna] >= matriz_2[linha][coluna]:
            temp.append(matriz_1[linha][coluna])
        else:
            temp.append(matriz_2[linha][coluna])
    matriz_r.append(temp)

print(matriz_1, end='\n')

print(matriz_2, end='\n')
print(matriz_r, end='\n')

Exercicio 7:


matriz = []

for linha in range(10):
    temp = []
    for coluna in range(10):
        if linha < coluna:
            temp.append((2*linha + 7*coluna - 2))
        elif linha == coluna:
            temp.append((3* linha**2 - 1))
        else:
            temp.append((4 * linha**3 - 5 * coluna ** 2 + 1))
    matriz.append(temp)


for linha in matriz:
    print(linha)

Exercicio 8:


import random


matriz = [[random.randint(1, 5) for coluna in range(3)] for linha in range(3)]
posi = [0, 1]
soma = 0

for linha in range(3):
    for coluna in range(3):
        if linha == posi[0] and coluna == posi[1]:
            soma += matriz[linha][coluna]
            posi[0] += 1
            posi[1] += 1

for i in matriz:
    print(i)

print(soma)

Exercicio 9:


import random


matriz = [[random.randint(1, 5) for coluna in range(3)] for linha in range(3)]
posi = [1, 0]
soma = 0

for linha in range(3):
    for coluna in range(3):
        if linha == posi[0] and coluna == posi[1]:
            soma += matriz[linha][coluna]
            posi[0] += 1
            posi[1] += 1

for i in matriz:
    print(i)

print(soma)

Exercicio 10:


import random


matriz = [[random.randint(1, 5) for coluna in range(3)] for linha in range(3)]
posi = [0, 0]
soma = 0

for linha in range(3):
    for coluna in range(3):
        if linha == posi[0] and coluna == posi[1]:
            soma += matriz[linha][coluna]
            posi[0] += 1
            posi[1] += 1

for i in matriz:
    print(i)

print(soma)

Exercicio 11:

import random


matriz = [[random.randint(1, 5) for coluna in range(3)] for linha in range(3)]
posi = [0, 2]
soma = 0

for linha in range(3):
    for coluna in range(3):
        if linha == posi[0] and coluna == posi[1]:
            soma += matriz[linha][coluna]
            posi[0] += 1
            posi[1] -= 1

for i in matriz:
    print(i)

print(soma)

Exercicio 12:

import random

matriz = [[random.randint(1, 20) for coluna in range(3)] for linha in range(3)]
matriz_t = []


for linha in range(len(matriz)):
    temp = []
    for coluna in range(len(matriz)):
        temp.append(matriz[coluna][linha])

    matriz_t.append(temp)

for i in matriz:
    print(i)

print('')

for i in matriz_t:
    print(i)

Exercicio 13:

matriz = []
num = 0

for linha in range(4):
    temp = []
    for colina in range(4):
        temp.append(num)
        num += 1

    matriz.append(temp)

for i in matriz:
    print(i)

for linha in range(4):
    for colina in range(4):
        if colina > linha:
            matriz[linha][colina] = 0

print('')
for i in matriz:
    print(i)

Exercicio 14:

matriz = []
num = 0

for linha in range(10):
    temp = []
    for colina in range(10):
        temp.append(num)
        num += 1

    matriz.append(temp)

for i in matriz:
    print(i)

Exercicio 15:

import random


resp_a = [[chr(random.randint(97, 100)) for _ in range(10)] for _ in range(5)]
resp_g = [chr(random.randint(97, 100)) for _ in range(10)]
pontuacao = []


for linha in range(len(resp_a)):
    conta = 0
    for coluna in range(len(resp_g)):
        if resp_a[linha][coluna] == resp_g[coluna]:
            conta += 1
        else:
            pass
    pontuacao.append(conta)

print(f'O gabarito é {resp_g}')

for i in range(len(pontuacao)):
    print(f'O aluno {i+1} obeteve a pontuação {pontuacao[i]}')

Exercicio 16:


import random


resp_a = [[chr(random.randint(97, 100)) for _ in range(10)] for _ in range(3)]
resp_g = [chr(random.randint(97, 100)) for _ in range(10)]
pontuacao = {}


print(resp_a)

for linha in range(len(resp_a)):
    conta = 0
    for coluna in range(len(resp_g)):
        if resp_a[linha][coluna] == resp_g[coluna]:
            conta += 1
        else:
            pass
    if linha == 0:
        pontuacao['aluno_1'] = [resp_a[0], conta]
    elif linha == 1:
        pontuacao['aluno_2'] = [resp_a[1], conta]
    else:
        pontuacao['aluno_3'] = [resp_a[2], conta]


print(f'O gabarito é {resp_g}')

for i, b in pontuacao.items():
    if b[1]/7 >= 1:
        print(f'O aluno {i} obeteve a pontuação {b[1]}, e foi aprovado')
    else:
        print(f'O aluno {i} obeteve a pontuação {b[1]}, e foi reprovado')


Exercicio 17  (não é oque o exercicio pediu...):

import random


def nota(x, a, b):
    ponto = 0
    for i in range(x):
        if a[i] == b[i]:
            ponto += 1
    return ponto


resp_a = [[chr(random.randint(97, 100)) for _ in range(10)] for _ in range(9)]
pontuacao = {'aluno_1': [resp_a[0], resp_a[1], resp_a[2]], 'aluno_2': [resp_a[3], resp_a[4], resp_a[5]],
             'aluno_3': [resp_a[6], resp_a[7], resp_a[8]]}
resp_g = [[chr(random.randint(97, 100)) for _ in range(10)] for _ in range(3)]


for prova in range(len(resp_g)):
    pontuacao['aluno_1'][prova] = nota(10, pontuacao['aluno_1'][prova], resp_g[prova])
    pontuacao['aluno_2'][prova] = nota(10, pontuacao['aluno_2'][prova], resp_g[prova])
    pontuacao['aluno_3'][prova] = nota(10, pontuacao['aluno_3'][prova], resp_g[prova])

    if (pontuacao['aluno_1'][prova] < pontuacao['aluno_2'][prova]) and (pontuacao['aluno_1'][prova] < pontuacao['aluno_3'][prova]):
        print(f"A menor nota foi do aluno 1, sendo {pontuacao['aluno_1'][prova]}")
    elif (pontuacao['aluno_2'][prova] < pontuacao['aluno_1'][prova]) and (pontuacao['aluno_2'][prova] < pontuacao['aluno_3'][prova]):
        print(f"A menor nota foi do aluno 2, sendo {pontuacao['aluno_2'][prova]}")
    else:
        print(f"A menor nota foi do aluno 3, sendo {pontuacao['aluno_3'][prova]}")


Exercicio 17 CORRETO:

import random
from collections import Counter

notas = [[random.randint(0, 10) for _ in range(3)] for _ in range(3)]


for i in range(3):
    temp = Counter(notas[i])
    print(f' {min(temp.values())} Alunos tirarm {min(temp.keys())} na prova {i}')

Exercicio 18:

import random

matriz = [[random.randint(-10, 10) for _ in range(3)] for _ in range(3)]
soma = []

for linha in range(len(matriz)):
    temp = 0
    for coluna in range(len(matriz)):
        temp += matriz[coluna][linha]

    soma.append(temp)


for i in matriz:
    print(i)

print(f'A soma foi de {soma}')


Vou pular a 19, só enche o saco.

Exercicio 20:

import random

matriz = [[random.randint(1, 50) for _ in range(3)]for _ in range(6)]
soma_i = 0
soma_2_e_4 = 0


for i in matriz:
    print(i)

for linha in range(len(matriz)):
    for coluna in range(len(matriz[0])):
        if coluna % 2 != 0:
            soma_i += matriz[linha][coluna]
        if coluna == 2 or coluna == 4:
            soma_2_e_4 += matriz[linha][coluna]
        if coluna == 2:
            matriz[linha][2] = (matriz[linha][0] + matriz[linha][1])

print(f'A soma das colunas impares é: {soma_i}')
print(f'A soma dos valores da 2 e quarta coluna é: {soma_2_e_4}')
print(f'Substitiuindo a sexta coluna pela soma da coluna um e dois temos: ')
for i in matriz:
    print(i)

Exercicio 21:

import random

matriz_a = [[random.randint(1, 10) for _ in range(2)] for _ in range(2)]
matriz_b = [[random.randint(1, 10) for _ in range(2)] for _ in range(2)]
matriz_c = [[0 for _ in range(2)] for _ in range(2)]


def menu():
    x = int(input('\nEscolha a operacao: \n[1] Para soma as duas matrizes abaixo. \n[2] Para subtrair a primeira da '
                  'segunda.\n[3] Adicionar uma constante as duas matrizes. \n[4] Imprimir as matrizes. '
                  '\n[5] Encerar programa.\nOperacao:  '))

    while x != 5:

        print('')

        if x == 1:  # soma
            for linha in range(len(matriz_a)):
                for coluna in range(len(matriz_a)):
                    matriz_c[linha][coluna] = (matriz_a[linha][coluna] + matriz_b[linha][coluna])
                print(matriz_c[linha])

        elif x == 2:  # subtracao
            for linha in range(len(matriz_a)):
                for coluna in range(len(matriz_a)):
                    matriz_c[linha][coluna] = (matriz_a[linha][coluna] - matriz_b[linha][coluna])
                print(matriz_c[linha])

        elif x == 3:  # adicionar uma constante
            const = int(input('Digite uma constante para ser para ser adicionada nas duas matrizes: '))
            for linha in range(len(matriz_a)):
                for coluna in range(len(matriz_a)):
                    matriz_a[linha][coluna] += const
                    matriz_b[linha][coluna] += const

            for i in range(len(matriz_a)):
                print(matriz_a[i], ' ' * 10, matriz_b[i])

        elif x == 4:

            for i in range(len(matriz_a)):
                print(matriz_a[i], ' ' * 10, matriz_b[i])

        x = int(
            input('\nEscolha a operacao: \n[1] Para soma as duas matrizes abaixo. \n[2] Para subtrair a primeira da '
                  'segunda.\n[3] Adicionar uma constante as duas matrizes. \n[4] Imprimir as matrizes. '
                  '\n[5] Encerar programa.\nOperacao:  '))


print('Matrizes iniciais:\n')

for i in range(len(matriz_a)):
    print(matriz_a[i], ' ' * 10, matriz_b[i])
print('')

menu()


for i in range(len(matriz_a)):
    print(matriz_a[i], 'x', ' ' * 10, matriz_b[i], ' ' * 10, '=', matriz_c[i])


Exercicio 22:

import random


matriz_a = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]
matriz_b = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]
matriz_c = []


for linha in range(len(matriz_a)):
    temp = []
    for coluna in range(len(matriz_a)):
        soma = 0
        for lateral in range(len(matriz_a)):
            soma += (matriz_a[linha][lateral] * matriz_b[lateral][coluna])
        temp.append(soma)

    matriz_c.append(temp.copy())
    temp.clear()

for i in range(len(matriz_a)):
    print(matriz_a[i], 'x', ' ' * 10, matriz_b[i], ' ' * 10, '=', matriz_c[i])


Exercicio 23:

import random

matriz_a = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]
matriz_c = []

print(len(matriz_a))

for linha in range(len(matriz_a)):
    temp = []
    for coluna in range(len(matriz_a)):
        soma = 0
        for inverso in range(len(matriz_a)):
            print(linha, coluna, inverso)
            soma += (matriz_a[linha][inverso] * matriz_a[inverso][coluna])
        temp.append(soma)
    matriz_c.append(temp.copy())

for i in range(len(matriz_a)):
    print(matriz_a[i], ' ' * 10, matriz_c[i])



"""

matriz = [[8, 2, 22, 97, 38, 15, 00, 40, 00, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
          [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0],
          [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
          [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
          [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
          [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
          [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
          [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
          [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
          [21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95],
          [78, 1, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
          [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57],
          [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
          [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
          [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
          [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
          [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
          [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
          [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
          [61, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]]

'A função abaixo irá localizar qualquer conbinação de produtos desejada, tendo uma condição de parada e quais ' \
'produtos multiplica. Assim temos que informar a matriz, a condicação de parada, o passo da linha e o passo da coluna'


lin = 0
col = 0


def loc_maior(tamanho, t):
    dados = [[0, 0, 0]]

    for linha in range(len(tamanho)):
        for coluna in range(len(tamanho)):
            produto = 1
            x = int(linha)
            y = int(coluna)

            cond = [coluna + 3 < 20, coluna - 3 >= 0]
            passo = [[0, 1], [0, -1]]
            if cond[t]:
                for i in range(4):
                    if i == 0:
                        produto *= matriz[linha][coluna]
                    else:
                        x += passo[t][0]
                        y += passo[t][1]
                        produto *= matriz[x][y]

            if produto > dados[0][0]:
                dados[0][0] = produto
                dados[0][1] = linha
                dados[0][2] = coluna

    return dados


esquerda = loc_maior(matriz, 0)
direita = loc_maior(matriz, 1)


print(esquerda)
print(direita)