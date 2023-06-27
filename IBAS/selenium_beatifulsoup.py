from bs4 import BeautifulSoup
from selenium import webdriver
import time

url="https://www.youtube.com/watch?v=xkMyVijvpOQ"

driver = webdriver.Chrome('chromedriver')
driver.maximize_window()
driver.get(url)

time.sleep(5)
driver.execute_script("window.scrollTo(0, 500);")
for i in range(10):
      driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
      time.sleep(4)


soup = BeautifulSoup(driver.page_source,"html.parser")
driver.close()

comments =soup.select("yt-formatted-string#content-text")

for comment in comments:
   print(comment.text.replace('\n'," ").replace('\t',"").strip())