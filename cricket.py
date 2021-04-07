from selenium import webdriver
from bs4 import BeautifulSoup


path="D:/chromedriver"
driver=webdriver.Chrome(path)
driver.get("https://www.cricbuzz.com/cricket-series/3472/indian-premier-league-2021/matches")
content = driver.page_source.encode('utf-8').strip()
soup=BeautifulSoup(content,"html.parser")
table= soup.findAll("div",{"class":""})
for matches in table:
    print(matches.text)
driver.quit()











