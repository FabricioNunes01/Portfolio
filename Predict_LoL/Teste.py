from selenium import webdriver
import pandas as pd

# Dicionário para mapear valores numéricos para as strings correspondentes
objetivos = {
    'kill': 'Eliminações',
    'tower': 'Torres',
    'drake': 'Dragões',
    'baron': 'Barões',
    'gold': 'Ouro'
}

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

# Reordenando as colunas
blue_df = blue_df[['Time', 'Objetivo', 'Valor']]
red_df = red_df[['Time', 'Objetivo', 'Valor']]

# Concatenando os DataFrames
result_df = pd.concat([blue_df, red_df]).reset_index(drop=True)

# Print do DataFrame resultante
print(result_df)
