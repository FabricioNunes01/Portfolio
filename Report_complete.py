
import pandas as pd
import sweetviz as sv

# Carregar o DataFrame
df = pd.read_excel('meu_dataframe.xlsx')
df_drake = df.loc[df[1] == 'Drake'].iloc[[0]]
df = df.loc[df[1] != 'Drake']
df = pd.concat([df_drake,df])
df.columns = df.iloc[0]
df = df.drop(0)
df['Resultado'] = df['Resultado'].replace({'WIN': 1, 'LOSS': 0})
df = df.drop('Double kills', axis=1)
df = df.drop('Triple kills', axis=1)
df = df.drop('Quadra kills', axis=1)
df = df.drop('Penta kills', axis=1)
df = df.drop('Objectives Stolen', axis=1)
df = df.drop("['56817']", axis=1)
df = df.drop("CS in Enemy Jungle", axis=1)
#df = df.drop("Solo Kills", axis=1)
#df = df.drop("nan", axis=1)
df['Solo kills'] = df['Solo kills'].fillna(0, inplace=True)
df = df.dropna(axis=1)

# Converte os possíveis valores em float e int para facilitar
for coluna in df.columns:
    df[coluna] = pd.to_numeric(df[coluna], errors='ignore')

print(df.info())    
# Criar um relatório Sweetviz
report = sv.analyze(df)

# Exibir o relatório no navegador padrão
report.show_html('sweetviz_report.html')
