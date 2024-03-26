import pandas as pd

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
    'Data_Formatada': linhas_banco['Data_Formatada'],  # Use 'Data_Formatada' para a nova coluna de datas
    'Segunda_Coluna': linhas_banco.iloc[:, 0]  # Substitua 'Segunda_Coluna' pelo nome real da segunda coluna
})

# Exibe o novo DataFrame
print("\nNovo DataFrame com as linhas que contêm a palavra 'banco' e datas formatadas:")
print(novo_dataframe)
