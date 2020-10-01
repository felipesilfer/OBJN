import requests,csv
from bs4 import BeautifulSoup

url = 'http://www.objnursing.uff.br/index.php/nursing/issue/archive'

def get_volumes():
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    lista_volumes = soup.find_all('div', class_='issueCoverImage')
    for volume in lista_volumes:
        url_volume = volume.find('a').get('href') +'/showToc'
        get_artigos(url_volume)

def get_artigos(url_volume):
    r = requests.get(url_volume)
    soup = BeautifulSoup(r.text, 'lxml')
    lista = soup.find_all('table', class_='tocArticle')
    for item in lista:
        lista_artigos = item.find_all('div', class_='tocTitle')
        for artigo in lista_artigos:
            url_art = artigo.find_next('a').get('href')
            get_doi(url_art)

def get_doi(url_art):
    r = requests.get(url_art)
    soup = BeautifulSoup(r.text, 'lxml')
    doi = soup.find(id='pub-id::doi').get('href')
    art_name = soup.find(id='articleTitle').text
    if check_doi(doi):
        print(art_name.encode("utf-8"))
        print(url_art.encode("utf-8"))
        print(doi.encode("utf-8"))
        print('quebrado')
        print('-----')
        with open('arquivo.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([art_name.encode("utf-8"),doi.encode("utf-8"),url_art.encode("utf-8")])
    else:
        print(art_name.encode("utf-8"))
        print(url_art.encode("utf-8"))
        print(doi.encode("utf-8"))
        print('ok')
        print('-----')

def check_doi(doi):
    r = requests.get(doi)
    soup = BeautifulSoup(r.text, 'lxml')
    titulo = soup.find('title').next_element
    if titulo == 'Error: DOI Not Found':
        return True
    else:
        return False

def main():
    get_volumes()

if __name__ == "__main__":
    main()