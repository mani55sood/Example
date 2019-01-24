#!/usr/bin/env python
# coding: utf-8

# In[50]:


import numpy as np


# In[70]:


step =0
a = []
for i in range(500):
    step = 0 
    for i in range(0,500):
        num= np.random.randint(1,7)
        if (num <=3):
            step -=1
        elif  (num == 4 or num == 5 ):
              step +=1
        elif (num==6):
            b=np.random.randint(1,7)
            step=step+b
    a.append(step)

    


# In[71]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.hist(a,bins=50)


# In[ ]:




