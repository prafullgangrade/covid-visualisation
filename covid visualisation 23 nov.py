#!/usr/bin/env python
# coding: utf-8

# In[68]:


#!/usr/bin/env python
# coding: utf-8

# ### Covid-19 World Health Organisation data
# - live data update day to day basis
# - covid spreadness in world

# ##### import libraries
# - required libraries pandas, numpy
# - matplotlib, seaborn
# In[139]:


#import libraries
import numpy as np
import pandas as pd
import seaborn as sns
from datetime import date
import matplotlib.pyplot as plt
#import plotly.express as px
get_ipython().run_line_magic('matplotlib', 'inline')


# #### load the data from WHO Website
# -go to [WHO.int](https://covid19.who.int/)

# In[140]:


url = "https://covid19.who.int/WHO-COVID-19-global-data.csv"
df = pd.read_csv(url)

#first 5 row
print(df.head())
df.shape


# In[141]:


#remove the white space before the column name
df.columns = df.columns.str.strip()
df.columns


# In[142]:


df.describe()


# In[143]:


#sort the data frame to know the highe affected country
high_cumulative_case = df.groupby('Country').max()['Cumulative_cases'].sort_values()
high_cumulative_case.sort_values(inplace=True, ascending=False)
most_affected = high_cumulative_case[:5]
most_affected

# In[145]:


#split month to grouping
df[['Year','Month','Day']] = df.Date_reported.str.split("-",expand=True,)


# In[146]:


df.columns


# In[147]:


#india graph
India_covid_case = df[(df['Country'] == 'India')]

# In[148]:


plot_data = df[['Country', 'New_cases',
       'Cumulative_cases', 'New_deaths', 'Cumulative_deaths','Month']]

my_labels = most_affected.index.tolist() 
my_data = most_affected.values.tolist()
plt.pie(my_data,labels=my_labels,autopct='%1.1f%%')
plt.title('hige affected Country wise covid distribution')
plt.axis('equal')
plt.show()


# # #### NEW CASES GRAPH

# # In[154]:

sns.lineplot(data=India_covid_case, x='Month', y='New_cases')
plt.title("India_covid New case monthly", size=12)
plt.show()

# # #### NEW DEATHS GRAPH

# # In[150]:


sns.lineplot(data=India_covid_case, x='Month', y='New_deaths')
plt.title("India_covid New death monthly", size=12)
plt.show()


# #### Cumulative_cases GRAPH

# In[151]:


sns.lineplot(data=India_covid_case, x='Month', y='Cumulative_cases')
plt.title("India_covid Cumulative_cases monthly", size=12)
plt.show()


# #### Cumulative_deaths GRAPH

# In[152]:


sns.lineplot(data=India_covid_case, x='Month', y='Cumulative_deaths')
plt.title("India_covid Cumulative_deaths monthly", size=12)
plt.show()


# In[ ]:




