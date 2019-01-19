import sqlite3
import requests as r
from bs4 import BeautifulSoup as bs

headers = {"accept":"*/*" ,"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
base_url = "https://hh.ru/search/vacancy?search_period=7&clusters=true&area=1&text=python&enable_snippets=true&page=00"

end_list = []
for j in range(0,20):
    if j<10:
        t = '0'+str(j)
        end_list.append(t)
    else:
        t = str(j)
        end_list.append(t)
'''
print(end_list)

for q in range(0, len(end_list)):
    base_url = base_url[0:-2]
    base_url = base_url + end_list[q]
    print(base_url)
'''   
def parser(base_url, headers, python_list):
    session = r.Session()
    request = session.get(base_url, headers = headers)
    if request.status_code == 200:
        soup = bs(request.content,"html.parser")
        divs = soup.find_all("div", attrs= {"data-qa":"vacancy-serp__vacancy"})
        #print(divs)
        for div in divs:
            title = div.find('a', attrs = {'data-qa':'vacancy-serp__vacancy-title'}).text
            href = div.find('a', attrs = {'data-qa':'vacancy-serp__vacancy-title'})['href']
            company = div.find('a', attrs = {'data-qa':'vacancy-serp__vacancy-employer'}).text
            python_list.append({'title':title,'href':href,'company':company })
    else:
        print('Error')

python_list = []  
parser(base_url, headers, python_list)
print(python_list)
