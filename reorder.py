import os
import re

# Caminho para a pasta com as imagens
pasta = rf"./dataset"

# Expressão para extrair o número do nome
regex = re.compile(r'Match(\d+)')

# Lista para armazenar os arquivos e seus números
arquivos_com_numeros = []

# Percorrer arquivos da pasta
for nome_arquivo in os.listdir(pasta):
    match = regex.search(nome_arquivo)
    if match:
        numero = int(match.group(1))
        arquivos_com_numeros.append((numero, nome_arquivo))

# Ordenar decrescentemente pelo número
arquivos_com_numeros.sort(reverse=True)

# Renomear com adição de 169, seguindo a ordem
for idx, (numero_original, nome_arquivo) in enumerate(arquivos_com_numeros):
    novo_numero = numero_original + 169
    novo_nome = regex.sub(f'Match{novo_numero}', nome_arquivo)
    
    caminho_antigo = os.path.join(pasta, nome_arquivo)
    caminho_novo = os.path.join(pasta, novo_nome)
    
    os.rename(caminho_antigo, caminho_novo)
    print(f'Renomeado: {nome_arquivo} → {novo_nome}')