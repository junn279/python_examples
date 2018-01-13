# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup


#from pyvirtualdisplay import Display
#display = Display(visible=0, size=(800, 600))
#display.start()

driver = webdriver.Chrome('./chromedriver')
driver.set_window_size(800,600)
driver.implicitly_wait(5)
driver.get('https://google.co.kr')
print("Done")

html = driver.page_source
bsObj = BeautifulSoup(html, "html.parser")

driver.quit()
#driver.close()

#display.stop()

