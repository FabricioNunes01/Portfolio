import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import re

# URL da página
url = "https://gol.gg/game/stats/56083/page-fullstats/"
numeros = re.findall(r'/(\d+)/', url)

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
nova_linha = pd.DataFrame([[numeros]*len(df.columns)], columns=df.columns)

# Adicionando a nova linha ao DataFrame existente
df = pd.concat([df, nova_linha], ignore_index=True)
df = df.T
print(df)
#print(df)
#nome_arquivo = 'exemplo.xlsx'
#with pd.ExcelWriter(nome_arquivo) as writer:
    #ff.to_excel(writer, index=False)




