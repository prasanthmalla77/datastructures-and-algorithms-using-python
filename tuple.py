#!/usr/bin/env python
# coding: utf-8

# In[2]:


#python tuples are same as lists but here we cant change the tuple once it is defined 
#that means a tuple is same aas list bbut immutable
#tuples are written using ()
tuple1=("hello","prasanth","malla")
print("\ntuple with the use of string:")
print(tuple1)


# In[6]:


#we can convert a list into tuple
list1=[1,2,3,4,22,3,4,8]
tuple2=tuple(list1)
print("\nlist:",list1)
print("\ntuple:",tuple2)


# In[11]:


print("print first element of tuple:")
#as tuple is indexed we can get values using tuple indexing
print(tuple2[0])


# In[13]:


#we can use negative indexing using for getting the last element of the tuple
print("\n last element of tuple using negative indexing[tuple[0]]:",tuple2[-1])


# In[15]:


tuple2[::-1]
#reversing of a tuple can be done using negative indexing


# In[ ]:




