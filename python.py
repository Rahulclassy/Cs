#PRACTICAL-1

a,b,c= eval(input("enter value separated by commas : "))

d = b * 2 - 4 * a *c
r1 = (-b + (d) * 0.5) / 2 * a
r2 = (-b - (d) ** 0.5) / 2 * a
if d >=0:
    print("roots are real " ,r1 ,r2)
else:
    print("roots are not real")

#PRACTICAL-2
(a)
n = eval(input("enter value :"))
if n>1:
  for i in range(2,n):
      if n % i == 0:
        print(n,"is not a prime number ")
        break
  else:
          print(n,"is a prime number")
          
else:
        print(n,"is not a prime number ")

(b)
n = eval(input("enter value "))
for num in range(1,n):
    if num > 1:
        for i in range (2,num):
           if num % i ==  0:
            break
        else:
            print(num,end =',')
(c)
n = eval(input("enter value "))
count = 0
number = 2
while count < n:
    for i in range(2,number):
        if number % i == 0:
         number += 1
         break
    else:
        print(number,end=',')
        count += 1
        number += 1

#PRACTICAL-3

n = int(input("enter the no of rows :"))
for i in range(n):
 for j in range(n-i-1):
     print(" ",end = " ")
 for j in range(2*i+1):
     print("*",end =" ")
 print()
for i in range (n):
 for j in range (i+1):
     print(" ",end = " ")
 for j in range(2*n-2*i-3):
     print("*",end =" ")
print()

#PRACTICAL-4

character = input("enter data ")
if character >='A' and character<='Z':
 print("uppercase letter")
elif character >='a' and character<='z':
 print("lowercase letter")
elif character >='0' and character<='9':
 print("numeric digit")
 n = int(character)
 dict ={0:'zero',1:'first',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
 print(dict[n])
else:
 print("special character")

#PRACTICAL-5

(a)
string = "hello welcome to python"
character = input("enter a character :")
f = 0
for i in string:
 if i == character:
  f += 1
print("frequency of",character,'is',f)

(b)
string = "hello welcome to python"
print(string.replace("h","t"))

(c)
string = "hello welcome to python"
print(string[1:len(string)])

(d)

string = "hello welcome to python"
print(string[:0])

#PRACTICAL-6
str1 = input("enter first string: ")
str2 = input("enter second string: ")
n1 = int(input("enter no of character which is to be swap: "))
n = str1[ :n1]
m = str2[ :n1]
if n1 <= min(len(str1),len(str2)):
 print(str1.replace(n,m))
else:
 print(str2.replace(m,n))

#PRACTICAL-7

def occurances(a,b):
 newlist =[]
 if b not in a:
     print(-1)
 else:
     i= 0
     while i< len(a):
        c=a.find(b,i)
        if c== -1:
            break
        i= c+ len(b)
        newlist.append(c)
     print(newlist)
a= input("enter first string ;")
b= input("enter second string ;")
occurances(a,b)

# PRACTICAL 8
# WAP to create a list of the cubes of only the even integers appearing in the input list 
#(may have elements of other types also) using the following: 
#(a). 'for' loop 
#(b).  list comprehension

def cubes():
 newlist= []
 number = [1,2,3,4,5,6,"seven"]
 for i in number:
     if type(i)== int:
         if i % 2 == 0:
             newlist.append(i**3)
         print(newlist)
cubes()
# PRACTICAL-9

#PRACTICAL-10



# PRACTICAL-11
#write a function that prints a dictionary where the keys are numbers
#between 1 and 5 and the values are cubes of the keys.

def cubes():
 dict={}
 for i in range (1,6):
    dict[i]=i**3
 print(dict)
cubes()

# PRACTICAL-12
#) Consider a tuple t1=(1,2,5,7,9,2,4,6,8,10).WAP to perform following
#oprations:
#(a.)Print half the values of the tuple in one line and other half in the other next
#line.
#(b.)Print another tuple whose values are even numbers in the given tuple.
#(c.)concatenate a tuple t2 = (11,13,15) with t1.
#(d.)Return maximmum and minimum value from this given tuple.

#(a)
t1 = (1,2,5,7,9,2,4,6,8,10)
half_value=len(t1)//2
first_half = t1[ :half_value]
print("first_half",first_half)
second_half = t1[half_value: ]
print("second_half",second_half)

#(b)
t1 = (1,2,5,7,9,2,4,6,8,10)
even_number= tuple(filter(lambda x: x%2==0,t1))
print("tuple with even number",even_number)

#(c)
t1 = (1,2,5,7,9,2,4,6,8,10)
t2 = (11,13,15)
concatenation= (t1 + t2)
print("tuple with concatenation ", concatenation)

#(d)
t1= (1, 2, 5, 7, 9, 2, 4, 6, 8, 10, 11, 13, 15)
print("maximum value in t1 is ",max(t1))
print("minimum value in t1 is ",min(t1))

# PRACTICAL -13
#Wap to accept a name from a user. Raise and handle appropriate
#exception(s) if the text entered by the user contains digits and/or special
#characters.

name = input("enter a name ")
try:
 if name.isalpha():
     print("This is correct Name")
 else:
    raise Exception(" There is NameError")
except Exception as e:
 print(e)



          
