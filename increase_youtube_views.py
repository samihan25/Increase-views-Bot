from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = input("Enter URL:-\n")
no_of_views = int(input("Enter no of Views:- "))
duration = float(input("Enter duration for each view (in seconds):- "))
print("")

for i in range(0,no_of_views):
    browser = webdriver.Firefox()
    browser.get(url)
    browser.find_element_by_tag_name('body').send_keys(Keys.SPACE)
    time.sleep(duration)
    print(str(i+1) + " iterations done")
    browser.quit()
