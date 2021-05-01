#https://www.haberler.com/
from bs4 import BeautifulSoup
import selenium
import requests
from selenium import webdriver
PATH = "D:/WebDriver/bin/chromedriver.exe"
url = "https://www.ensonhaber.com/"
#hbBoxMainText
"""
driver = webdriver.Chrome(PATH)
driver.get(url)

className = driver.find_elements_by_class_name("news-left")
i=0
daily = []
sport = []
for news in className:
    daily.append(news.find_element_by_xpath('//div[@class="news-left"]').text)
    sport.append(news.find_element_by_xpath('//div[@class="cat-area__bottom"]').text)


print(daily, sport)
"""
source = requests.get(url)
soup = BeautifulSoup(source.content, "html.parser")
actualNews = soup.find_all("div", attrs={"class":"news-item__group"})
actualNews_date = soup.find_all("div", attrs={"class":"news-item__date"})
actualNews_category = soup.find_all("div", attrs={"class":"news-item__cat"})
actualNews_title = soup.find_all("div", attrs={"class":"news-item__title"})


actualNews_data = []
for new in actualNews_date:
    actualNews_data.append([new.text, new.text, new.text])
counter = 0
for new in actualNews_category:
    if (counter < len(actualNews_data)):
        actualNews_data[counter][1] = new.text
        counter += 1

counter = 0
for new in actualNews_title:
    if(counter < len(actualNews_data)):
        actualNews_data[counter][2] = new.text
        counter += 1


for i in range(len(actualNews_data)):
    print(actualNews_data[i][2])

file = open("news.txt", "w")
for i in range(0, len(actualNews_data)):
    information = actualNews_data[i][0] , "|", actualNews_data[i][1], "|", actualNews_data[i][2]
    file.write(str(information))

file.close()
