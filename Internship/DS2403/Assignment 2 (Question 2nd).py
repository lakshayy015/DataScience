#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[30]:


driver= webdriver.Chrome()


# In[31]:


import selenium 
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[32]:


driver.get("https://www.shine.com/")


# In[34]:


skills=driver.find_element(By.CLASS_NAME,"form-control")
skills.send_keys('Data Scientist')


# In[35]:


location=driver.find_element(By.XPATH,"/html/body/div/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[2]/div/input")
location.send_keys('Bangalore')


# In[37]:


search_jobs=driver.find_element(By.XPATH,"/html/body/div/div[4]/div/div[2]/div[2]/div/form/div/div[2]/div/button")
search_jobs.click()


# In[41]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[65]:


location_tags=driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2"]')
for i in location_tags:
    location=i.text
    job_location.append(location)


# In[69]:


company_tags=driver.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_cName__mYnow"]')
for i in company_tags:
    company=i.text
    company_name.append(company)


# In[73]:


experience_tags=driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_jobIcon__3FB1t"]')
for i in experience_tags:
    experience=i.text
    experience_required.append(experience)


# In[75]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[77]:


import pandas as pd
df=pd.DataFrame({'Title':job_title,'Location':job_location,'Company_name':company_name,'Experience':experience_required})
df

