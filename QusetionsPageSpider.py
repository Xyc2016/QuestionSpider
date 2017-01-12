from urllib import request
from bs4 import BeautifulSoup
import re
link='https://www.zhihu.com/question/38478558'
def f1(link):
    webPage=request.urlopen(link).read()
    soup=BeautifulSoup(webPage,'html5lib')
    # print(soup.title.string)
    fileName='newFolder/'+link[-8:]+'.txt'
    file=open(fileName,'w')
    file.write(soup.title.string)
    search=re.compile(r'(?<=question/).*?(?=" data-id=)')
    newLinks=[]
    for item in search.findall(str(webPage)):
        if(len(item)==8):
            newLinks.append('https://www.zhihu.com/question/'+item)
    return newLinks

alreadyDownload=set()
Links=[]
Links.append(link)

while True:
    newLinks=[]
    for item in Links:
        if item not in alreadyDownload:
            try:
                newLinks+=f1(item)
                alreadyDownload.add(item)
            except Exception as e:
                continue

    Links=newLinks
    print(Links)
