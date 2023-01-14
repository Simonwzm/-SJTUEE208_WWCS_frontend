from newspaper import Article
import sys, os, threading, time,string
import nltk

def valid_filename(s):
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    s = ''.join(c for c in s if c in valid_chars)
    return s

if __name__ == '__main__':
    root='webb'
    for web in os.listdir(root):
            webpath="webb/"+web
            for page in os.listdir(webpath):
                # try:
                pagepath=webpath+'/'+page
                urlpath=pagepath+'/url.txt'
                with open(urlpath,'r') as tar:
                    reader=tar.read()
                    print(reader)
                    article=Article(reader,language='zh')
                    article.download()
                    article.parse()
                    print(article.title)
                    article.nlp()
                    keyword=article.keywords
                    print(keyword)
                    kwd = open(os.path.join(pagepath, 'keyword.txt'), 'w',encoding='utf-8')
                    for kw in keyword:
                        kwd.write(kw)
                        kwd.write('\t')
                tar.close()  
                # except:
                #     print("Failed")
                #     continue