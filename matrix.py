#!/usr/bin/env python
# coding: utf-8

# In[23]:


import numpy as np
a=np.array([[1,2,3,4],[2,3,4,5],[8,9,0,1],[1,4,5,6]])
m=np.reshape(a,(4,4))
m


# In[24]:


#accessing elements in matrix
print("/n Accessing Elements:")
print(a[1])


# In[25]:


print(a[1][2])


# In[31]:


#adding elements to the matrix
m=np.append(m,[[1,2,3,7]],0)
m


# In[32]:


m=np.delete(m,[1],0)


# In[33]:


m


# In[ ]:




