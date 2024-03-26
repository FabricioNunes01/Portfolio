import requests
from bs4 import BeautifulSoup
import pandas as pd

# Função para realizar a raspagem de dados de uma página específica
def raspagem_pagina(url, noticias, datas):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = soup.find_all('h2', class_='content__title')
        datas_noticias = soup.find_all('time', itemprop='datePublished')  # Encontrando todas as datas
        
        for i, headline in enumerate(headlines):
            # Acessando a data correspondente ao índice da manchete atual
            data = datas_noticias[i]['datetime'] if i < len(datas_noticias) else 'Data não encontrada'
            
            # Adicionando os valores às listas
            noticias.append(headline.text.strip())
            datas.append(data)
    else:
        print('Falha ao carregar a página:', response.status_code)

# Listas para armazenar as notícias e datas
todas_noticias = []
todas_datas = []

# Loop para percorrer múltiplas páginas
for pagina in range(2, 2350):  # De 2 a 2395 (para todas as páginas)
    url = f'https://www.suno.com.br/noticias/negocios/page/{pagina}/#ultimas-noticias'
    print(f'Raspagem da página: {url}')
    raspagem_pagina(url, todas_noticias, todas_datas)

# Criando um DataFrame do Pandas com as listas de notícias e datas
dados = pd.DataFrame({'Notícia': todas_noticias, 'Data': todas_datas})

# Salvar os dados em um arquivo CSV
dados.to_csv('dados_suno.csv', index=False)

# Mensagem indicando que a exportação foi realizada com sucesso
print('Dados exportados para dados_suno.csv')
