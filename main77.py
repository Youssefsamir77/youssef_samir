# task 1
num= float(input("please enter a number "))
if num >=0 :
    print(num)
else:
    print(num*-1)
# task 2
x= int(input("please enter the year "))
if x%4==0 :
    print("this year is a leap year")
else:
    print("this is not a leap year")
# task 3
p1=int(input("please enter your age "))
p2=int(input("please enter your age "))
p3=int(input("please enter your age "))
if p1>p2 and p1>p3:
    print("person 1 is the oldest")
    if p2>p3 :
        print("person 3 is the youngest")
    else:
        print("person 2 is the youngest")

elif p2>p1 and p2>p3 :
       print("person 2 is the oldest")
       if p1>p3:
           print("person 3 is the youngest")
       else:
           print("person 1 is the youngest")
elif p3>p1 and p3>p2 :
    print("person 3 is the oldest")
    if p1>p2 :
          print("person 2 is the youngest")
    else:
        print("person 1 is the youngest")
# task 4
sum=0
for n in range (1,1000):
    x=int(input("please enter a num"))
    if x<0:
        break
    sum=sum+x
print("the sum of all postive numbers is =",sum)

# task 5
username=input("please enter your name")
age=int(input("please enter your age"))
if age >= 18 :
    print(username,"you are eligible to vote")
else:
    print(username," you are not eligible to vote")
#task 6
b=int(input("please enter a number"))
factorial=1
if b <0 :
    print(" factorial is not available")
elif b==0:
    print("the factorial is 1")
else:
    for n in range (1,b+1):
        factorial=factorial*n
    print("the factorial is",factorial)













