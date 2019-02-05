
# coding: utf-8

# # LinkedList

#  A linked list consists of nodes where each node contains a data field and a reference(link) to the next node in the list. <br>
# - Consists of 2 parts <br>
# - 1. Data<br> 2. Pointer to the next node <br>

# Different types of LinkedList:
# - Singly LinkedList <br>
# - Doubly LinkedList <br>
# - Circular LinkedList<br>
# 

# Node Operations:
# - get.next()
# - get.next(node)
# - get.data() # getters 
# - set.data(data) # setters
# - has.next()
# - to_string()

#  List Operations:
#  - get.size()
#  - find.data()
#  - add(data)
#  - remove(data)
#  - print(list)
#  - sort()
#  

# Singly LinkedList

# In[19]:

class Node(object):

   def __init__ (self, d, n = None):
       self.data = d
       self.next_node = n

   def get_next (self):
       return self.next_node

   def set_next (self, n):
       self.next_node = n

   def get_data (self):
       return self.data

   def set_data (self, d):
       self.data = d


class LinkedList (object):

   def __init__(self, r = None):
       self.root = r
       self.size = 0

   def get_size (self):
       return self.size

   def add (self, d):
       new_node = Node (d, self.root)
       self.root = new_node
       self.size += 1

   def remove (self, d):
       this_node = self.root
       prev_node = None

       while this_node:
           if this_node.get_data() == d:
               if prev_node:
                   prev_node.set_next(this_node.get_next())
               else:
                   self.root = this_node.get_next()
               self.size -= 1
               return True		# data removed
           else:
               prev_node = this_node
               this_node = this_node.get_next()
       return False  # data not found

   def find (self, d):
       this_node = self.root
       while this_node:
           if this_node.get_data() == d:
               return d
           else:
               this_node = this_node.get_next()
       return None


# In[20]:

myList = LinkedList()
myList.add(5)
myList.add(8)
myList.add(12)
print("size="+str(myList.get_size()))


# In[21]:

print("size="+str(myList.get_size()))
myList.remove(8)
print("size="+str(myList.get_size()))
print(myList.remove(12))


# In[22]:

print("size="+str(myList.get_size()))
print(myList.find(5))


# In[ ]:




# In[ ]:



