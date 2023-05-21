#!/usr/bin/env python
# coding: utf-8

# importamos las librerias necesarias para la realización de la actividad

# In[9]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[10]:


df = pd.read_csv("train.csv")


# In[11]:


df.head(10)


# In[12]:


df.info()


# In[13]:


df.describe()


# In[15]:


df["Age"].hist(bins=20)
plt.xlabel("Age")
plt.ylabel("Count")
plt.show


# In[17]:


survived_counts = df["Survived"].value_counts()
plt.bar(survived_counts.index, survived_counts.values)
plt.xticks([0,1], ["Not Survived", "Survived"])
plt.ylabel("Count")
plt.show()


# In[18]:


sex_counts = df["Sex"].value_counts()
plt.bar(sex_counts.index, sex_counts.values)
plt.xticks(["male","female"], ["male", "female"])
plt.ylabel("Count")
plt.show()


# In[ ]:




