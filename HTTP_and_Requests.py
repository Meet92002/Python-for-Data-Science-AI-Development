# Overview of HTTP
# Uniform Resource Locator:URL
# Requests in Python
# Get Request with URL Parameters
# Post Requests

# Overview of HTTP ////////////////////////////////

# When you, the client, access a web page your browser sends an HTTP request to the web server that hosts the page. 
# If no specific file is mentioned in the URL, the server typically looks for a default file, such as "index.html". 
# If your request is successful, the server will send the object to the client in an HTTP response. 
# This includes information like the type of the resource, the length of the resource, and other information.

# Uniform Resource Locator:URL ///////////////////////////////

# Uniform resource locator (URL) is the most popular way to find resources on the web. We can break the URL into three parts.

# Scheme:- This is this protocol, for this lab it will always be http://
# Internet address or Base URL :- This will be used to find the location here are some examples: www.ibm.com and  www.gitlab.com 
# Route:- Location on the web server for example: /images/IDSNlogo.png

# Requests in Python ////////////////////////////////////

import requests
import os 
from PIL import Image
from IPython.display import IFrame

# You can make a GET request via the method get to www.ibm.com:

url='https://www.ibm.com/'
r=requests.get(url)

r.status_code
print(r.request.headers)
print("request body:", r.request.body)
header=r.headers
print(r.headers)
header['Date']
header['Content-Type']
r.encoding
r.text[0:100]
# Use single quotation marks for defining string
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'
r=requests.get(url)
print(r.headers)
r.headers['Content-Type']
# An image is a response object that contains the image as a bytes-like object. 
# As a result, we must save it using a file object. 
# First, we specify the file path and name
path=os.path.join(os.getcwd(),'image.png')

with open(path,'wb') as f:
    f.write(r.content)

Image.open(path)

# Exercise:-

url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'
path=os.path.join(os.getcwd(),'example1.txt') 
r=requests.get(url)
with open(path,'wb') as f:
    f.write(r.content)

# Get Request with URL Parameters //////////////////////

url_get='http://httpbin.org/get'

# To create a Query string, add a dictionary
payload={"name":"Joseph","ID":"123"}

# Then passing the dictionary payload to the params parameter of the  get() function:
r=requests.get(url_get,params=payload)
r.url

print("request body:", r.request.body)
print(r.status_code)
print(r.text)
r.headers['Content-Type']
r.json()
r.json()['args']

# Post Requests ///////////////////////////////

url_post='http://httpbin.org/post'
r_post=requests.post(url_post,data=payload)

#print("POST request URL:",response.url )
#print("GET request URL:",r.url)
print("POST request URL:", r_post.url) # Use r_post instead of response

# We can compare the POST and GET request body, we see only the POST request has a body:
print("POST request body:",r_post.request.body)
print("GET request body:",r.request.body)

r_post.json()['form']
