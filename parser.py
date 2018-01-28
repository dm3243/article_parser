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

def article_details(url):
    article = Article(url)
    article.download()
    article.parse()
    print(color.BOLD + 'Title: ' + color.END, article.title)
    print(color.BOLD + 'Author: ' + color.END, article.authors)
    print(color.BOLD + 'Date: ' + color.END, article.publish_date)
    publication = article.source_url.split('.')
    print(color.BLUE + color.BOLD + 'Publication: ' + color.END, publication[1].capitalize())
    #print(article.keywords)
    


def url_grab(url):
    r = requests.get(url)
    print(r.status_code)
    print(r.text)

#This is my temp fix for getting names of publications. 
#Newspaper package is better for this, so will adjust after learning how to use it. 
def find_names(url):
    if 'cnn' in url:
        print('Article by: CNN')
    elif 'qz' in url:
        print('Article by: Quartz')
    elif 'wsj' in url:
        print('Article by: Wall Street Journal')
    elif 'fivethirtyeight' in url:
        print('Article by: Five Thirty Eight')
    elif 'nytimes' in url:
        print('Article by: New York Times')
    elif 'bloomberg' in url:
        print('Article by: Bloomberg')
    elif 'cnbc' in url:
        print('Article by: CNBC')
    elif 'theguardian' in url:
        print('Article by: The Guardian')
    elif 'huffingtonpost' in url:
        print('Article by: The Huffington Post')
    elif 'themarshallproject' in url:
        print('Article by: The Marshall Project')
    elif 'seattletimes' in url:
        print('Article by: The Seattle Times')
    else:
        print('Article publication not recognized')

def main():

    #find_names('https://www.wsj.com/articles/trump-takes-to-twitter-like-clockwork-1516357800')
    #url_grab('https://www.cnbc.com/2017/05/05/teslas-valuation-raises-grim-reminders-of-the-dotcom-bubble.html')
    article_details('https://www.cnbc.com/2017/05/05/teslas-valuation-raises-grim-reminders-of-the-dotcom-bubble.html')

if __name__ == '__main__': main()