#!/usr/bin/env python
# coding: utf-8

# In[1]:


per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)
    else:
        print("clean data")
    finally:
        print("변환 완료")


# In[ ]:




