
# coding: utf-8

# # Introduction To The Dataset

# In[1]:


f = open('US_births_1994-2003_CDC_NCHS.csv', 'r')
data = f.read()
rows = data.split('\n')


# In[2]:


print(rows[0: 10])


# # Converting Data Into A List Of Lists

# In[3]:


def read_csv(filename):
    string_data = open(filename).read()
    string_list = string_data.split("\n")[1:]
    final_list = []
    
    for row in string_list:
        string_fields = row.split(",")
        int_fields = []
        for value in string_fields:
            int_fields.append(int(value))
        final_list.append(int_fields)
    return final_list
        
cdc_list = read_csv("US_births_1994-2003_CDC_NCHS.csv")


# In[4]:


cdc_list[0:10]


# # Calculating Number Of Births Each Month

# In[6]:


def month_births(data):
    births_per_month = {}
    
    for row in data:
        month = row[1]
        births = row[4]
        if month in births_per_month:
            births_per_month[month] = births_per_month[month] + births
        else:
            births_per_month[month] = births
    return births_per_month
    
cdc_month_births = month_births(cdc_list)


# In[7]:


cdc_month_births


# # Calculating Number Of Births Each Day Of Week

# In[8]:


def dow_births(data):
    births_per_dow = {}
    
    for row in data:
        dow = row[3]
        births = row[4]
        if dow in births_per_dow:
            births_per_dow[dow] = births_per_dow[dow] + births
        else:
            births_per_dow[dow] = births
    return births_per_dow
    
cdc_dow_births = dow_births(cdc_list)


# In[9]:


cdc_dow_births


# # Creating A More General Function

# In[10]:


def calc_counts(data, column):
    sums_dict = {}
    
    for row in data:
        col_value = row[column]
        births = row[4]
        if col_value in sums_dict:
            sums_dict[col_value] = sums_dict[col_value] + births
        else:
            sums_dict[col_value] = births
    return sums_dict

cdc_year_births = calc_counts(cdc_list, 0)
cdc_month_births = calc_counts(cdc_list, 1)
cdc_dom_births = calc_counts(cdc_list, 2)
cdc_dow_births = calc_counts(cdc_list, 3)


# In[11]:


cdc_year_births


# In[12]:


cdc_month_births


# In[13]:


cdc_dom_births


# In[14]:


cdc_dow_births

