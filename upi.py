pin=int(0000);#pin number
myname='rajesh' #user name
user_name=input("Enter your name :")
user_pin=int(input("Enter Your pin :"));
balance=int(10000);
if pin==user_pin and myname==user_name: #validation
    print('')
    #print("Welocome",user_name)
    option=int(input(" 1.Balance 2.Send :"));#option selection
    if option==2:
        print('')
        rec=input("Enter Number:")
        num_len=len(rec)
        if num_len==10:
            
             amount=int(input("Enter Amount to Send :"))
             if amount>balance:
                 print('-----------------------------------------')
                 print('Insuficient of Balance ')
                 print('-----------------------------------------')
    
             elif amount==0:
                print('-----------------------------------------')
                print("Amount Must Be Greater Than zero")
                print('-----------------------------------------')

             elif amount<=0:
                 
                 print('-----------------------------------------')
                 print(' Negative Amount Not Valid ')
                 print('-----------------------------------------')
             pin_val=int(input("enter your pin:"))
             if pin_val==pin: #validation
                 
                remaing_bal=balance-amount
                print('----------------------------------------------')
                print("Your Amount Debited of",amount,'sucessfully')
                print('----------------------------------------------')
                print('')
                print('Your Remaing is balance:',remaing_bal)
        else:
            print('-------------------')
            print("Invalid Number Entered")
            print('--------------------')
    elif option==1:
        print('----------------------------')
        print("Your balance is:",balance)
        print('-----------------------------') 
    else:
        print('------------------------------')
        print("Invalid Option Entered")
        print('------------------------------')
else:
    print('-------------------------')
    print("invalid pin entered")
    print('-------------------------')
print("Thank You")
print("Made By ❤️Rajesh Korlapati")
