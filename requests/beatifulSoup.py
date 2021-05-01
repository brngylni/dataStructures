# Example Web Scraping

from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys

PATH = "D:/WebDriver/bin/chromedriver.exe"

driver = webdriver.Chrome(PATH)
url = "http://www.instagram.com"

driver.get(url)
time.sleep(2)

username = "brngylni"
password = "1598742369b"

usernameField = driver.find_element_by_name("username")
passField = driver.find_element_by_name("password")
loginBtn = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")

usernameField.send_keys(username)
passField.send_keys(password)
loginBtn.click()
time.sleep(5)
driver.get(f"{url}/{username}")
time.sleep(3)

followers = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
followers.click()
time.sleep(3)
followersContainer = driver.find_element_by_css_selector("div[role=dialog] ul")
eachFollower = followersContainer.find_elements_by_css_selector("li")
counter = len(eachFollower)

scroll = webdriver.ActionChains(driver)


while True:
    followersContainer.click()
    scroll.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
    time.sleep(2)
    eachFollower = followersContainer.find_elements_by_css_selector("li")
    newCounter = len(eachFollower)
    if newCounter == counter:
        break
    else:
        print("New Counter : ", newCounter, "Old Counter : ", counter)
        counter = newCounter
        time.sleep(1)

eachFollower = followersContainer.find_elements_by_css_selector("li")

for follower in eachFollower:
    information = follower.find_element_by_css_selector("a").get_attribute("title")
    print(information)

driver.close()
