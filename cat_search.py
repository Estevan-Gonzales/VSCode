from bs4 import BeautifulSoup
import requests

website = requests.get("https://www.austinpetsalive.org/adopt/cats")

soup = BeautifulSoup(website.content, 'html.parser')

names = []
attributes = []

for cat in soup.find_all('div', attrs={"class": "row justify-center"}):



    for name in cat.find_all('a', attrs={"class": "orange"}):
        #print(name.get_text())
        names.append(name.get_text())

    for stats in cat.find_all('ul', attrs={"class": "list-unstyled"}):
        #print(details.get_text())
        details = ''
        for detail in stats.find_all('li'):
            details += ' ' + detail.get_text()
        attributes.append(details)


cat_dict = {}

for i in range(len(names)):
    cat_dict[names[i]] = attributes[i]

for cat in cat_dict:
    print(cat, cat_dict[cat])
            
