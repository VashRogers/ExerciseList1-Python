from src.data import comparar_datas
from src.email_acadêmico import criar_emails_acadêmicos
from src.matriz import gerar_diagonal_matriz, gerar_matriz_triangular
from src.seguro import obter_população_cidade
from src.util import carregar_arquivo_csv


def exercício4():
    print('\nExercício 4: ')

    cidade = obter_população_cidade('Fortaleza, 2686612')
    print('Cidade escolhida: ', cidade)

    pass


def exercício3():
    print('\nExercício 3: ')
    matriz_quadrada = [[1, 7, 3, 7, 2],
                       [9, 2, 4, 1, 6],
                       [4, 8, 2, 3, 5],
                       [8, 3, 5, 1, 7],
                       [4, 6, 1, 5, 9]]
    diagonal_matriz = gerar_diagonal_matriz(matriz_quadrada)
    print('A diagonal da matriz quadrada é: ', diagonal_matriz, '\n')

    matriz_triangular_superior = gerar_matriz_triangular(matriz_quadrada, 'superior')
    matriz_triangular_inferior = gerar_matriz_triangular(matriz_quadrada, 'inferior')

    print('Matriz Triangular Superior: ', matriz_triangular_superior, '\n')
    print('Matriz Triangular Inferior: ', matriz_triangular_inferior, '\n')

    pass


def exercício2():
    print('\nExercício 2: ')
    informar_comparação((31, 7, 2021), (31, 5, 2021))
    informar_comparação((31, 5, 2021), (31, 5, 2021))
    informar_comparação((31, 5, 2021), (31, 5, 2022))

    pass


def exercício1():
    print('\nExercício 1:')
    alunos = ['Silvia Lemos da Silva', 'Fernando Tavares de Almeida', 'Rafael Souza Junior', 'Sandra Maria dos Santos',
              'Pedro Valente Neto']
    lista_de_emails_e_nomes = criar_emails_acadêmicos(alunos)
    for tupla in lista_de_emails_e_nomes:
        print(tupla)
    pass


def informar_comparação(data1, data2):
    resultado = comparar_datas(data1, data2)
    if resultado == 1:
        print(str(data1) + ' é maior que ' + str(data2))
    elif resultado == 0:
        print(str(data1) + ' é igual a ' + str(data2))
    elif resultado == -1:
        print(str(data1) + ' é menor que ' + str(data2))
    pass


if __name__ == '__main__':
    print('Lista de Exercícios: Róger Evângelis Freitas Matos')
    exercício1()
    exercício2()
    exercício3()
    exercício4()
