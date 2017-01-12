from urllib import request
from bs4 import BeautifulSoup
import re
link='https://www.zhihu.com/question/38478558'
def realTitle(title):
    s=''
    for c in title:
        if c!='\n':
            s+=c
    return s

def PageSearch(link, topic=None):
    webPage=request.urlopen(link).read()
    soup=BeautifulSoup(webPage,'html5lib')
    topicidSet=set()

    if topic!=None:
        for A in soup.find_all('a'):
            if A.get('data-topicid'):
                topicidSet.add(A.get('data-topicid'))
        if topic not in topicidSet:
            return []

    fileName='linkFolder/'+link[-8:]+'.desktop'
    file=open(fileName,'w')
    text = '[Desktop Entry]\nEncoding=UTF-8\nName=' + realTitle(soup.title.string) + '\nType=Link\nURL=https://www.zhihu.com/question/'+link[-8:]+'\nIcon=text-html'
    file.write(text)
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
                newLinks+=PageSearch(item)
                alreadyDownload.add(item)
            except Exception as e:
                continue

    Links=newLinks
    print(Links)

