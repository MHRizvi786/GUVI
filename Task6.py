# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


"""
1)You are given a list  L1=[10,501,22,37,100,999,87,351] your task is 2 create 2 lists one which have all the even numbers  and another which have all odd numbers in it.

"""
L1=[10,501,22,37,100,999,87,351]
L2=[i for i in L1 if i%2==0]  ##List comprehension to store all even numbers in new list
L3=[i for i in L1 if i%2!=0]    ##List comprehension to store all odd numbers in new list
print("List with even numbers",L2)
print("List with odd numbers",L3)

"""
2)You are given a list  L1=[10,501,22,37,100,999,87,351] your task is to count all the prime numbers  and create a new python list which contain all the prime numbers.
"""
L1=[10,501,22,37,100,999,87,351]
L_prime=[]  #list to store all prime numbers.
for i in L1:
    flag=0
    num=i
    for i in range(2,i): #loop to check whether number is prime or not
        if  num%i==0:
            flag=1
    if flag==0:
        L_prime.append(num) ##appending the number if it is prime to new list
print("Length of all prime numbers in the list",len(L_prime))
print("Prime number list",L_prime)

"""
3)You are given a list  L1=[10,501,22,37,100,999,87,351].Find out how many numbers are there  in the Python list which are Happy numbers.
"""

L1=[10,501,22,37,100,999,87,351]
L_happy=[]   #list to store the prime numbers.
for ele in L1: #iterating througth elements.
    num=ele
    rev=0
    while(ele!=0):   #loop to reverse the number and square and its digits.
        rem=ele%10
        rev+=rem*rem
        ele=ele//10
        ele
    if rev==1:   #checking if the number is happy number or not.
        L_happy.append(num)
print("Number of happy numbers in the list",len(L_happy))
"""
4) Write a python program to find the sum of first and last digit of an integer.
"""
num1=input("Enter a number")  #input
l1=list(num1)   #converting number to list
sum1=int(l1[0])+ int(l1[-1])  #adding first and last index
print("Sum of first and last digit of number ",sum1)

"""
6) You have been given three lists .Your task is to find the duplicates in the three lists.Write a python program for the same .You can use your own python lists.

"""

L1=[10,22,33,11,8,11,19,10]
L2=[101,201,34,59,101,20,19,34,10,11]
L3=[11,22,98,33,55,11,100,22,22,105,178,20,19]   #initializing the 3 lists
s1=set(L1)  #converting each list to set
s2=set(L2)
s3=set(L3)
set1=s1.intersection(s2) #
set2=set1.intersection(s3)
print("The duplicate element in the 3 lists",set2)
"""
7) Write a python  program to find the first non-repeating elements in a given list of integers?
"""
L1=[10,11,20,10,22,100,20,101,201]
flag=0
dict1={}  #dictionary to store the number of times element occurs in the list
for ele in L1:
    if ele in dict1:  #checking if the element occurs in the list and adding its count.
        dict1[ele]+=1
    else:
        dict1[ele]=1
for ele in dict1.keys():  #loop to print the first non-repeating element in dict
    if dict1[ele]==1:
        print("The first non-repeating element in the list",ele)
        break

"""
8) Write program to find the minimum element in a sorted list.
"""
L1=[100,90,102,19,110,10001]    #defining 2 lists
L2=[500,501,30,90,197,201,677]
L1.extend(L2)  #extending 1 list into another
print("The minium element in th lists",min(L1))   # finding the minimum element in the list



"""
9)You have been given a python list L=[10,20,30,9] and a value of 59.Write  a Python program to find the triplet in the list 
"""
def find_sum1(a, n, sum1):   #function with array ,length ,and sum of triplet as arguments.
    print("Triplets are: ")
    for i in range(0, n - 2):  #loop to get first number in triplet
        for j in range(i + 1, n - 1):    #loop to get second number in triplet
            for k in range(j + 1, n):    #loop to get third number in triplet
                if (a[i] + a[j] + a[k]) == sum1:    #checking if sum of triplet==59
                    print("The Triplets with sum=59 is",a[i], a[j], a[k])


array = [10,20,30,9]
sum1 = 59

find_sum1(array, len(array), sum1)  #calling the triplet function.

"""
10) Given a list  L=[4,2,-3,1,6].Write a python program to find if there is a sublist with sum=zero?
"""
def subArray(arr1, n):  #function takes array and length of array  as input.
    for i in range(n):
        # Starting point of the subarray
        # sum is initialized with the first element of subarray
        sum1 = arr1[i]
        if sum1 == 0:
            return True
        for j in range(i + 1, n):
            # We are finding the sum till the jth index
            # starting from the ith index
            sum1 += arr1[j]
            if sum1 == 0:
                return True
    return False
L1=[4,2,-3,1,6]
x=subArray(L1,len(L1))
print("The sublist with sum=zero in python",x)