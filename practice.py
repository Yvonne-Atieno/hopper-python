#Write a Python program that takes a list of numbers as input and outputs the median of the numbers 
digits =  [2,4,6,8,10,12,14]
median  = statistics.median(digits)
print(median)    

#Write a Python program that takes a list of numbers as input and outputs the second largest number in the list using conditional statements and a for loop.


#Write a Python program that takes a year as input and determines if it is a leap year.
year= int(input("Enter year"))
if(year%4==0):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")  
    year=[2000,2003,2004,2010]  



#Write a Python program that takes a string as input and checks if it is a palindrome (reads the same forwards and backwards), ignoring spaces and punctuation.
string=("yvonne","emma","cathy")
if(string==[]):
    print("The string is a palindrome")
else:
    print("Not a palindrome")   
