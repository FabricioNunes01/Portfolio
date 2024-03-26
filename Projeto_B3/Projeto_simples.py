import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Lê o arquivo CSV
dados = pd.read_csv(r'C:\Code\Projeto_B3\dados_suno.csv')

# Filtra as linhas que contêm a palavra "banco" na segunda coluna
linhas_banco = dados[dados.iloc[:, 0].str.contains('banco', case=False)].copy()

# Exibe a contagem
contagem_banco = len(linhas_banco)
print(f"Quantidade de linhas com a palavra 'banco' na segunda coluna: {contagem_banco}")

# Converte as datas para o formato desejado
linhas_banco['Data'] = pd.to_datetime(linhas_banco['Data'], utc=True)
linhas_banco['Data_Formatada'] = linhas_banco['Data'].dt.strftime('%d/%m/%Y')

# Cria um novo DataFrame com as linhas filtradas
novo_dataframe = pd.DataFrame({
    'Data_Formatada': linhas_banco['Data_Formatada'],
    'Segunda_Coluna': linhas_banco.iloc[:, 0]
})

# Exibe o novo DataFrame
print("\nNovo DataFrame com as linhas que contêm a palavra 'banco' e datas formatadas:")
print(novo_dataframe)

# Defina os símbolos das ações e o período desejado
tickers = ['BBDC3.SA', 'ABCB4.SA', 'BBAS3.SA']
start_date = '2019-01-01'
end_date = '2023-12-31'

# Obtém os dados de preços das ações usando yfinance
dados_acoes = yf.download(tickers, start=start_date, end=end_date)

# Seleciona apenas a coluna 'Close' (preço de fechamento)
dados_acoes_fechamento = dados_acoes['Close']

# Exibe os dados de preços de fechamento das ações
print("\nDados de preços de fechamento das ações:")
print(dados_acoes_fechamento.head())

# Cria um gráfico de linhas com os preços de fechamento
plt.figure(figsize=(10, 6))
dados_acoes_fechamento.plot()
plt.title('Preços de Fechamento das Ações')
plt.xlabel('Data')
plt.ylabel('Preço de Fechamento')
plt.legend(tickers)
plt.show()

# Unir os dois DataFrames com base na coluna de datas
dados_completos = pd.merge(novo_dataframe, dados_acoes_fechamento, left_on='Data_Formatada', right_index=True)

# Calcular a correlação entre as duas variáveis
correlacao = dados_completos['Segunda_Coluna'].corr(dados_completos['Close'])

# Exibir a correlação
print(f"\nCorrelação entre notícias sobre bancos e preços de fechamento das ações: {correlacao}")
