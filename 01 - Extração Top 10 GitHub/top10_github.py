import requests
import csv
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup


conteudo = None
URL = 'https://github.com/trending'

try:
    resposta = requests.get(URL)
    resposta.raise_for_status()
except HTTPError as exc:
    print(exc)
else:
    conteudo = resposta.text

with open(file = 'D:\Curso EBAC\Módulo 12 - Data Wrangling I\Pandas/gitsite.html', mode = 'w', encoding = 'utf8') as arquivo:
    arquivo.write(conteudo)


pagina = BeautifulSoup(open(file='D:\Curso EBAC\Módulo 12 - Data Wrangling I\Pandas/gitsite.html', mode = 'r', encoding= 'utf8'), 'html.parser')


git_projects = pagina.find_all(class_='Box-row')

#Listas finais
ranking = [1,2,3,4,5,6,7,8,9,10]
project = []
language = []
stars = []
stars_today = []
forks = []

#listas auxiliares
name_auxiliar = []
star_today_auxiliar=[]
forks_auxiliar = []

for proj in git_projects:
    name_info = proj.find(class_='h3').text.strip().split('\n')
    name_auxiliar.append(name_info)
    
    try:
        language_info = proj.find(itemprop="programmingLanguage").text
    except AttributeError:
        language.append('Não Descrito')
    else:
        language.append(language_info)
    
    stars_info = proj.find(class_="Link--muted d-inline-block mr-3").text.strip()
    stars.append(stars_info)
    
    stars_today_info = proj.find(class_="d-inline-block float-sm-right").text.strip()
    star_today_auxiliar.append(stars_today_info)
    
    forks_info = proj.find(class_="f6 color-fg-muted mt-2").text.strip().split('\n')
    forks_auxiliar.append(forks_info)

#Tratamento para a lista Project
for nome in name_auxiliar:
    project.append(nome[2].lstrip())


#Tratamento para a lista stars_today:
for estrela in star_today_auxiliar:
    stars_today.append(estrela.replace(' stars today',''))


#Tratando a variável Forks
for listas in forks_auxiliar:
    if listas[12].lstrip() == "":
        if len(listas) == 22:
            lista6 = [',', ',', ',', ',',',',',']
            listas = lista6 + listas
            forks.append(listas[12].lstrip())
        elif len(listas) == 25:
            list36 = [',', ',', ',']
            listas = lista6 + listas
            forks.append(listas[12].lstrip())
        elif len(listas) == 26:
            lista2 = [',', ',']
            listas = lista6 + listas
            forks.append(listas[12].lstrip())
        elif len(listas) == 18:
            lista10 = [',', ',', ',', ',',',',',',',',',',',',',']
            listas = lista6 + listas
            forks.append(listas[12].lstrip())
        else:
            forks.append(listas[12].lstrip())
    else:
        forks.append(listas[12].lstrip())

project = project[0:11]
language = language[0:11]
stars = stars[0:11]
stars_today = stars_today[0:11]
forks = forks[0:11]


#Colocando as informações extraidas em um arquivo CSV
with open(file= 'D:\Curso EBAC\Módulo 12 - Data Wrangling I\Pandas/github.csv', mode = 'w', encoding = 'utf8') as arquivo:
     git_info = csv.writer(arquivo, delimiter = ';')
     git_info.writerows([['ranking','project','language','stars', 'stars_today','forks']] + list(map(lambda ranking_extracao,project_extracao,language_extracao, stars_extracao, stars_today_extracao,forks_extracao:[ranking_extracao]+[project_extracao]+[language_extracao]+[stars_extracao]+[stars_today_extracao]+[forks_extracao],ranking,project,language,stars,stars_today,forks)))