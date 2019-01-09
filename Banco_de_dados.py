#! python3

# Autor: Jonas Henrique Nascimento
# W8jonas
#
# Automatize com Python
#
# Data da ultima att no código: 09/01/2019
# tópico atual: Lendo e escrevendo em arquivos
#

import os
import shelve


def programa():
    print(""" Digite o que deseja fazer?
    1 - Armazenar valores.
    2 - Salvar valores em txt.
    3 - Salvar valores em bin.
    4 - Ler dados em txt.
    5 - Ler dados em bin.
    6 - Fechar programa.
    """)
    operacao = int(input())
    if operacao == 1:
        armazenar_valores()
    elif operacao == 2:
        escrever_txt()
    elif operacao == 3:
        escrever_bin()
    elif operacao == 4:
        ler_txt()
    elif operacao == 5:
        ler_bin()
    elif operacao == 6:
        exit()
    else:
        print("Operação inválida.")


def armazenar_valores():
    global dados_armazenados

    print("Para sair e voltar às opções iniciais digite 0 em um dos dois termos.")
    while True:
        nome = input(print('Digite um nome: '))
        if nome == '0':
            break
        idade = int(input(print('Digite uma idade: ')))
        if idade == 0:
            break
        idade = idade.__str__()
        dados_armazenados.append(nome + ';' + idade + ';')

    print('Saindo da gravação de dados e voltando para o menu.')
    print(f'Os dados gravados foram: {dados_armazenados}')
    programa()


def escrever_txt():
    numero = ultima_linha()
    ponteiro_txt = open(local, 'a')
    j = 0
    for i in dados_armazenados:
        j += 1
        ponteiro_txt.write((j + numero).__str__())
        ponteiro_txt.write(';')
        ponteiro_txt.write(i)
        ponteiro_txt.write('\n')
    ponteiro_txt.close()
    programa()


def escrever_bin():
    numero = ultima_linha()
    ponteiro_bin = shelve.open('database_bin')
    j = 0
    for i in range(0, len(dados_armazenados)):
        j += 1
        linha = (j + numero).__str__()
        ponteiro_dic = {linha: dados_armazenados[i]}
        ponteiro_bin[linha] = ponteiro_dic
        print(f'Linha = {linha} e dado armazenado = {dados_armazenados[i]}')
        print("ficando assim: ")
        print(ponteiro_bin[linha])
    ponteiro_bin.close()
    programa()


def ler_txt():
    ponteiro_txt = open(local, 'r')
    print(ponteiro_txt.read())
    ponteiro_txt.close()
    programa()


def ler_bin():
    total_linhas = ultima_linha()
    ponteiro_bin = shelve.open('database_bin')
    for i in range(5, total_linhas+1):
        print(i.__str__())
        print(ponteiro_bin[i.__str__()])
    ponteiro_bin.close()
    programa()


def ultima_linha():
    global ponteiro_txt_
    global valor
    try:
        print("TRY")
        ponteiro_txt_ = open(local, 'r')
        lista = ponteiro_txt_.readlines()
        frase = lista[len(lista) - 1]
        frase_2 = frase.split(';')
        valor = int(frase_2[0])

    except FileNotFoundError:
        print("File Not Found Error")
        ponteiro_txt_ = open(local, 'a')
        ponteiro_txt.write('0;Primeira linha;0\n')
        valor = 0

    except IndexError:
        print("Index Error")
        valor = 0

    finally:
        print("FINALLY")
        ponteiro_txt_.close()
    return valor


local = os.getcwd()
local = os.path.join(local, 'DataBase.txt')

dados_armazenados = []
print(local)

continuar = input(print("deseja continuar?"))
continuar.upper()

if continuar == 'S' or "SIM" or 'Y' or 'YES':
    programa()
else:
    exit()
