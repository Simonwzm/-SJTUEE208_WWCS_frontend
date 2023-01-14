# SJTU EE208

import os
import re
import string
import sys
import urllib.error
import urllib.parse
import urllib.request
import threading
import queue
import time

from bs4 import BeautifulSoup


count = 0

def valid_filename(s):
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    s = ''.join(c for c in s if c in valid_chars)
    return s


def get_page(page): #获取页面,返回soup
    req = urllib.request.Request(page)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36')    
    content = urllib.request.urlopen(req,data = None,timeout=3).read().decode('utf-8','ignore')
    soup = BeautifulSoup(content, 'html.parser')
    return soup

def get_content(soup): #获取页面内容
    content = ""
    for i in soup.find_all('p'):
        if i.string != None:
            content += i.string
    return content

def get_image(soup):
    img_src = ""
    for i in soup.find_all('img',{"border":"1"}):
        img_src += i.get('src')
        img_src += "\n"
    return img_src

def get_time(soup):#获取时间(未完成,问题在于获取时分秒)
    news_time = ""
    flag = 0
    #  " 2022-11-13 10:41:11 " 
    for i in soup.find_all('span',{"class":"fl time2"}):
        news_time += i.text
    endp=news_time.find(':')+3
    news_time=news_time[0:endp]
    news_time=news_time.replace('年','\n')
    news_time=news_time.replace('月','\n')
    news_time=news_time.replace('日','\n')
    news_time=news_time.replace(':','\n')
    return news_time


def get_title(soup):
    title = ""
    for i in soup.find_all('h1',{"class":"toph1"}):
        if i.string != None:
            title += i.string
    return title

def get_url(soup,page,max_page):#获取url(未完成)(失败，因为url是动态加载的)
    url = str(page)
    url += "\n"
    cnt = 0
    for i in soup.find_all('a',{"targe":"_blank"}):
        if i.get('href') != None:
            print(i.string)
            if i.get('href')[0:4] == "http":
                url += i.get('href')
                url += "\n"
                cnt += 1
                if(cnt == max_page):
                    break
    return url

def make_folder():  #建立根目录
    folder = 'www_stdaily_com'  
    if not os.path.exists(folder):
        os.mkdir(folder)
        print(folder)
    
def add_page(page):  #对每个页面创建文件夹
    folder = page
    folder = valid_filename(folder)
    if not os.path.exists(folder):
        os.mkdir(folder)
    soup = get_page(page)

    flag=True

    f1 = "content.txt"
    f2 = "image.txt"
    f3 = "time.txt"
    f4 = "title.txt"
    f5 = "url.txt"

    content = open(os.path.join(folder, f1), 'w',encoding='utf-8')
    content.write(get_content(soup))
    if(not get_content(soup)):
        flag=False
    content.close()

    image = open(os.path.join(folder, f2), 'w',encoding='utf-8')
    image.write(get_image(soup))
    image.close()

    time = open(os.path.join(folder, f3), 'w',encoding='utf-8')
    time.write(get_time(soup))
    if(not get_time(soup)):
        flag=False
    time.close()

    title = open(os.path.join(folder, f4), 'w',encoding='utf-8')
    title.write(get_title(soup))
    if(not get_title(soup)):
        flag=False
    print(get_title(soup))
    title.close()

    url = open(os.path.join(folder, f5), 'w',encoding='utf-8')
    url.write(get_url(soup,page,10))
    if(not get_url(soup,page,10)):
        flag=False
    url.close()

    if not flag:
        os.remove(folder)
        raise IndexError


def get_web_list(seed):
    soup = get_page(seed)
    web_list = []

    for j in soup.find_all('a',{"target":"_blank"}):
        if len(j.text)<8:
            continue
        web_list.append(j.get('href'))
    return web_list

def gen_nxt(cnt):
    origin = "http://app.tech.china.com.cn/news/live.php?channel=%E7%A7%91%E6%8A%80&p="
    nxt_page = origin + str(cnt) 
    return nxt_page 


def crawl(max_page):
    web_list = []
    cnt = 0
    index = 0
    page_cnt = 1
    while(cnt < max_page):
        if index == len(web_list):
            nxt_page = gen_nxt(page_cnt)
            new_web_list = get_web_list(nxt_page)
            web_list = web_list + new_web_list
            page_cnt+=1
        page = web_list[index]
        try:
            if not 'http://tech.china.com' in page:
                raise TypeError
            add_page(page)
            index += 1
            cnt += 1
            print(cnt)
        except:
            index+=1





if __name__ == '__main__':
    # make_folder()
    crawl(6000 )
