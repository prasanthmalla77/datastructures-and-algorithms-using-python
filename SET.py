#!/usr/bin/env python
# coding: utf-8

# In[3]:


#sets are mainly used to get rid of the negative values
#we should use set function to define a set so that it will print all the values without duplication
set1=set(["prasanth","malla","naidu","prasanth"])
print("\nset:",set1)


# In[6]:


print("\nElements of set:")
for i in set1:
    print(i,end="\n")


# In[7]:


#checking whether a element is in set or not using in operator
print("prasanth" in set1)


# In[15]:


#set are immutable to remove the mutability of anny set we can convvert it into frozen set
normal_set=set(["prasanth","malla","naga"])
print(normal_set)
normal_set.add("prasu")
print("normal set after adding new element:",normal_set)
frozen_set1=frozenset(normal_set)
print(frozen_set1)
#we cant add or rremove elements from frozen set, we can make all other operations on a frozen set


# In[ ]:




