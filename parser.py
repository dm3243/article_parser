import requests
import newspaper
from newspaper import Article

class Edits():
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# class Article_Edits(Edits):
#     def__init__(self,...)

#     url = input("Please enter article URL: ")
    
#     def article_details(self, url):
#         article = Article(url)
#         article.download()
#         article.parse()
#         print(Edits.BOLD + 'Title: ' + Edits.END, article.title)
#         print(Edits.BOLD + 'Author: ' + Edits.END, article.authors)
#         print(Edits.BOLD + 'Date: ' + Edits.END, article.publish_date)

#     def find_names(self, url):
#         new_url = url.split('.')
#         print(Edits.BOLD + 'Article by: ' + Edits.END + new_url[1].upper())

#    def check(self):
#        if article.



def article_details(url):
    article = Article(url)
    article.download()
    article.parse()
    print(Edits.BOLD + 'Title: ' + Edits.END, article.title)
    print(Edits.BOLD + 'Author: ' + Edits.END, article.authors)
    print(Edits.BOLD + 'Date: ' + Edits.END, article.publish_date);

# def url_grab(url):
#     r = requests.get(url)
#     print(r.status_code)
#     print(r.text)

#Following function is for getting the publication's name simply. 
# Will need to format string to tidy up the result.

def find_names(url):
    new_url = url.split('.')
    print(Edits.BOLD + 'Article by: ' + Edits.END + new_url[1].upper())

#This is my temp fix for getting names of publications.  

    # if 'cnn' in url:
    #     print(Edits.BOLD + 'Article by:' + Edits.END, 'CNN')
    # elif 'qz' in url:
    #     print(Edits.BOLD + 'Article by:' + Edits.END, 'Quartz')
    # elif 'wsj' in url:
    #     print(Edits.BOLD + 'Article by:' + Edits.END, 'The Wall Street Journal')
    # elif 'fivethirtyeight' in url:
    #     print(Edits.BOLD + 'Article by:' + Edits.END, 'Five Thirty Eight')
    # elif 'nytimes' in url:
    #     print(Edits.BOLD + 'Article by:' + Edits.END, 'The New York Times')
    # elif 'bloomberg' in url:
    #     print(Edits.BOLD + 'Article by:' + Edits.END, 'Bloomberg')
    # elif 'cnbc' in url:
    #     print(Edits.BOLD + 'Article by:' + Edits.END, 'CNBC')
    # elif 'theguardian' in url:
    #     print(Edits.BOLD + 'Article by:' + Edits.END, 'The Guardian')
    # elif 'huffingtonpost' in url:
    #     print(Edits.BOLD + 'Article by:' + Edits.END, 'The Huffington Post')
    # elif 'themarshallproject' in url:
    #     print(Edits.BOLD + 'Article by:' + Edits.END, 'The Marshall Project')
    # elif 'seattletimes' in url:
    #     print(Edits.BOLD + 'Article by:' + Edits.END, 'The Seattle Times')
    # else:
    #     print('Article publication not recognized')

def main():

    #print(article_Edits())

    url_input = input("Please enter article URL: ")

    find_names(url_input)
    article_details(url_input)
    #url_grab(url_input)   

if __name__ == '__main__': main()