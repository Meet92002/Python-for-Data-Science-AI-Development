# RandomUser API

# Get Method

# get_cell()                      get_login_md5()
# get_city()                      get_login_salt()
# get_dob()                       get_login_sha1()
# get_email()                     get_login_sha256()
# get_first_name()                get_nat()
# get_full_name()                 get_password()
# get_gender()                    get_phone()
# get_id()                        get_picture()
# get_id_number()                 get_postcode()
# get_id_type()                   get_registered()
# get_info()                      get_state()
# get_last_name()                 get_street()
# get_username()                  get_zipcode()


from randomuser import RandomUser
import pandas as pd
import json

import requests

r = RandomUser()
# print("r", r)
some_list = r.generate_users(10) 
# print(some_list)

# The "Get Methods" functions mentioned at the beginning of this notebook,
#  can generate the required parameters to construct a dataset.
name = r.get_full_name()

# Let's say we only need 10 users with full names and their email addresses.
#  We can write a "for-loop" to print these 10 users.

for user in some_list:
    # print (user.get_full_name()," ",user.get_email())

# Exercise 1 /////////////////////////////////////////////////////

# In this Exercise, generate photos of the random 10 users.
 for user in some_list:
    # print(user.get_picture())

    def get_users():
        users =[]
        for user in r.generate_users(10):
            users.append({"Name":user.get_full_name(),
                      "Gender":user.get_gender(),
                      "City":user.get_city(),
                      "State":user.get_state(),
                      "Email":user.get_email(),
                      "DOB":user.get_dob(),
                      "Picture":user.get_picture()})
        print("users", pd.DataFrame(users))
        return pd.DataFrame(users) 
    get_users()
    # df1 = pd.DataFrame(get_users())               

# Example 2: Fruityvice API //////////////////////////////////

# We will obtain the fruityvice API data using requests.get("url") function. The data is in a json format.
data = requests.get("https://web.archive.org/web/20240929211114/https://fruityvice.com/api/fruit/all")

# We will retrieve results using json.loads() function.
results = json.loads(data.text)

# We will convert our json data into pandas data frame.
pd.DataFrame(results)

# The result is in a nested json format. The 'nutrition' column contains multiple subcolumns, so the data needs to be 'flattened' or normalized.
df2 = pd.json_normalize(results)

# Let's see if we can extract some information from this dataframe. Perhaps, we need to know the family and genus of a cherry.
cherry = df2.loc[df2["name"] == 'Cherry']
(cherry.iloc[0]['family']) , (cherry.iloc[0]['genus'])

# In this Exercise, find out how many calories are contained in a banana.

# Write your code here
cal_banana = df2.loc[df2["name"] == 'banana']
cal_banana.iloc[0]['nutritions.calories']

# Exercise 3 ////////////////////////////////////////

# Using requests.get("url") function, load the data from the URL.
data = requests.get("https://official-joke-api.appspot.com/jokes/ten")

# Retrieve results using json.loads() function.
# Write your code here
result = json.loads(data.text)

# Convert json data into pandas data frame. Drop the type and id columns.

df3 = df2.DataFrame(result)
df3.drop(columns=["type","id"],implace=True)
df3
