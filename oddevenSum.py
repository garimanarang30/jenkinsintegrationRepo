'''

ctr=0
eSum=oSum=0
num = int(input("enter the nth term :  "))
while (ctr < num/2) :
    eSum += 2*ctr
    ctr+=1
ctr =0
if(num %2 ==0):
    while (ctr < num/2):
        oSum += 2*ctr +1
        ctr+=1
else :
    while(ctr < (num+1)/2):
        oSum += 2 * ctr + 1
        ctr += 1

print ("sum of even numbers are ", eSum)
print ("sum of odd numbers are ", oSum)



# TO CHOOSE RANDOM NUMBER  AND CHOOSE WHETHER NUMBER GUESSED IS CORRECT OR NOT
import random
number = random.randint(10,50)
ctr = 0
while(ctr<5):
    guess = int(input("GUESS A NUMBER IN THE RANGE 10 .....50 "))
    if (guess== number):
        print ("You Won !!!!")
        break
    else:
        ctr+=1
    if ctr==5 :
        print ("you loose... Num guessed was : ", number)




# NUMBER IS PRIME OR NOT

num = int(input("ENTER NUM : "))
lim= int(num/2) +1
for i in range(2, lim):
    rem= num% i
    if rem==0:
        print(num , " is not a prime number")
        break
    else:
        print(num , " is a prime number")
        break



# making triangle

for i in range(1, 8):
    for j in range(1, i):
        print("*", end=' ')
    print()
'''
# seraching prime number in range
import self as self

low = int (input("ENTER THE lower RANGE IN WHICH YOU WANT TO FIND NUMBER IS PRIME OR NOT : "))
up =  int (input("ENTER THE upper RANGE IN WHICH YOU WANT TO FIND NUMBER IS PRIME OR NOT : "))
nonprime =[]
primelist=[]
for num in range(low, up):
    for i in range(2, num):
        if (num%i == 0 ):
            nonprime.append(num)
            break
    else:
        primelist.append(num)
print("prime numbers between ", low , " and ", up , " are ")

print(primelist)
print()
print("Non prime numbers between ", low , " and ", up , " are ")

print(nonprime)



















    





