import pandas as pd
import glob
import os

print("Iniciando script de unificação...")

# Define o caminho para a pasta de dados (relativo ao script)
# .. -> "volte uma pasta" (da /scripts para a raiz)
# /dados -> "entre na pasta dados"
caminho_dados = 'dados/'

# Usa o glob para encontrar todos os arquivos .csv dentro da pasta 'dados'
arquivos_csv = glob.glob(os.path.join(caminho_dados, "pda-prouni-*.csv"))

print(f"Arquivos encontrados: {arquivos_csv}")

# Lista para armazenar os DataFrames de cada ano
lista_dataframes = []

for arquivo in arquivos_csv:
    print(f"Lendo o arquivo: {arquivo}")
    # Lê cada CSV
    df_ano = pd.read_csv(arquivo, sep=';', encoding='latin1') 
    lista_dataframes.append(df_ano)

print("Concatenando todos os arquivos...")
# Concatena (empilha) todos os DataFrames da lista em um só
df_unificado = pd.concat(lista_dataframes, ignore_index=True)

# Define o nome do arquivo de saída
arquivo_saida = os.path.join(caminho_dados, 'ProUniTrienio.csv')

print(f"Salvando arquivo unificado em: {arquivo_saida}")
# Salva o DataFrame unificado em um novo CSV
df_unificado.to_csv(arquivo_saida, index=False, sep=';', encoding='latin1')

print("Processo concluído com sucesso!")