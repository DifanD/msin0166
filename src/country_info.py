# -*- coding: utf-8 -*-
"""Country_info.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aCaDUX7-LgspZoJLmfdQHh2dTvETbZMp
"""

!pip install selenium

# Commented out IPython magic to ensure Python compatibility.
# %%shell
# # Add debian buster
# cat > /etc/apt/sources.list.d/debian.list <<'EOF'
# deb [arch=amd64 signed-by=/usr/share/keyrings/debian-buster.gpg] http://deb.debian.org/debian buster main
# deb [arch=amd64 signed-by=/usr/share/keyrings/debian-buster-updates.gpg] http://deb.debian.org/debian buster-updates main
# deb [arch=amd64 signed-by=/usr/share/keyrings/debian-security-buster.gpg] http://deb.debian.org/debian-security buster/updates main
# EOF
# 
# # Add keys
# apt-key adv --keyserver keyserver.ubuntu.com --recv-keys DCC9EFBF77E11517
# apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 648ACFD622F3D138
# apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 112695A0E562B32A
# 
# apt-key export 77E11517 | gpg --dearmour -o /usr/share/keyrings/debian-buster.gpg
# apt-key export 22F3D138 | gpg --dearmour -o /usr/share/keyrings/debian-buster-updates.gpg
# apt-key export E562B32A | gpg --dearmour -o /usr/share/keyrings/debian-security-buster.gpg
# 
# # Prefer debian repo for chromium* packages only
# # Note the double-blank lines between entries
# cat > /etc/apt/preferences.d/chromium.pref << 'EOF'
# Package: *
# Pin: release a=eoan
# Pin-Priority: 500
# 
# Package: *
# Pin: origin "deb.debian.org"
# Pin-Priority: 300
# 
# 
# Package: chromium*
# Pin: origin "deb.debian.org"
# Pin-Priority: 700
# EOF

!apt-get update
!apt-get install chromium chromium-driver
from selenium import webdriver
def web_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--verbose")
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument("--window-size=1920, 1200")
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    return driver

! pip install bs4
! pip install lxml
import requests
import re
import pandas as pd
import time
import random
from datetime import date, timedelta
import pandas as pd
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup as soup
from urllib.parse import urljoin
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By

# Find unique countries in the column 'country' for latter extraction purpose
country_name= country_corruption_df.country.unique()

# Webscrape ISO code and country name from IBAN https://www.iban.com/country-codes
country_info = ['country', 'code']
country_table = pd.DataFrame(columns=country_info)
country_url = 'https://www.iban.com/country-codes'
response = requests.get(country_url)
country_link = soup(response.text, "lxml")
country= country_link.find_all('td')

country_name_list=[]
country_name=[]
for i in country:
  country_name_list.append(i.text)

# Country name list 
country_name=[]
for i in range(0,len(country_name_list),4):
  country_name.append(country_name_list[i])

# Country Code list 
country_code=[]
for i in range(1,len(country_name_list),4):
  country_code.append(country_name_list[i])

# Concat two lists into a dataframe
merge_country = {'country_name':country_name, 'country_code':country_code}
country_info = pd.DataFrame(merge_country)

# Verify the country information
print(country_info)



