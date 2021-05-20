#!/usr/bin/env python
# coding: utf-8

# The simplest form of vectors is as a list of numbers. A list of numbers corresponds to a vector in 3D space. Example below:

# In[1]:


height_weight_age = [70, 170, 40]
grades = [95,60,75,62]


# The problem with the list approach is that we may want to perform arithmetic operations on vectors.
# Python lists are not vectors and we will need to build these arithmetic tools ourselves.

# In[23]:


# This can be implemented by zipping the vectors together 
# and using a list comprehension to add the corresponding elements

def vector_add(v,w):
    # adds corresponding elements
    return [v_i + w_i 
            for v_i, w_i in zip(v,w)]
print(vector_add([1,2],[3,4]))


# In[24]:


# similarly, to subtract two vectors, we just subtract corresponding elements

def vector_subtract(v, w):
    return [v_i - w_i
            for (v_i, w_i) in zip(v,w)]
print(vector_subtract([1,2],[3,4]))


# In[28]:


# we also want to component wise sum a list of vectors

def vector_sum(vectors):
    vector_result = vectors[0]
    for vector in vectors[1:]:
        vector_result = vector_add(vector_result, vector)
    return vector_result
v1 = [1,2,3,4]
v2 = [5,2,6,8]
v3 = [5,9,0,2]
print(vector_sum([v1,v2,v3]))


# In[30]:


# we will also need to be able to multiply a vector by a scalar, which we do simply by multiplying each element of the vector by that number
def scalar_multiple(vector, k):
    return [k * x for x in vector]
print(scalar_multiple([1,2], 4))


# In[46]:


# the dot product of two vector is the sum of their componentwise product

def dot_product(v, w):
    return sum([v_i * w_i
           for (v_i, w_i) in zip(v,w)])
print(dot_product([2,3],[5,6]))


# In[42]:


# using this, it is easy to compute a vector's sum of squares

def sum_of_squares(v):
    return dot_product(v,v)
print(sum_of_squares([3,4]))


# In[47]:


# we can use the sum of squares to compute the vector's magnitude
import math
def magnitude(v):
    return math.sqrt(sum_of_squares(v))
print(magnitude([3,4]))


# In[50]:


# we now have what is needed to compute the squared distance
def squared_distance(v,w):
    return sum_of_squares(vector_subtract(v,w))
print(squared_distance([1,2],[3,4]))


# In[51]:


# and finally, the distance between two vectors
import math
def distance(v,w):
    return math.sqrt(squared_distance(v,w))
print(distance([1,2],[3,4]))


# In[ ]:




