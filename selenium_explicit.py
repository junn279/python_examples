# -*- coding: utf-8 -*-

from selenium import webdriver
import urllib
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

#http://www.marinamele.com/selenium-tutorial-web-scraping-with-selenium-and-python
#https://beomi.github.io/2017/10/29/HowToMakeWebCrawler-ImplicitWait-vs-ExplicitWait/
#https://christopher.su/2015/selenium-chromedriver-ubuntu/
#chrome_options.add_argument('--no-sandbox')
#https://beomi.github.io/2017/10/29/HowToMakeWebCrawler-ImplicitWait-vs-ExplicitWait/

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
service_log_path = "/root/chromedriver.log"
driver = webdriver.Chrome("/root/chromedriver", chrome_options=options, service_log_path=service_log_path)

try:
	driver.get('https://mediteam.us/search_crawl.php?'+urllib.urlencode(query))
	element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID , "___gcse_0")))
except TimeoutException as err:
	print err
	driver.quit()
	process.exit()
finally:
	print("Done")


print("Get Done")
html = driver.page_source
bsObj = BeautifulSoup(html, "html.parser")
titles = bsObj.findAll("a",{"class":"gs-title"})
links = bsObj.findAll("div",{"class":"gs-bidi-start-align gs-visibleUrl gs-visibleUrl-long"})

analysis_time = time.time()
print "Done: ", (analysis_time - work_start_time)

driver.quit()
#driver.close() 프로세스가 죽지 않는다