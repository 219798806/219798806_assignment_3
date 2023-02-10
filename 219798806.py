##Student name: Msimango TS
##Student no: 219798806
##Date: 11 Feb 2023
##Assignment 3: Python

##Problem 1

s = 'fullstackslp'
print(s[0])
print(s[11])
print(s[4:9])
print(s[9:13])
print(s[7:10])
print(s[::-1])

##Problem 2

d1 = {'simple_key':'hello'}
print(d1['simple_key'])

d2 = {'k1':{'k2':'hello'}}
print(d2['k1']['k2'])

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])

##Problem 3

mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
uniq_values = set(mylist)
print(uniq_values)

##Problem 4

age = 45
name = "Kyle"
print("Hello my dog's name is {} and he looks {} years old".format(name, age))
