#!/usr/bin/env python
# coding: utf-8

# In[ ]:


year = int(input('Enter your year of birth(yyyy):'))
month = int(input('Enter your month of birth(mm):'))
day = int(input('Enter your day of birth(dd):')) 


# In[ ]:


import datetime as dt
from datetime import datetime, timezone


# In[ ]:


current_date = dt.datetime.now()
start_date = dt.datetime(year,month, day)


# In[ ]:


def utc_to_local(utc_dt):
    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)


# In[ ]:


current_date = utc_to_local(current_date)
start_date = utc_to_local(start_date)


# In[ ]:


years = (current_date - start_date)/365

years = str(years)


# In[ ]:


print("You're", years[0:2], "years old."  )

