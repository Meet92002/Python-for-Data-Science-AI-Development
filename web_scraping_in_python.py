# Web Scraping - A Key Tool in Data Science

# Introduction

# Web scraping, also known as web harvesting or web data extraction, 
# is a technique used to extract large amounts of data from websites. 
# The data on websites is unstructured, and web scraping enables us to convert it into a structured form.

# BeautifulSoup :-
# BeautifulSoup is a Python library used for web scraping purposes to pull the data out of HTML and XML files.
# It creates a parse tree from page source code that can be used to extract data in a hierarchical and more readable manner.

from bs4 import BeautifulSoup
import requests
URL = "http://www.example.com"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
print(soup)
# Scrapy:-
# Scrapy is an open-source and collaborative web crawling framework for Python. 
# It is used to extract the data from the website

import scrapy 
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['http://quotes.toscrape.com/tag/humor/',]
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {'quote': quote.css('span.text::text').get()}

# Selenium:- 
# Selenium is a tool used for controlling web browsers through programs and automating browser tasks.

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(
    service=Service(GeckoDriverManager().install())
)

driver.get("https://www.example.com")
print(driver.title)

driver.quit()
# Web Scraping Tables using Pandas

# The Pandas library in Python contains a function read_html() 
# that can be used to extract tabular information from any web page. -->

import pandas as pd
import requests
URL = 'https://en.wikipedia.org/wiki/List_of_largest_banks'
headers = {
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(URL, headers=headers)
tables = pd.read_html(response.text)
tables = pd.read_html(URL)
df = tables[0]
print(df)   
print(df.head())

URL = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'
tables = pd.read_html(URL)
df = tables[2] # the required table will have index 2
print(df)

# Beautiful Soup Object
# Tag
# Children, Parents, and Siblings
# HTML Attributes
# Navigable String
# Filter
# find All
# find
# HTML Attributes
# Navigable String
# Downloading And Scraping The Contents Of A Web -->

from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page

# Beautiful Soup Objects ////////////////////////////////////// 
'''
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>
<h3><b id='boldest'>Lebron James</b></h3>
<p> Salary: $ 92,000,000 </p>
<h3> Stephen Curry</h3>
<p> Salary: $85,000, 000 </p>
<h3> Kevin Durant </h3>
<p> Salary: $73,200, 000</p>
</body>
</html>'''

# We can store it as a string in the variable HTML: 
html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"

# To parse a document, pass it into the BeautifulSoup constructor. The BeautifulSoup object represents the document as a nested data structure:
soup = BeautifulSoup(html, 'html.parser')

# We can use the method prettify() to display the HTML in the nested structure:
print(soup.prettify())

# Tags ///////////////////////////////////
# Let's say we want the title of the page and the name of the top paid player. We can use the Tag. 
# The Tag object corresponds to an HTML tag in the original document, for example, the tag title.
tag_object=soup.title
print("tag object:",tag_object)

# we can see the tag type bs4.element.Tag 
print("tag object type:",type(tag_object))

# If there is more than one Tag with the same name, the first element with that Tag name is called. 
# This corresponds to the most paid player: 
tag_object=soup.h3
tag_object

# Children, Parents, and Siblings ///////////////////

# As stated above, the Tag object is a tree of objects. 
# We can access the child of the tag or navigate down the branch as follows: 

tag_child =tag_object.b
tag_child

# You can access the parent with the  parent 
parent_tag=tag_child.parent
parent_tag

tag_object

# tag_object parent is the body element.
tag_object.parent

# tag_object sibling is the paragraph element 
sibling_1=tag_object.next_sibling
sibling_1

# sibling_2 is the header element, which is also a sibling of both sibling_1 and tag_object 
sibling_2=sibling_1.next_sibling
sibling_2

#Exercise: next_sibling 

sibling_2.next_sibling                              

# HTML Attributes //////////////////////////////

tag_child['id']

# You can access that dictionary directly as attrs:

tag_child.attrs

# We can also obtain the content of the attribute of the tag using the Python get() method.
tag_child.get('id')

# Navigable String/////////////////////////////////////////
tag_string=tag_child.string
tag_string

# we can verify the type is Navigable String/////////////////////////////
type(tag_string)

# A NavigableString is similar to a Python string or Unicode string.
# To be more precise, the main difference is that it also supports some BeautifulSoup features. 
# We can convert it to string object in Python:
unicode_string = str(tag_string)
unicode_string

# Filter ////////////////////////////////

'''<table>
  <tr>
    <td id='flight' >Flight No</td>
    <td>Launch site</td> 
    <td>Payload mass</td>
   </tr>
  <tr> 
    <td>1</td>
    <td><a href='https://en.wikipedia.org/wiki/Florida'>Florida</a></td>
    <td>300 kg</td>
  </tr>
  <tr>
    <td>2</td>
    <td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td>
    <td>94 kg</td>
  </tr>
  <tr>
    <td>3</td>
    <td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td>
    <td>80 kg</td>
  </tr>
</table>'''

# We can store it as a string in the variable table:

table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"
table_bs = BeautifulSoup(table, 'html.parser')

# find All /////////////////////////////////

# When we set the name parameter to a tag name, the method will extract all the tags with that name and its children.
table_rows=table_bs.find_all('tr')
table_rows

# The result is a Python Iterable just like a list, each element is a tag object:
first_row =table_rows[0]
first_row

# The type is tag
print(type(first_row))

# we can obtain the child
first_row.td

# If we iterate through the list, each element corresponds to a row in the table:
for i,row in enumerate(table_rows):
    print("row",i,"is",row)

for i,row in enumerate(table_rows):
    print("row",i)
    cells=row.find_all('td')
    for j,cell in enumerate(cells):
        print('colunm',j,"cell",cell)

# If we use a list we can match against any item in that list.

list_input=table_bs .find_all(name=["tr", "td"])
list_input

# Attributes //////////////////////////////////////////

# If the argument is not recognized it will be turned into a filter on the tag’s attributes. 
# For example with the id argument, Beautiful Soup will filter against each tag’s id attribute. 
# For example, the first td elements have a value of id of flight, therefore we can filter based on that id value.

table_bs.find_all(id="flight")

# We can find all the elements that have links to the Florida Wikipedia page:
list_input=table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida")
list_input

# If we set the href attribute to True, regardless of what the value is, the code finds all tags with href value:
table_bs.find_all(href=True)
