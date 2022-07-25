def carregar_arquivo_csv(nome_arquivo):
    arquivo = open('dados/' + nome_arquivo + '.csv', 'r')
    matriz_str = arquivo.read().strip('\n')
    arquivo.close()
    matriz = matriz_str.split('\n')
    for índice_linha, linha_str in enumerate(matriz):
        linha = list(linha_str.split(', '))
        matriz[índice_linha] = linha
        for índice_coluna, valor in enumerate(linha):
            valor = valor.strip()
            linha[índice_coluna] = valor

    return matriz
