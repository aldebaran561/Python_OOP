#!/usr/bin/env python
# coding: utf-8

# In[7]:


class Car:
    
    def accelerate(self):
        return 'This car is on moving'

class Gas(Car):
    def accelerate(self):
        return 'This Car moves on gas'

class Electric(Car):
    def accelerate(self):
        return 'This Car moves on electric' 


# In[9]:


ferrari = Car()
print(ferrari.accelerate())

bus = Gas()
print(bus.accelerate())

tesla = Electric()
print(tesla.accelerate())


# In[ ]:




