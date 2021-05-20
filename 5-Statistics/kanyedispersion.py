#!/usr/bin/env python
# coding: utf-8

# ## Dispersion
# This refers to measures of how spread out our data is. Typically, they are statistics for which values near zero signify not spread out at all and for which large values signify very spread out.
# For your example, a simple measure is the range, which is just the difference between the largest and smallest elements.
# 

# In[20]:


import kanyevect as kvec
import descsingleds as kdesc
import math


# In[11]:


# we will use data range
num_friends = kdesc.generate_rand_friends(1000,5)
def data_range(x):
    return max(x) - min(x)
data_range(num_friends)


# In[18]:


# a more complex measure of dispersion is variance, which is computed as
def de_mean(x):
    x_bar = kdesc.mean(x)
    return [x_i - x_bar for x_i in x]
def variance(x):
    n = len(x)
    deviations = de_mean(x)
    result = kvec.sum_of_squares(deviations)/(n-1)
    return result
variance(num_friends)


# In[21]:


# for standard deviation
def standard_deviation(x):
    return math.sqrt(variance(x))
standard_deviation(num_friends)


# A more robust alternative computes the difference between the 75th percentile value and
# the 25th percentile value:

# In[23]:


def interquartile_range(x):
    return kdesc.quantile(x, 0.75) - kdesc.quantile(x, 0.25)
interquartile_range(num_friends)


# In[ ]:




