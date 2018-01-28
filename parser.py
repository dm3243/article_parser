import requests
import newspaper
from newspaper import Article

class edits():
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

# class article_edits(edits):

#     url = input("Please enter article URL: ")
    
#     def article_details(self, url):
#         article = Article(url)
#         article.download()
#         article.parse()
#         print(edits.BOLD + 'Title: ' + edits.END, article.title)
#         print(edits.BOLD + 'Author: ' + edits.END, article.authors)
#         print(edits.BOLD + 'Date: ' + edits.END, article.publish_date)

#     def find_names(self, url):
#         new_url = url.split('.')
#         print(edits.BOLD + 'Article by: ' + edits.END + new_url[1].upper())

#    def check(self):
#        if article.

#Will uncomment this bit later if the class article_edits above doesn't work

def article_details(url):
    article = Article(url)
    article.download()
    article.parse()
    print(edits.BOLD + 'Title: ' + edits.END, article.title)
    print(edits.BOLD + 'Author: ' + edits.END, article.authors)
    print(edits.BOLD + 'Date: ' + edits.END, article.publish_date);

# def url_grab(url):
#     r = requests.get(url)
#     print(r.status_code)
#     print(r.text)

#Following function is for getting the publication's name simply. 
# Will need to format string to tidy up the result.

def find_names(url):
    new_url = url.split('.')
    print(edits.BOLD + 'Article by: ' + edits.END + new_url[1].upper())

#This is my temp fix for getting names of publications.  

    # if 'cnn' in url:
    #     print(edits.BOLD + 'Article by:' + edits.END, 'CNN')
    # elif 'qz' in url:
    #     print(edits.BOLD + 'Article by:' + edits.END, 'Quartz')
    # elif 'wsj' in url:
    #     print(edits.BOLD + 'Article by:' + edits.END, 'The Wall Street Journal')
    # elif 'fivethirtyeight' in url:
    #     print(edits.BOLD + 'Article by:' + edits.END, 'Five Thirty Eight')
    # elif 'nytimes' in url:
    #     print(edits.BOLD + 'Article by:' + edits.END, 'The New York Times')
    # elif 'bloomberg' in url:
    #     print(edits.BOLD + 'Article by:' + edits.END, 'Bloomberg')
    # elif 'cnbc' in url:
    #     print(edits.BOLD + 'Article by:' + edits.END, 'CNBC')
    # elif 'theguardian' in url:
    #     print(edits.BOLD + 'Article by:' + edits.END, 'The Guardian')
    # elif 'huffingtonpost' in url:
    #     print(edits.BOLD + 'Article by:' + edits.END, 'The Huffington Post')
    # elif 'themarshallproject' in url:
    #     print(edits.BOLD + 'Article by:' + edits.END, 'The Marshall Project')
    # elif 'seattletimes' in url:
    #     print(edits.BOLD + 'Article by:' + edits.END, 'The Seattle Times')
    # else:
    #     print('Article publication not recognized')

def main():

    #print(article_edits())

    url_input = input("Please enter article URL: ")

    find_names(url_input)
    article_details(url_input)
    #url_grab(url_input)   

if __name__ == '__main__': main()