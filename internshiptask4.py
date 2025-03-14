import random
'''
1 for rock
-1 for paper
0 for scissor
'''
computer = random.choice([1,-1,0])
userstr= input("Enter your choice:  ")
userDict = {"r":1,"p":-1,"s":0}
reverseDict = {1:"rock",-1:"paper",0:"scissor"}

user =userDict[userstr]

#By now we have 2 variables,user and computer

print(f"user chose {reverseDict[user]}\ncomputer chose {reverseDict[computer]}")

if(computer == user):
    print("its a tie")

else:
    if(computer==1 and user== -1):
        print("user win!")

    elif(computer==1 and user==0):
        print("user lose!")

    elif(computer==-1 and user==0):
        print("user win!")

    elif(computer==-1 and user==1):
        print("user lose!")

    elif(computer==0 and user==1):
        print("user win!")

    elif(computer==0 and user==-1):
        print("user lose!")

    else:
        print("something went wrong")
        
