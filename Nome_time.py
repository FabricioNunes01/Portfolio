from selenium import webdriver
import pandas as pd

# Dicionário para mapear valores numéricos para as strings correspondentes
objetivos = {
    'kill': 'kill',
    'tower': 'tower',
    'drake': 'drake',
    'baron': 'baron',
    'gold': 'gold'
}

# Criando uma função para extrair apenas o nome do time
def extract_team_name(team_name):
    return team_name.split(' - ')[0]

# Inicializando o navegador Chrome
driver = webdriver.Chrome()

# URL da página
url = 'https://gol.gg/game/stats/56083/page-game/'

# Abrindo a página
driver.get(url)

# Encontrando todos os elementos span com a classe 'score-box blue_line'
score_boxes = driver.find_elements('css selector', 'span.score-box.blue_line')

# Iterando sobre os elementos e extraindo os textos
blue_data = []
for i, score_box in enumerate(score_boxes):
    objetivo = list(objetivos.keys())[i]
    blue_data.append([objetivos[objetivo], score_box.text.strip()])

# Encontrando todos os elementos <span class="score-box red_line">
score_boxes_red = driver.find_elements('css selector', 'span.score-box.red_line')

# Iterando sobre os elementos e extraindo os textos
red_data = []
for i, score_box_red in enumerate(score_boxes_red):
    objetivo = list(objetivos.keys())[i]
    red_data.append([objetivos[objetivo], score_box_red.text.strip()])

# Encontrando o elemento <div class="col-12 blue-line-header">
blue_line_header = driver.find_element('css selector', 'div.col-12.blue-line-header')

# Extraindo o texto dentro do elemento div blue-line-header
blue_line_text = blue_line_header.text.strip()

# Encontrando o elemento <div class="col-12 red-line-header">
red_line_header = driver.find_element('css selector', 'div.col-12.red-line-header')

# Extraindo o texto dentro do elemento div red-line-header
red_line_text = red_line_header.text.strip()

# Fechando o navegador
driver.quit()

# Criando DataFrames do pandas
blue_df = pd.DataFrame(blue_data, columns=['Objetivo', 'Valor'])
red_df = pd.DataFrame(red_data, columns=['Objetivo', 'Valor'])

# Adicionando uma coluna para o nome do time
blue_df['Time'] = blue_line_text
red_df['Time'] = red_line_text

# Aplicando a função para extrair apenas o nome do time
blue_df['Time'] = blue_df['Time'].apply(extract_team_name)
red_df['Time'] = red_df['Time'].apply(extract_team_name)

# Reordenando as colunas
blue_df = blue_df[['Time', 'Objetivo', 'Valor']]
red_df = red_df[['Time', 'Objetivo', 'Valor']]

# Concatenando os DataFrames
result_df = pd.concat([blue_df, red_df]).reset_index(drop=True)

# Adicionando uma coluna para o resultado
result_df['Resultado'] = result_df['Time'].apply(lambda x: 'WIN' if x in red_df['Time'].values else 'LOSS')


primeiro_time =result_df.iloc[0, 0]
segundo_time =result_df.iloc[6, 0]
primeiro_res =result_df.iloc[0, 3]
segundo_res =result_df.iloc[6, 3]
primeiro_bar =result_df.iloc[3, 2]
segundo_bar =result_df.iloc[8, 2]
primeiro_drake =result_df.iloc[2, 2]
segundo_drake =result_df.iloc[7, 2]
print(segundo_time)
data = {0: ['Time',"Drake","Baron","Resultado"],
        1: [primeiro_time,primeiro_drake,primeiro_bar,primeiro_res],
        2: [primeiro_time,primeiro_drake,primeiro_bar,primeiro_res],
        3: [primeiro_time,primeiro_drake,primeiro_bar,primeiro_res],
        4: [primeiro_time,primeiro_drake,primeiro_bar,primeiro_res],
        5: [primeiro_time,primeiro_drake,primeiro_bar,primeiro_res],
        6: [segundo_time,segundo_drake,segundo_bar,segundo_res],
        7: [segundo_time,segundo_drake,segundo_bar,segundo_res],
        8: [segundo_time,segundo_drake,segundo_bar,segundo_res],
        9: [segundo_time,segundo_drake,segundo_bar,segundo_res],
        10: [segundo_time,segundo_drake,segundo_bar,segundo_res],}

new_df = pd.DataFrame(data)
#Aqui para pegar time e vitoria derrota
#print(result_df)
print(new_df)