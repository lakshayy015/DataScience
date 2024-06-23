#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install selenium')


# In[47]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings 
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[48]:


driver=webdriver.Chrome()


# In[49]:


driver.get("https://www.flipkart.com/")


# In[50]:


Products=driver.find_element(By.CLASS_NAME,"Pke_EE")
Products.send_keys('sneakers')
Products.click()


# In[51]:


brand_name=[]
product_description=[]
product_prices=[]


# In[52]:


brand_tags=driver.find_elements(By.XPATH,'//div[@class="syl9yP"]')
for i in brand_tags:
    brand=i.text
    brand_name.append(brand)


# In[53]:


description_tags=driver.find_elements(By.XPATH,'//a[@class="WKTcLC"]')
for i in description_tags:
    description=i.text
    product_description.append(description)


# In[54]:


description_tags=driver.find_elements(By.XPATH,'//a[@class="WKTcLC BwBZTg"]')
for i in description_tags:
    description=i.text
    product_description.append(description)


# In[55]:


prices_tags=driver.find_elements(By.XPATH,'//div[@class="Nx9bqj"]')
for i in prices_tags:
    prices=i.text
    product_prices.append(prices)


# In[56]:


print(len(brand_name),len(product_description),len(product_prices))


# In[61]:


import pandas as pd
df=pd.DataFrame({'Brand':brand_name,'Product Description':product_description,'Price':product_prices})
df

