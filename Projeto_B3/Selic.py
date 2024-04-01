import requests
import pandas as pd

# URL da API do Banco Central do Brasil para a Taxa Selic
url = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json&dataInicial=01/01/2018&dataFinal=01/01/2023'

# Realizando a requisição HTTP para obter os dados da Taxa Selic
response = requests.get(url)

# Verificando se a requisição foi bem-sucedida (código 200)
if response.status_code == 200:
    # Convertendo os dados da resposta para um DataFrame do Pandas
    dados_selic = pd.DataFrame(response.json())
    dados_selic = dados_selic[['valor', 'data']]
    
    # Exportando os dados para um arquivo CSV
    dados_selic.to_csv('dados_selic.csv', index=False)
    print('Dados da Taxa Selic exportados para o arquivo dados_selic.csv')
else:
    print('Falha ao carregar os dados da Taxa Selic:', response.status_code)
