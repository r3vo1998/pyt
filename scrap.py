<<<<<<< HEAD
import urllib.request
from bs4 import BeautifulSoup

news = "https://vesti.ua/"

class Scraper:
    def __init__(self, news):
        self.site = news
        
    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "html" in url:
                print("\n" + url)
                 
               
       


           

=======
import urllib.request
from bs4 import BeautifulSoup

news = "https://vesti.ua/"

class Scraper:
    def __init__(self, news):
        self.site = news
        
    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "html" in url:
                print("\n" + url)
                 
               
       


           

>>>>>>> ac5d2c7ba8c62d0e5ba2b0895e95f3b71ed59ce6
