#present: This program gets addresses from a Google Maps search and outputs data.
    # Only works if you search specific place in one word and it finds it in one word.
    # Could not get to work with Firefox webdriver.
#future: Checks to see if place is currently open.
    # Get certain properties from class instead of array so can check what it is if different number of lines for entries.
    # Go to next page to check more results if possible.

#import time
#time.sleep(5)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
import os

input = "target"

#launch url
url = "https://www.google.com/maps/search/"+input.lower()

# create a new Firefox session
driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(30)
driver.get(url)
iffy = True

sections = driver.find_elements_by_class_name('section-result-text-content')
for section in sections:
    sectionText = section.text
    lineArray = sectionText.splitlines()
    for line in lineArray:
        if input.lower() in line.lower():
            print(line)
    #if iffy:
    #    print(sectionText)
    #iffy = False

#addresses = driver.find_elements_by_class_name('section-result-location')
#for a in addresses:
#    print(a.text)
