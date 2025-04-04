# 1
x=int(input("please enter the first number"))
y=int(input("please enter the second number"))
print("the sum of the two numbers is",x+y)
# 2
num=int(input("please enter a number"))
if num%2 ==0 :
    print(num,"is an even number")
else:
    print(num,"is an odd number")
# 3
for i in range(1,21) :
    if i%2==0:
        print(i)
# 4
s = input(" enter a word")
vowels = "aeiou"
count = sum(1 for char in s if char in vowels)
print("the number of the vowels in the word is",count)
#5
l=[1,2,3,4,5,6,7,8,9,10]
index=0
for i in range (10):
    print(l[index]**2)
    index=index+1
#6
student_name=input("please enter your name")
name= student_name
subject_num=int(input("please enter the amount of subjects you have"))
while True:
    print("note if you finish type finish")
    subject_name=input("please enter your subject")
    subject=subject_name
    if subject_name=="finish":
            break
scores_1=0
while True:
    print("note if you finish type 0000")
    scores = int(input("please enter your scores"))
    scores_1=scores_1+scores
    if scores == 0000:
        break
average_grade= scores_1/subject_num
if average_grade >70:
    print("congrats")
else:
    print("sorry")

#7
list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]

common_elements = list(set(list_a) & set(list_b))
print(common_elements)
#8
list1=[1,2,3,4,5]
list1.remove(2)
print(list1)
#9
print(" 5*2*3*4=120 so the answer will be ",end= " ")
num1=5
num2=2
num3=3
num4=4
sum=num1*num2*num3*num4
sum=str(sum)
(list(sum))
print(list(sum)[1],list(sum)[2])
#10
X = int(input("Enter a number: "))

if X > 1:
    for i in range(2, int(X**0.5) + 1):
        if X % i == 0:
            print(f"{X} is not a prime number.")
            break
    else:
        print(f"{X} is a prime number.")
else:
    print(f"{X} is not a prime number.")
#11
l=[1,5,8,7,9,10,12,15]
type=int(input("please enter a number"))
if type in l :
    print(type,"and its index is ",l.index(type))
else :
    print ("not found")
#12
list_4=[2,2,4,6,7,8,9,2,33,53,21]
count_min=list_4.count(min(list_4))         # if we increase the list by another 2 and run again the output will be unlucky
if count_min%2!=0:
    print("the array is lucky")
else:
    print("unlucky array")
#13
list_3=[15,7,3,8,6]
print("the min no is",min(list_3))
print("the max no is",max(list_3))
list_3[0],list_3[2]= min(list_3),max(list_3)
print(list_3)
#14
list_5=[8,2,3,2,6,2,5]
print(min(list_5),"its index is ",list_5.index(min(list_5)))
#15
list_6=[29,1,66,32,5,8]
print(sorted(list_6))
#16
s="h e l l o"
o=s.split(" ")
print("".join(o))
#17
list_6=[3,4,17,6,22,13,7]
list_6[0],list_6[-1]=list_6[-1],list_6[0]
print(list_6)
# last task
num_one = int(input("Enter first number: "))
num_two = int(input("Enter second number: "))

while num_two:
    num_one, num_two = num_two, num_one % num_two
print(f"The HCF is {num_one}.")














