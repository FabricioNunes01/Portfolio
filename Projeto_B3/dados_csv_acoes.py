import pandas as pd

# Caminho do arquivo CSV
caminho_arquivo = 'dados_selic.csv'

# Lendo o arquivo CSV e carregando os dados para um DataFrame do Pandas
dados_selic = pd.read_csv(caminho_arquivo)

# Exibindo os primeiros registros do DataFrame
print(dados_selic.head())
