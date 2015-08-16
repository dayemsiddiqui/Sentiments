import mechanize
from bs4 import BeautifulSoup

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent','Firefox/4.0')]

with open("movieid.csv",'r') as f:
    tt = f.read()

for t in tt.split(','):
    url = "http://www.imdb.com/title/" + t + "/reviews"

    html = br.open(url).read()

    soup = BeautifulSoup(html,"lxml")

    paragraphs = soup.find('div',{"id":"tn15content"})
    paragraphs = paragraphs.find_all('p')

    readable_p = " ".join([p.text.encode('utf-8','ignore').strip() for p in paragraphs])

    toReplace = ["\n","Add another review","*** This review may contain spoilers ***"]

    for r in toReplace:
        readable_p = readable_p.replace(r," ")
        
    with open("imdbReviews.txt",'a') as i:
        i.write(readable_p)
    
print "Reviews are saved in file \"imdbReviews.txt\""
