#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().system('pip install selenium')


# In[3]:


driver = webdriver.Chrome()


# In[2]:


import selenium 
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[4]:


driver.get("https://www.naukri.com/")


# In[5]:


designation=driver.find_element(By.CLASS_NAME,"suggestor-input")
designation.send_keys('Data Scientist')


# In[6]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input")
location.send_keys('Delhi/NCR')


# In[7]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[8]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[9]:


salary=driver.find_element(By.XPATH,"/html/body/div/div/main/div[1]/div[1]/div/div/div[2]/div[5]/div[2]/div[2]/label/p/span[1]")
salary.click()


# In[10]:


title_tags=driver.find_elements(By.XPATH,'//div[@class="cust-job-tuple layout-wrapper lay-2 sjw__tuple "]/div/a')
for i in title_tags:
    title=i.text
    job_title.append(title)


# In[11]:


location_tags=driver.find_elements(By.XPATH,'//span[@class="locWdth"]')
for i in location_tags:
    location=i.text
    job_location.append(location)
    
company_tags=driver.find_elements(By.XPATH,'//div[@class=" row2"]/span/a[1]')
for i in company_tags:
    company=i.text
    company_name.append(company)

experience_tags=driver.find_elements(By.XPATH,'//span[@class="expwdth"]')
for i in experience_tags:
    experience=i.text
    experience_required.append(experience)



# In[12]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[14]:


import pandas as pd 
df=pd.DataFrame({'Title':job_title,'Location':job_location,'Company_name':company_name,'Experience':experience_required})
df

