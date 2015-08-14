# Importing modules
import mechanize
from bs4 import BeautifulSoup


# Setting the User Agent
user_agent="Mozilla/4.0"


# Imitating a Web Browser
br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders=[('User-agent',user_agent)]

# Getting the URL to Scrape
url=raw_input("Enter the URL to be scraped: ")

try:
    # Getting the HTML
    html = br.open(url).read()

    # Beautifying the HTML
    soup = BeautifulSoup(html,"lxml")

    # Getting all the <p></p> tags
    paragraphs = soup.find_all("p")

    # Joining all the <p></p> tags in one string
    text = " \n\n".join([ paragraph.text.encode('ascii','ignore').strip() for paragraph in paragraphs])

    # Printing the Result
    print text

except Exception as e:
    print(str(e))


