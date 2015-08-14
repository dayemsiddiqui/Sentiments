import nltk
import urllib2
import readability
from bs4 import BeautifulSoup
from readability.readability import Document
import mechanize

URL=raw_input("Enter the URL of the page : ")

br= mechanize.Browser()
br.set_handle_robots(False)
br.addheaders=[('User-agent','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36')]

##URL="http://techcrunch.com/2010/07/05/how-steam-stopped-me-from-pirating-games-and-enjoy-the-sweet-drm-kool-aid/"

#html = urllib2.urlopen(URL).read()

html = br.open(URL).read()
#print html

readable_article=Document(html).summary()
#print readable_article
readable_title=Document(html).short_title()
#print readable_title

soup = BeautifulSoup(readable_article,"lxml")
#print soup

final_article=soup.text

links = soup.findAll('img',src=True)

print final_article

