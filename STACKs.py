#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#stack is a linear data structure that stores items in a last-in-first-out order


# In[7]:


#in stack element is added and removed from the same end
"""
empty() – Returns whether the stack is empty – Time Complexity: O(1)
size() – Returns the size of the stack – Time Complexity: O(1)
top() – Returns a reference to the topmost element of the stack – Time Complexity: O(1)
push(a) – Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)
pop() – Deletes the topmost element of the stack – Time Complexity: O(1)
credits: geekforgeeks
"""
#implementation of stacks usinng python
stack=[]
stack.append("prasu")
stack.append("malla")
stack.append("naga")
print("initial staclk:",stack)
print("elements removed from stack:")
print(stack.pop())
print(stack.pop())
print(stack.pop())
print("\nelements after elemeennts are popped:")
print(stack)


# In[ ]:




