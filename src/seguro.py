from src.util import carregar_arquivo_csv


def obter_população_cidade(cidade_segurado):
    nomeArquivoCsv = 'PopulaçõesCidadesBrasileiras'
    populações_cidades_brasileiras = carregar_arquivo_csv(nomeArquivoCsv)
    cidade_população = []
    for indice_cidade, população in enumerate(populações_cidades_brasileiras):
        if cidade_segurado in populações_cidades_brasileiras:
            cidade_população.append(indice_cidade)
    return cidade_população
