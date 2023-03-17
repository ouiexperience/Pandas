#!/usr/bin/env python
# coding: utf-8

# In[98]:


import numpy as np
import pandas as pd


# In[99]:


visits = pd.read_csv('C:/Users/anian/OneDrive/Desktop/Ani/DATA Analytics/Codeacademy/Panda/cool T shirts/Page_Visits_Funnel_Project/visits.csv',
                     parse_dates=[1])


# In[100]:


cart = pd.read_csv('C:/Users/anian/OneDrive/Desktop/Ani/DATA Analytics/Codeacademy/Panda/cool T shirts/Page_Visits_Funnel_Project/cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('C:/Users/anian/OneDrive/Desktop/Ani/DATA Analytics/Codeacademy/Panda/cool T shirts/Page_Visits_Funnel_Project/checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('C:/Users/anian/OneDrive/Desktop/Ani/DATA Analytics/Codeacademy/Panda/cool T shirts/Page_Visits_Funnel_Project/purchase.csv',
                       parse_dates=[1])


# In[101]:


print(visits.head())


# In[102]:


print(cart.head())


# In[103]:


print(checkout.head())


# In[104]:


print(purchase.head())


# # Let's see all the visitors and the ones that put a T shirt in the cart

# In[105]:


visitors_cart = pd.merge(visits,cart, how ="left")


# In[106]:


visitors_cart.user_id.count()


# In[107]:


cart.user_id.count()


# In[108]:


print(visitors_cart.head())


# # How many of the 2000 visitors that visited the site left without putting an article in the cart?

# In[109]:


num_of_no_cart= len(visitors_cart[visitors_cart.cart_time.isnull()])


# In[110]:


print(num_of_no_cart)


# # 1652 out of the 2000 visitors never made it to the cart

# # What percentage of the visitors ended up not placing an article in the cart?

# In[111]:


percentage_not_cart = float(num_of_no_cart)/float(visitors_cart.user_id.count())


# In[112]:


print(percentage_not_cart)


# # 82.6% of visiters did not place an article in the cart.

# In[113]:


visitors_checkout = pd.merge(cart,checkout, how ="left")


# In[114]:


print(visitors_checkout.head())


# In[115]:


count_no_checkout = len(visitors_checkout[visitors_checkout.checkout_time.isnull()])


# In[116]:


print(visitors_checkout.user_id.count())


# In[117]:


print(count_no_checkout)


# # What percentage of users put items in their cart, but did not proceed to checkout

# In[118]:


cart_not_checkout = float(count_no_checkout) / float(visitors_checkout.user_id.count())


# # 35% of the users that put items in their cart did not proceed to checkout

# In[119]:


all_data = visitors_cart.merge(visitors_checkout,how="left").merge(purchase, how="left")


# In[120]:


print(all_data.head())


# In[121]:


checkout = all_data.user_id.count() - len(all_data[all_data.checkout_time.isnull()])


# In[122]:


purchase = all_data.user_id.count()-len(all_data[all_data.purchase_time.isnull()])


# In[123]:


checkout_not_purchased = (all_data.user_id.count() - len(all_data[all_data.checkout_time.isnull()]))-(all_data.user_id.count()-len(all_data[all_data.purchase_time.isnull()]))


# In[124]:


print(checkout_not_purchased)


# # What percentage of users proceeded to checkout, but did not purchase a t-shirt?# 

# In[125]:


reached_checkout = all_data[~all_data.checkout_time.isnull()]

checkout_not_purchase = all_data[(all_data.purchase_time.isnull()) & (~all_data.checkout_time.isnull())]

checkout_not_purchase_percent = float(len(checkout_not_purchase)) / float(len(reached_checkout))

print("% of users who got to checkout but did not purchase:",checkout_not_purchase_percent)


# # 24.55% of users go to checkout but did not purchase

# In[126]:


print(reached_checkout.user_id.count())


# In[127]:


print(checkout_not_purchase.user_id.count())


# In[128]:


print("{} percent of users who visited the page did not add a t-shirt to their cart".format(round(percentage_not_cart*100, 2)))
print("{} percent of users who added a t-shirt to their cart did not checkout".format(round(cart_not_checkout*100, 2)))
print("{} percent of users who made it to checkout  did not purchase a shirt".format(round( checkout_not_purchase_percent*100, 2)))


# # The weakest part of the funnel is getting a person who visited the site to purchase a T-shirt. why are people not putting the T-shirt in the cart? Is the cart button visible enough? Is the cart button at several strategic places on the website? Is the ad targetted to the wrong audience? Are the T-shirts too expensive?   

# # How long does it take from the time people get on the website to the time they purchase the product?

# In[129]:


all_data["Time_to_checkout"]= all_data.purchase_time - all_data.visit_time
print(all_data.head(20))


# In[130]:


all_data.Time_to_checkout.mean()


# # In average it takes 43minutes and 12 seconds for a person visiting the website to purchase a T shirt
