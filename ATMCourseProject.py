
## Program: ATM Project 
## Language: Python 3.9.7
##
## Description: This program will be a functional ATM
##
## College: Husson University
## Course: IT 261
## Author: Kaleb Currier
## 
## Change Log:
##

print('Welcome to IdleBank!')

#userName =

pinAttempts = 3

userPin = 1234

pinCheck = int(input('Please Enter Your PIN: '))

atmFunctions = input('Deposit or Withdraw? (d/w): ').upper()

withdraw = float(input('How much would you like to Withdraw?: '))

deposit = float(input('How much would you like to Deposit?: '))

while pinAttempts != 0:
    pinCheck
    if pinCheck != userPin:
        pinAttempts -= 1
        print('Authentication Failed you have, ', pinAttempts, 'left. PLEASE ENTER THE CORRECT PIN')
    else:
        atmFunctions



    if atmFunctions == 'd':
        deposit, print('You have deposited: ', deposit)
    
    elif atmFunctions == 'w':
        withdraw, print('You have withdrew: ', withdraw)
    
    




#savings1 =

#savings2 =

#checking1 =

#limitTotal =

#limitSingle =

#endBal =

#balInfo =

