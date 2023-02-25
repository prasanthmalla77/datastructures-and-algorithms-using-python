#!/usr/bin/env python
# coding: utf-8

# In[1]:


#dictonary is a unordered collection of data that stores data in the format of key:value pair.
dict1={"1":"2","name":"prasanth"}
print(dict1)


# In[3]:


print("\naccessinng elements of a dictionary using key:")
print(dict1["name"])


# In[4]:


dict2={x:x**3 for x in [1,2,3,4,55]}


# In[5]:


print(dict2)


# In[7]:


for i in dict2.keys():
    print(i,end=" ")


# In[10]:


if "two" in dict2:
    print("yes")
elif "166375" not in dict2:
    print("yes")


# In[ ]:




