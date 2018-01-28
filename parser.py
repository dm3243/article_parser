import requests
import newspaper
from newspaper import Article

class color():
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

#class article_edits(self):
#    def check(self):
#        if article.


def article_details(url):
    article = Article(url)
    article.download()
    article.parse()
    print(color.BOLD + 'Title: ' + color.END, article.title)
    print(color.BOLD + 'Author: ' + color.END, article.authors)
    print(color.BOLD + 'Date: ' + color.END, article.publish_date)
    publication = article.source_url.split('.')
    print(color.BOLD + 'Publication: ' + color.END, publication[1].upper())
    #print(article.keywords)
    


def url_grab(url):
    r = requests.get(url)
    print(r.status_code)
    print(r.text)

#This is my temp fix for getting names of publications. 
#Newspaper package is better for this, so will adjust after learning how to use it. 
def find_names(url):
    if 'cnn' in url:
        print(color.BOLD + 'Article by:' + color.END, 'CNN')
    elif 'qz' in url:
        print(color.BOLD + 'Article by:' + color.END, 'Quartz')
    elif 'wsj' in url:
        print(color.BOLD + 'Article by:' + color.END, 'The Wall Street Journal')
    elif 'fivethirtyeight' in url:
        print(color.BOLD + 'Article by:' + color.END, 'Five Thirty Eight')
    elif 'nytimes' in url:
        print(color.BOLD + 'Article by:' + color.END, 'The New York Times')
    elif 'bloomberg' in url:
        print(color.BOLD + 'Article by:' + color.END, 'Bloomberg')
    elif 'cnbc' in url:
        print(color.BOLD + 'Article by:' + color.END, 'CNBC')
    elif 'theguardian' in url:
        print(color.BOLD + 'Article by:' + color.END, 'The Guardian')
    elif 'huffingtonpost' in url:
        print(color.BOLD + 'Article by:' + color.END, 'The Huffington Post')
    elif 'themarshallproject' in url:
        print(color.BOLD + 'Article by:' + color.END, 'The Marshall Project')
    elif 'seattletimes' in url:
        print(color.BOLD + 'Article by:' + color.END, 'The Seattle Times')
    else:
        print(color.BOLD + 'Article publication not recognized')

def main():

    url_input = input("Please enter article URL: ")

    find_names(url_input)
    #url_grab(url_input)
    article_details(url_input)

if __name__ == '__main__': main()