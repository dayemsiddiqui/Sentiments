from bs4 import BeautifulSoup
import lxml
import re
import requests
import mechanize

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent','Firefox/4.0')]

url = "http://www.imdb.com/chart/top?ref_=ft_250"


html = br.open(url).read()

soup = BeautifulSoup(html,"lxml")

links = soup.find("div",{"class":"lister"})

for link in links.find_all('a'):
    
    m = re.search(r'tt[0-9]{7}',link.get('href'))

    with open("movieid.csv",'a') as f:
        f.write(m.group()+',')
    
print 'Movie title IDs are saved in \"movieid.csv\"'

