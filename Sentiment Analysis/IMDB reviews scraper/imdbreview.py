import mechanize,csv
from bs4 import BeautifulSoup

print "Initializing...\nInitialized"

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent','Firefox/4.0')]

with open("title.csv",'r') as f:
    current_title = f.read()

url = "http://www.imdb.com/title/" + current_title + "/reviews"

print "Working...\nPlease wait"

html = br.open(url).read()

soup = BeautifulSoup(html,"lxml")

paragraphs = soup.find('div',{"id":"tn15content"})
paragraphs = paragraphs.find_all('p')

readable_p = " ".join([p.text.encode('utf-8','ignore').strip() for p in paragraphs])

print "Almost done..."

toReplace = ["\n","Add another review","*** This review may contain spoilers ***"]
print "."
for r in toReplace:
    readable_p = readable_p.replace(r," ")
    
with open("imdbReviews.txt",'w') as i:
    i.write(readable_p)
print "."
with open("movieid.csv",'r+') as i:
    data = i.read()
    print "."
    title = current_title + ","
    for d in data:
        data = data.replace(title," ").strip()
    #i.seek(0)
    i.write(data)
    ##print "movieid.csv edited"
print "."
with open("movieid.csv",'r') as csvin:
    reader = csv.reader(csvin,delimiter=',')
    with open("title.csv",'w') as out:
        for row in reader:
            title = row[0]
        writer = out.write(title)
    
    
print "\nReviews are saved in file \"imdbReviews.txt\""
