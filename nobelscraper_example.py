# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup as bs
import csv

r = requests.get('https://www.nobelprize.org/nobel_prizes/lists/all/') #connect to the website
soup = bs(r.content,'html.parser') #create a html parser and parse the content on the page r from above
print(soup.prettify()) #Print what the parser has opened for debugging
#print(soup) #print without prettify(no indentation and such)

data = soup.findAll("h2") #find all h2 tags
print(data)
for i, d in enumerate(data):  #loop through all the h2 tags
  d = str(d)
  data[i] = d[4:8] # get the data while ignoring the <h2> and ,/h2>
print(data)

data = soup.findAll("div", {"class": "by_year"}) # finds all of the div classes that have a by year class
print(data[0])

p = data[0].findAll('p')  #Search for p tags within the first element of data. Keep in mind data has multiple indices.
print(p)

output = []
for p_element in p:               #loops through each of the individual p tags within the first index of data
  work = p_element.text           #extracts text each p tag
  #print(work)
  start_work = work.find('“') + 1     # find the “ within a string. Notice how I had to copy this directly from the printed html data
  work = work[start_work :-1]       #index
  #print(work)
  try:
    a = p_element.findAll('a')
    for a_element in a:           #loops through the a elements witihin each p tag. If no a tag exist the try except will pass it
      #print(a_element)
      s = str(a_element)          #converts a_element to string
      
      w1 = s.find('prizes/')      #finds index of prizes/ in a_element string
      w2 = s.find('/20')          #finds index of /20 in a_element string
      
      name = a_element.text       #extracts elements that are text in within the a tag 
      field = s[w1+7:w2]          #slice the string to return just the field
      year = s[w2+1:w2+5]         #slice the string to return just the field
      print(year,field,name,work)
      output.append([[year], [field], [name], [work]])

  except: 
    continue
    
print(output)













"""
Created on Thu Jan 13 09:49:23 2022

@author: Alex
"""

