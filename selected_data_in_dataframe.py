# let us import the Pandas Library
import pandas as pd

#Define a dictionary 'x'

x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}

#casting the dictionary to a DataFrame
df = pd.DataFrame(x)

#display the result df
df

# Coloumm Selection: /////////////////////////

#Retrieving the "ID" column and assigning it to a variable x
x = df[['ID']]
x

#check the type of x
type(x)

# Access to multiple columms /////////////////////////

#Retrieving the Department, Salary and ID columns and assigning it to a variable z

z = df[['Department','Salary','ID']]
z

# loc() and iloc() functions: /////////////////////////

# Access the value on the first row and the first column

df.iloc[0, 0]

# Access the value on the first row and the third column

df.iloc[0,2]

# Access the column using the name

df.loc[0, 'Salary']

# Let us create a new dataframe called 'df2' and assign 'df' to it.
# Now, let us set the "Name" column as an index column using the method set_index().

df2=df
df2=df2.set_index("Name")

#To display the first 5 rows of new dataframe
df2.head()

#Now, let us access the column using the name
df2.loc['Jane', 'Salary']

# Slicing DataFrames: /////////////////////////

# let us do the slicing using old dataframe df

df.iloc[0:2, 0:3]

#let us do the slicing using loc() function on old dataframe df where index column is having labels as 0,1,2
df.loc[0:2,'ID':'Department']

#let us do the slicing using loc() function on new dataframe df2 where index column is Name having labels: Rose, John and Jane
df2.loc['Rose':'Jane', 'ID':'Department']