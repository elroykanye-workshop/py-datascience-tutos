#!/usr/bin/env python
# coding: utf-8

# from collections import Counter
# import matplotlib.pyplot as plt
# import random# Statistics
# When working with small sets of data, it is easy to show and explain the data in a simple structure such as a list.
# For a much larger dataset, it becomes unweildy and strainous. For this reason, we use statistics to distill and communicate relevant featues of our data.
# 
# Through a combination of word-of-mouth and luck, DataSciencester has grown to dozens of members, and the VP of Fundraising asks you for some sort of description of how many friends your members have that he can include in his elevator pitches.

# In[1]:


from collections import Counter
import matplotlib.pyplot as plt
import random


# In[2]:


# generate a random number of friends
def generate_rand_friends(n,k):
    random.seed(k)
    return [int(100* random.random()) for x in range(n)]
print(generate_rand_friends(1000,3))

# generate random mins
def generate_rand_mins(n,s):
	random.seed(s)
	return [int(1440*random.random()) for x in range(n)]


# In[3]:


num_friends = generate_rand_friends(1000,5)
# first , we put the friend data into a histogram using Counter and plt.bar
friend_counts = Counter(num_friends)
xs = range(100)
ys = [friend_counts[x] for x in xs]
plt.bar(xs,ys)
plt.title("Histogram of Friend Counts")
plt.axis([0,101,0,25])
plt.xlabel("# of friends")
plt.ylabel("# of people")


# In[4]:


# lets generating some statistics
num_points = len(num_friends)

# get largest and smallest value
largest_val = max(num_friends)
smallest_val = min(num_friends)

# or
sorted_values = sorted(num_friends)
smallest_value = sorted_values[0]
second_smallest_value = sorted_values[1]
second_largest_value = sorted_values[-2]


# ### Yo! Hope you are keeping up
# Cause we only just got started :)

# ## Central Tendencies
# Usually, we want some notion of where our data is centered. We mostly use mean or average for this, which is just a sum of the the data divided by its count

# In[5]:


def mean(data):
    return sum(data)/len(data)
num_friends = generate_rand_friends(1000,5)
print(mean(num_friends))


# In[6]:


# also, we may need the median
def median(data):
    data = sorted(data)
    if(len(data) % 2 == 0):
        return (data[len(data)//2]
                + data[len(data)//2]+1)/2
    else:
        return data[int(len(data)/2)]
print(median([1,2,3,4]))
print(median(num_friends))


# In[7]:


def quantile(x,p):
    p_index = int(p*len(x))
    return sorted(x)[p_index]


# In[8]:


print(quantile(num_friends, 0.10))
print(quantile(num_friends, 0.25))
print(quantile(num_friends, 0.50))
print(quantile(num_friends, 0.75))
print(quantile(num_friends, 0.90))


# In[9]:


# less commonly, you may want to look at the node or the most common value
def mode(data):
    the_counter = Counter(data)
    the_mode = 0
    for key in the_counter.keys():
        if the_counter.get(key) > the_mode:
            the_mode = key
    return the_mode
print(mode(num_friends))
for item in sorted(Counter(num_friends).items()): print(item)


# In[ ]:




