def gerar_diagonal_matriz(matriz_quadrada):
    diagonal = []
    # indice_linha = i, indice_coluna = j
    for indice_linha in range(len(matriz_quadrada)):
        for indice_coluna in range(len(matriz_quadrada[0])):
            if indice_linha == indice_coluna:
                diagonal.append(matriz_quadrada[indice_linha][indice_coluna])
    return diagonal


def gerar_matriz_triangular(matriz_quadrada, tipo_matriz_triangular):
    if tipo_matriz_triangular == 'superior':
        matriz_triangular = []
        for indice_linha in range(len(matriz_quadrada)):
            linha_convertida = []
            for indice_coluna in range(len(matriz_quadrada)):
                if indice_linha > indice_coluna:
                    linha_convertida.append(0)
                else:
                    linha_convertida.append(matriz_quadrada[indice_linha][indice_coluna])
            matriz_triangular.append(linha_convertida)
        return matriz_triangular

    elif tipo_matriz_triangular == 'inferior':
        matriz_triangular = []
        for indice_linha in range(len(matriz_quadrada)):
            linha_convertida = []
            for indice_coluna in range(len(matriz_quadrada)):
                if indice_linha < indice_coluna:
                    linha_convertida.append(0)
                else:
                    linha_convertida.append(matriz_quadrada[indice_linha][indice_coluna])
            matriz_triangular.append(linha_convertida)
        return matriz_triangular
