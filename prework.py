#1. Print username
def hello_name(user_name):
    print("\nhello_" + user_name)

#Driver code
hello_name("AnuTri")


#2. Print first 100 odd numbers
print("\nFirst 100 odd numbers:")
for num in range(1,101):
   if(num%2 != 0):
       print(num, end=" ")


#3. Return max number of the list
def max_num_in_list(a_list):
   print("\n\nList of numbers:") 
   print(*a_list)

   maxnum = 0;
   for num in a_list:
       if(num > maxnum):
           maxnum = num
   return maxnum

#Driver code
print("Max num is:" + str(max_num_in_list([10,230,50,100,30])))


#4. Check for a leap year
def is_leap_year(a_year):
    a_year = int(a_year)
    isleap = False

    if a_year % 400 == 0:
        isleap = True
    elif a_year % 100 == 0:
        isleap = False
    elif a_year % 4 == 0:
        isleap = True
    
    return isleap

year = input("\nPlease enter a year: ")

#Driver code
if(is_leap_year(year)):
    print("The year " + year + " is a leap year")
else:
    print("The year " + year + " is not a leap year")


#5. Check for consecutive numbers in a list
def is_consecutive(a_list):
    is_consec = False
    
    print("\nList of numbers:")
    print(*a_list)

    for i in range(len(a_list)-1):
        if (a_list[i+1] - a_list[i]) == 1:
            is_consec = True
        else:
            is_consec = False
            break
    
    return is_consec

#Driver code
if(is_consecutive([1,2,3,4,5])):
    print("Numbers are consecutive\n")
else:
    print("Numbers are not consecutive\n")


 