# About the Dataset
# Introduction of Pandas
# Viewing Data and Accessing Data
# Quiz on DataFrame

# Import required library

import pandas as pd

# Read data from CSV file

# csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/LXjSAttmoxJfEG6il1Bqfw/Product-sales.csv'
# df = pd.read_csv(csv_path)

from pyodide.http import pyfetch # type: ignore
import pandas as pd

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/LXjSAttmoxJfEG6il1Bqfw/Product-sales.csv"

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())
async def main():
    await download(filename, "Product-sales.csv")
    df = pd.read_csv("Product-sales.csv")
    
    # Read data from Excel File and print the first five rows
    xlsx_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/n9LOuKI9SlUa1b5zkaCMeg/Product-sales.xlsx'
    await download(xlsx_path, "Product-sales.xlsx")
    df_xlsx = pd.read_excel("Product-sales.xlsx")
    return df, df_xlsx

df, df_xlsx = __import__('asyncio').run(main())

# We can use the method head() to examine the first five rows of a dataframe:
# Print first five rows of the dataframe

df.head()

# Read data from Excel File and print the first five rows

df_xlsx
df_xlsx.head()

# Access to the column Length

x = df[['Quantity']]
x
# Get the column as a series

x = df['Product']
x

# Access to multiple columns

y = df[['Product','Category', 'Quantity']]
y


