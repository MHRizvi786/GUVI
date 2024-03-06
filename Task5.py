#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Write a python program to  calculate the total number of vowels  and count of each individual vowel AEIOU  in the string "Guvi Geeks Network Private Limited"
"""


# In[41]:


str1="Guvi Geeks Network Private Limited"
str1=str1.upper()
a1=0  ##intializing the variables for vowel count.
e1=0
i1=0
o1=0
u1=0
total_cnt=0
for char in str1:
            if char =="A":  ##checking if a character is a vowel or not.
                a1+=1      ##incrementing the count if char is a vowel.
            elif char=="E" :
                e1+=1
            elif char=="I":
                i1+=1
            elif char=="O":
                o1+=1
            elif char=="U":
                u1+=1
total_cnt=a1+e1+i1+o1+u1
print("Total Count",total_cnt)
print("Total Count of A",a1)
print("Total Count of E",e1)
print("Total Count of I",i1)
print("Total Count of O",o1)
print("Total Count of U",u1)


                
            


# In[43]:


#2)Create a pyramid of numbers using  1 to 20 using for loop.

for i in range(1,20): #loop for range(1,20)
    for j in range(i): #loop to print characters in i
        print("* ", end="")
    print()
    


# In[48]:


# 3) Write a program that takes a string as input  and returns a string with all the vowels removed.
s1=input("Enter the string")
s1=list(s1.lower())   ##converting string to lowercase and  to list
vowels="aeiou"
for i in s1:
    if i in vowels:#checking  if a string is vowel or not.
        s1.remove(i)
    
print("New string with all vowels removed","".join(s1))


# In[49]:


#4)Write a program that  takes a string and returns the number of unique characters in it
s2=input("Enter the string")
print("Unique Characters in string","".join(set(s2)))  ##making set of string and joining the characters on "".


# In[54]:


#5) Write a program that takes a string and returns True if it is palindarome.False otherwise.

s3=input("Enter the string")
s5=s3.lower()  ##converting the string to lowercase and storing in another variable.
s4=s3.lower()[::-1]  ##reversing the string 
print(s4)
if s5==s4:  #comparing the 2 strings for palindrome.
    print("Palindrome")
else:
    print("Not Palindrome")


# In[64]:


#6)Write a program that takes 2 strings and returns the longest common substring between them.
s1=input("Enter string1")
s2=input("Enter string2")

from difflib  import SequenceMatcher   ##importing difflib  from SequenceMatcher module from 2 strings

match=SequenceMatcher(None,s1,s2).find_longest_match(0,len(s1),0,len(s2))
print(match)#Match(a=13, b=0, size=4)
print(s1[match.a:match.a+match.size])
print(s2[match.b:match.b+match.size])


# In[8]:


#7) Write a program that takes a string and returns the most  frequent character in it.

s1=input("Enter the string")
cnt=0
dict1={}  ##dictionary to store the element of characters with count
for  ele in s1:
        if ele in  dict1:
            dict1[ele]+=1  ##checking if the dictionary count is more than one for element
        else: 
            dict1[ele]=1  #checking if the dictionary count is  one for element
        if cnt<dict1[ele]:  #comparing the count  variable in with characters count in dictionary and assigning the largest count
            ans=ele
            cnt=dict1[ele]
print("The most frequent character in the string",ans)
            


# In[4]:


#8)Write a program that takes a string and returns True if it is anagram of another string  False otherwise.

def  anagram(str1,str2):   #function to accept 2 strings
    if sorted(str1)==sorted(str2):   #comparing the strings alphabetically.
        return True
    else:
        return False
    


# In[5]:


anagram("silent","listen")


# In[9]:


#9)Write a program that takes a string and returns the number of words in it.
s1=input("Enter a string")
l1=s1.split(" ")  #splitting the string the space
print("Number of words in the string",len(l1))  ##Counting the number of words in the string

    
    


# In[ ]:




