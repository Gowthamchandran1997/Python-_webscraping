import requests
import bs4
import pywhatkit


url=''

res= requests.get(url)
soup=bs4.BeautifulSoup(res.text,'html.parser')

score=soup.findAll("div",{"class":"cb-col cb-col-100 cb-scrd-hdr-rw"})
a=[]
for i in score:
    a.append(i.text)
livescore=a[0]
second=a[1]
final=livescore + " " + second
print(final)

pywhatkit.sendwhatmsg("+91********",final,20,10)








