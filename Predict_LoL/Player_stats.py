from selenium import webdriver
from selenium.webdriver.common.by import By

#Obter valores individuais de cada jogador

# URL da página
url = "https://gol.gg/game/stats/56083/page-fullstats/"

# Inicializar o driver do Selenium
driver = webdriver.Chrome()  # Certifique-se de ter o ChromeDriver instalado e no PATH
driver.get(url)

# Esperar até que a página seja totalmente carregada (pode ser necessário ajustar este tempo)
driver.implicitly_wait(10)

# Encontrar todos os elementos <img> dentro da tabela usando XPath
img_elements = driver.find_elements(By.XPATH, "//table//img")

# Lista para armazenar os valores do atributo "alt" dos elementos <img>
alt_values = []

# Iterar sobre os elementos <img> e extrair o valor do atributo "alt"
for img in img_elements:
    alt_value = img.get_attribute("alt")
    alt_values.append(alt_value)

# Encontrar a tabela usando XPath
table_xpath = "/html/body/div/main/div[2]/div/div[3]/div/div/div/table"
table = driver.find_element(By.XPATH, table_xpath)

# Imprimir os valores do atributo "alt" como colunas na parte superior
print("\t".join(alt_values))

# Encontrar todas as linhas da tabela
rows = table.find_elements(By.TAG_NAME, "tr")

# Iterar sobre as linhas e imprimir os valores das células
for row in rows:
    # Encontrar todas as células da linha
    cells = row.find_elements(By.TAG_NAME, "td")

    # Imprimir o texto de cada célula
    for cell in cells:
        # Use execute_script para recuperar o texto mesmo se estiver oculto
        cell_text = driver.execute_script("return arguments[0].textContent;", cell)
        print(cell_text.strip(), end='\t')

    print()  # Adiciona uma quebra de linha entre as linhas

# Fechar o navegador
driver.quit()
