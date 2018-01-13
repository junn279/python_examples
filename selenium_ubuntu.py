# -*- coding: utf-8 -*-
from selenium import webdriver
import urllib
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import mysql.connector
from mysql.connector import errorcode
import time

# References : 
# https://christopher.su/2015/selenium-chromedriver-ubuntu/
# https://beomi.github.io/2017/10/29/HowToMakeWebCrawler-ImplicitWait-vs-ExplicitWait/

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
service_log_path = "/root/chromedriver.log"

#display = Display(visible=0, size=(800, 600))
#display.start()
driver = webdriver.Chrome("/root/chromedriver", chrome_options=options, service_log_path=service_log_path)

work_start_time = time.time()
print "Work start"
words = {"영상","검사","조영제"}
query = {"q" : " ".join(words)}  ## print(urllib.urlencode(query)) : q=%EC%98%81%EC%83%81+%EA%B2%80%EC%82%AC+%EC%A1%B0%EC%98%81%EC%A0%9C
print("Get Start")
driver.implicitly_wait(5)
driver.get('https://mediteam.us/search_crawl.php?'+urllib.urlencode(query))

#################
# 여기서 작업
#################

driver.close()
driver.quit()