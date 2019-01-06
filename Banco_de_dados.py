#! python3

# Autor: Jonas Henrique Nascimento
# W8jonas
#
# Automatize com Python
#
# Data da ultima att no código: 03/01/2019
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
    nome = "caralho"
    idade = 2
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
        dados_armazenados = dados_armazenados + nome + ';' + idade + ';'

    print('Saindo da gravação de dados e voltando para o menu.')
    print(f'Os dados gravados foram: {dados_armazenados}')

    programa()


def escrever_txt():
    ponteiro_txt = open(local, 'a')
    ponteiro_txt.write(dados_armazenados)
    ponteiro_txt.close()
    programa()


def escrever_bin():
    print('oi')


def ler_txt():
    ponteiro_txt = open(local, 'r')
    print(ponteiro_txt.read())
    ponteiro_txt.close()
    programa()


def ler_bin():
    db = open(local, 'r')
    print(db.read())


local = os.getcwd()
local = os.path.join(local, 'DataBase.txt')

dados_armazenados = ""
print(local)

continuar = input(print("deseja continuar?"))
continuar.upper()
if continuar == 'S' or "SIM" or 'Y' or 'YES':
    programa()
