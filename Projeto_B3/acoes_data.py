import yfinance as yf
import pandas as pd

# Lista de símbolos das ações brasileiras
tickers = ['PETR4.SA', 'VALE3.SA', 'ITUB4.SA']  # Exemplos de tickers, adicione outros conforme necessário

# Criando um DataFrame vazio para armazenar os dados
dados_acoes = pd.DataFrame()

# Obtendo dados históricos de cada ação
for ticker in tickers:
    # Obtendo os dados históricos usando o yfinance
    acao = yf.download(ticker, start='2018-01-01', end='2023-01-01')
    
    # Adicionando os dados ao DataFrame
    if not acao.empty:
        acao['Ticker'] = ticker  # Adicionando uma coluna com o ticker da ação
        dados_acoes = pd.concat([dados_acoes, acao['Close']], axis=1)

# Renomeando as colunas para os tickers das ações
dados_acoes.columns = tickers

# Exibindo os primeiros registros dos dados baixados
print(dados_acoes.head())
