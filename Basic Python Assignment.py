#!/usr/bin/env python
# coding: utf-8

# In[1]:


List1 = [15,23,27,16,19,65,34] #Q.1
List1


# In[2]:


List1.sort(reverse=False)  #Q.1(a)
List1


# In[5]:


List1.sort(reverse=True)  #Q.1(b)
List1


# In[6]:


min(List1) #Q.1(c)


# In[7]:


max(List1) #Q.1(d)


# In[34]:


List2 = [23221,36363,54433,43321,51658,56595] #Q.2
List2


# In[35]:


len(List2) #Q.2(a)


# In[36]:


List2[2:5] #Q.2(b)


# In[17]:


List2[-1] #Q.2(c)


# In[18]:


List2.pop(3)  #Q.2(d)
List2


# In[25]:


List3 = ["Mumbai", "Chennai", "Banglore", "Pune", "Hyderabad"]  #Q.3
List3


# In[26]:


List3[1]= "Mumbai"  #Q.3(a)
List3


# In[27]:


List3.append("Delhi")  #Q.3(b)
print(List3)


# In[28]:


List4= [1,2,3,1,5,2,6,5] #Q.4
List4


# In[29]:


List4.count(1) #Q.4(a)


# In[30]:


List4.remove(6) #Q.4(b)
List4


# Q.5 Using while loop print first 10 Natural numbers? 

# In[1]:


i = 0
while (i<=10):
    print(i)
    i = i+1


# In[1]:


List1 = [40,50,60,70,80,90]  #Q.6
i = len(List1) - 1
while i>=0:
    print(List1[i])
    i-=1


# Q.7 Write a python program to count the total number of digits in
# a number using a while loop?

# In[18]:


num = 55555
count = 0

while num != 0:
    num //= 10
    count += 1
print(str(count))


# Q.8 Write a code to display only those numbers from given list
# that satisfy the following conditions.
# numbers = [45, 32, 140, 170, 352, 425, 45]?
# a) The number must be divisible by five
# b) If the number is greater than 500, then stop the loop

# In[18]:


numbers = [45, 32, 140, 170, 352, 425, 45]  #Q.8(a)The number must be divisible by five
for i in numbers:
    if i % 5 == 0:
        print(i)


# In[20]:


numbers = [45, 32, 140, 170, 352, 425, 45]  #Q.8(b) If the number is greater than 500, then stop the loop
for i in numbers:
    if i > 500:
        stop


# Q.9 Write a python code to display numbers from -10 to -1 using
# for loop?

# In[20]:


for i in range(-10,0):
    print(i)


# Q.10 Use a loop to display elements from a given list present at
# odd index positions.
# List_1 = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110]

# In[17]:


List_1 = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110]
y = len(List_1)
for i in range(y):
    if i % 2 != 0:
        print(List_1[i])

