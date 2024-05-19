import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


# Aqui obtemos os sites do cblol
url2 = "https://gol.gg/tournament/tournament-matchlist/CBLOL%20Split%201%202024/"
#url2 = "https://gol.gg/tournament/tournament-stats/LCK%20Spring%202024/"

original_url = "https://gol.gg/"
replacement_text = "/page-game/"
replacement_text_new = "/page-fullstats/"

response = requests.get(url2)
final_df = pd.DataFrame()

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    match_elements = soup.find_all('a', href=lambda href: href and "/game/stats/" in href)
    
    for match_element in match_elements:
        partial_link = match_element.get('href')
        modified_link = partial_link.replace(replacement_text, replacement_text_new)
        url = urljoin(original_url, modified_link)




        # URL da página
        numeros = re.findall(r'\d+', url)

        # Se você quiser pegar apenas os números no meio da URL, excluindo o início e o final


        # Inicializar o driver do Selenium
        driver = webdriver.Chrome()  # Certifique-se de ter o ChromeDriver instalado e no PATH
        driver.get(url)

        # Esperar até que a página seja totalmente carregada (pode ser necessário ajustar este tempo)
        driver.implicitly_wait(10)

        element_value = driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div/div[3]/div/div/div/table/tbody/tr[1]/td[2]/b").text

        # Encontra todos os elementos <td> dentro do primeiro <tr>, incluindo os ocultos
        td_elements = driver.find_elements(By.XPATH, "/html/body/div/main/div[2]/div/div[3]/div/div/div/table/tbody/tr[1]/td")

        # Extrai o conteúdo dos elementos <td> encontrados
        td_texts = [td.get_attribute('textContent') for td in td_elements]

        # Cria um DataFrame do Pandas
        gf = pd.DataFrame({"Elemento": ["Valor", *["Conteúdo"] * len(td_texts)]})

        # Adiciona os valores obtidos ao DataFrame
        gf["Valor"] = [element_value, *td_texts]
        gf = gf.T
        gf = gf.drop(gf.index[0])
        gf = gf.drop(gf.columns[0], axis=1)
        gf.reset_index(drop=True, inplace=True)
        novos_rotulos = [0, 1, 2, 3,4,5,6,7,8,9,10]
        gf.columns = novos_rotulos

        # Encontrar a tabela usando XPath
        table_xpath = "/html/body/div/main/div[2]/div/div[3]/div/div/div/table"
        table = driver.find_element(By.XPATH, table_xpath)

        # Encontrar todas as linhas da tabela
        rows = table.find_elements(By.TAG_NAME, "tr")

        # Lista para armazenar os dados
        data = []

        # Adicionar o título "Champion" como a primeira linha de dados
        row_data = []
        for row in rows[0].find_elements(By.TAG_NAME, "td"):
            cell_text = driver.execute_script("return arguments[0].textContent;", row)
            row_data.append(cell_text.strip())
        data.append(row_data)



        # Iterar sobre as linhas e extrair os valores das células
        for row in rows[2:]:
            # Encontrar todas as células da linha
            cells = row.find_elements(By.TAG_NAME, "td")
            row_data = []

            # Extrair o texto de cada célula e adicionar à lista de dados da linha
            for cell in cells:
                cell_text = driver.execute_script("return arguments[0].textContent;", cell)
                row_data.append(cell_text.strip())
            
            # Adicionar dados da linha à lista de dados
            data.append(row_data)


        # Encontrar todos os elementos <img> dentro da tabela usando XPath
        img_elements = driver.find_elements(By.XPATH, "//table//img")

        # Lista para armazenar os valores do atributo "alt" dos elementos <img>
        alt_values = []

        # Adicionar um elemento vazio à lista alt_values para corresponder ao título "Champion"
        alt_values.append("")

        # Iterar sobre os elementos <img> e extrair o valor do atributo "alt"
        for img in img_elements:
            alt_value = img.get_attribute("alt")
            alt_values.append(alt_value)

        # Fechar o navegador
        driver.quit()

        # Verificar se o número de colunas corresponde ao número de valores em alt_values
        num_columns_data = len(data[0]) if data else 0
        num_columns_alt_values = len(alt_values)

        # Se o número de colunas nos dados for maior que o número de valores em alt_values,
        # adicionamos valores vazios à lista alt_values para corresponder ao número de colunas
        if num_columns_data > num_columns_alt_values:
            num_missing_values = num_columns_data - num_columns_alt_values
            alt_values.extend([''] * num_missing_values)




        # Criar DataFrame pandas com os dados coletados e usar alt_values como cabeçalho
        df = pd.DataFrame(data)
        ff = pd.DataFrame(alt_values)
        #print(df)


        # Concatenar todos os valores em uma única linha separados por espaços
        champions_string = ' '.join(alt_values)

        # Criar DataFrame pandas com os dados concatenados como uma única linha e usar "Champion" como o cabeçalho da coluna

        df_transposed = ff.T
        #print(df_transposed)

        #Aqui colocamos como o titulo dos champions
        ff = pd.DataFrame(df_transposed)
        ff.loc[0,0] = 'Champion'



        df = pd.concat([ff,df])
        df = pd.concat([gf,df],ignore_index=True)
        #print(df)
        #nome_arquivo = 'exemplo.xlsx'
        #with pd.ExcelWriter(nome_arquivo) as writer:
            #ff.to_excel(writer, index=False)


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
        ### AQUI TA O PROBLEMA 
        url = url.replace("fullstats", "game")


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


        df = pd.concat([new_df,df],ignore_index=True)
        nova_linha = pd.DataFrame([[numeros]*len(df.columns)], columns=df.columns)
        print('oi')
        # Adicionando a nova linha ao DataFrame existente
        df = pd.concat([df, nova_linha], ignore_index=True)
        df = df.T
        final_df = pd.concat([final_df,df])
        print(final_df)


nome_arquivo_excel = 'meu_dataframe.xlsx'
#ome_arquivo_excel = 'meu_dataframe_kr.xlsx'

# Salvando o DataFrame como um arquivo do Excel
final_df.to_excel(nome_arquivo_excel, index=False)