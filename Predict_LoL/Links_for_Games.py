import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "https://gol.gg/tournament/tournament-matchlist/CBLOL%20Split%201%202024/"

original_url = "https://gol.gg/"
replacement_text = "/page-game/"
replacement_text_new = "/page-fullstats/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    match_elements = soup.find_all('a', href=lambda href: href and "/game/stats/" in href)
    
    for match_element in match_elements:
        partial_link = match_element.get('href')
        modified_link = partial_link.replace(replacement_text, replacement_text_new)
        full_link = urljoin(original_url, modified_link)
        print(full_link)
else:
    print(f"Erro ao acessar a página. Código de status: {response.status_code}")
