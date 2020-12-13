#!/usr/bin/env python
# coding: utf-8

# In[1]:


def 함수0(num) :                  #함수2가 2이므로 함수1이 12로 나오고 함수 0은 14로 나오므로 값은 28로 출력된다.
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c)


# In[ ]:




