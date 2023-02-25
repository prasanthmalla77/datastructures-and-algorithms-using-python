#!/usr/bin/env python
# coding: utf-8

# In[2]:


#linked list
#here the elements are not stored in a contiguous memory allocation
#the elements in linked list are linked using pointers
#each node in a linked list consists of atleast two parts:
#data,pointer(reference) to next node
class Node:
    # Function to initialize the node object
    def __init__(self,data):
        self.data=data # Assign data
        self.next=None# Initialize # next as null
 # Linked List class 
class Linkedlist:
    # Function to initialize the head
    # List object
    def __init__(self):
        self.head=None
    #now we should define a function which prints the whole list
    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
            
            
            
if __name__=="__main__":
    list1=Linkedlist()
    list1.head=Node(1)
    second=Node(2)
    third=Node(3)
    '''
    Three nodes have been created.
    We have references to these three blocks as head,
    second and third
  
    llist.head     second             third
        |             |                 |
        |             |                 |
    +----+------+     +----+------+     +----+------+
    | 1 | None |     | 2 | None |     | 3 | None |
    +----+------+     +----+------+     +----+------+
    
    credits: geek for geeks
    '''
    #now we should link the first node with second
    list1.head.next=second;
    second.next=third;
    list1.printList()        


# In[ ]:


"""if you have any confusion read this:
linked list is same as lists but here contiguous memory will not be allocated
hre we define nodes and data which will be linked with other nodes and data"""


# In[ ]:




