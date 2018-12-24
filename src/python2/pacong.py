# -* - coding: UTF-8 -* -  

from bs4 import BeautifulSoup as bs
import requests
import urllib2

zufang_url = 'https://cq.lianjia.com/zufang/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}

req = urllib2.Request(url=zufang_url,headers=headers)#这里要注意，必须使用url=url，headers=headers的格式，否则回报错，无法连接字符
response = urllib2.urlopen(req)#注意，这里要用req，不然就被添加useragent
text = response.read()

soup = bs(text, 'lxml')

arr = soup.find_all('div', class_='content__list--item')
href = arr[0].a.get('href')
item_url = 'https://cq.lianjia.com'+ href

print(item_url)