# Strip() method to remove white spaces
from unicodedata import name


text= input("Type Something ")
print(text.strip()) 

#len() To Calculate Length Of String
fruits= 'oranges'
print(len(fruits))

# Lower() method to Convert To LowerCase
name="SHIVAM"
print(name.lower())

# Upper() method to Convert To LowerCase
name='durani'
print(name.upper())

# Split() method to split Words
tech='python java cpplus'
print(tech.split())

# Splice Operator In Python
veg= ['potato','paneer','raddish']
print(veg[1:])
veg[1:2]='tomato'
print(veg)