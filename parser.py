import requests
import newspaper
from newspaper import Article

class Edits():
#Keeping these variables in case I need them later. Don't need to look up the code.
#   PURPLE = '\033[95m'
#   CYAN = '\033[96m'
#   DARKCYAN = '\033[36m'
#   BLUE = '\033[94m'
#   GREEN = '\033[92m'
#   YELLOW = '\033[93m'
#   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

#Keeping this class to work on later. Give each article an identity with functions to follow.

# class Article_Edits(Edits):

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

#Will uncomment this bit later if the class article_Edits above doesn't work

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