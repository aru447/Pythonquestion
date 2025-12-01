#Here’s Level 1: Baby Loops
#1. Print numbers from 1 to 10 using a for loop.
for container in range(1,11):
     newcontainer  = container
    
     startnumber  =  2
     endnumber  =    21

#2. Print all even numbers from 2 to 20.
#But since you already understood the math (start at 2, keep adding 2), the cleaner version is:
for evenvar in range(startnumber,endnumber,2):
    #  if(evenvar%2==0):
        evendata  =  evenvar


#3. Print each character of the string "hello".
string12 =  "hello"
for stringdata in string12:
       Datalatter  = stringdata
       #print(stringdata)

#4. Given a list nums = [3, 6, 2, 8, 5], print each element.
listdata  =  [3, 6, 2, 8, 5]
for listi in listdata:
       newlist  =  listi

#5. Sum all numbers from 1 to 100 using a loop.    
min  =  1
max = 101
Totalsum  =  0
for sumnumber in range(min,max):
     Totalsum  =  Totalsum+sumnumber


#5. multipule all number and then sum from 1 to 100 using a loop. 
start = 1
end = 101
total = 0

for n in range(start, end):
    total = total + (n * (n + 1))

print(total)

