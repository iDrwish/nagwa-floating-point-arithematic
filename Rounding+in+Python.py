
# coding: utf-8

# # Floating Point Arithematic

# ## decimal Module Representation

# In[1]:


from decimal import ROUND_UP, Decimal, getcontext
from sympy import cos, sin, pi


# In[2]:


getcontext()


# In[3]:


getcontext().rounding = 'ROUND_HALF_UP'


# In[4]:


Decimal('4.4').quantize(Decimal('1.0'))


# In[5]:


Decimal('4.44444444').quantize(Decimal('1.0'))


# In[6]:


Decimal(4.5).quantize(Decimal('1'))


# In[7]:


Decimal('5.000005').quantize(Decimal('1.00000'))


# In[8]:


Decimal(-68.44499999999996).quantize(Decimal('1.00'))


# In[9]:


Decimal('-68.44499999999996').quantize(Decimal('1.000'))


# In[10]:


Decimal('-51.005').quantize(Decimal('1.00'))


# In[11]:


Decimal('-51.004999999999974').quantize(Decimal('1.00'))


# In[12]:


cos(pi/3)


# In[13]:


cos(2*pi/3)


# In[ ]:





# In[1]:


0.1 + 0.1 + 0.1


# In[10]:


0.1.as_integer_ratio()


# In[11]:


sum([0.1] * 10) == 1.0


# In[12]:


from math import fsum
fsum([0.1] * 10) == 1.0

