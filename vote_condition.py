# This is a python program to chech a citizen's eligibility to vote

#Prompting a user to enter his/her age
age = int(input('enter your age \n'))

#An if else statement to check whether the user is eligible to vote based on age
if(age>=18):
    print('You are eligible to vote')
else:
    print('You are not eligible to vote')