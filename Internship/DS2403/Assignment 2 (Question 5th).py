#!/usr/bin/env python
# coding: utf-8
!pip install selenium
# In[77]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC


# In[78]:


driver=webdriver.Chrome()


# In[79]:


driver.get("https://www.amazon.in/")


# In[80]:


driver.maximize_window()


# In[81]:


Products=driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input")
Products.send_keys('laptop')


# In[82]:


submit=driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input")
submit.click()


# In[83]:


CPUType=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[5]/div[18]/span')
CPUType=driver.find_element(By.XPATH,'//i[@class="a-icon a-icon-checkbox"]').click()


# In[84]:


brand_title=[]
product_ratings=[]
product_price=[]


# In[86]:


title_tags=driver.find_elements(By.XPATH,'//h2[@class="a-size-mini a-spacing-none a-color-base s-line-clamp-2"]')
for i in title_tags:
    title=i.text
    brand_title.append(title)


# In[87]:


ratings_tags=driver.find_elements(By.XPATH,'//span[@class="a-size-base s-underline-text"]')
for i in ratings_tags:
    ratings=i.text
    product_ratings.append(ratings)


# In[88]:


price_tags=driver.find_elements(By.XPATH,'//span[@class="a-price-whole"]')
for i in price_tags:
    price=i.text
    product_price.append(price)


# In[90]:


print(len(brand_title),len(product_ratings),len(product_price))


# In[91]:


import pandas as pd 
df=pd.DataFrame({'Title':brand_title,'Ratings':product_ratings,'Price':product_price})

