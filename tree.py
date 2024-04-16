print("welcome to the atm")

balance = 70

lt = 0



def deposit(amount):

  global balance

  global lt

  global lt2

  global lt1

  global statement1

  global statement2

  if(amount > 0):

      balance = balance + amount

      lt1 = amount

      statement1 = lt + lt1

      


deposit(50)
print("balance deposit total",balance)
print("balance deposit afterwards",lt1)
print(" statement of deposit Lt",statement1)

print ("welcome to withdraw")

def withdraw(amount):

  global balance

  global lt

  global lt2

  global statement2

  if(balance >= amount):

      balance = balance - amount

      lt2 = -amount

      statement2 =lt2 -  lt


        
withdraw(40)
print("balance withdraw total",balance)
print("balance withdraw afterwards",lt2)
print(" statement of withdraw Lt",statement2)


def transfer(sender_account,recipient_account,amount):
    global statement3
    global totalbalance 

    
    
    
    
    

    if sender_account['balance'] >=amount:
        recipient_account['balance']-=amount
        
        
        print("transfer succesfully")
    else:
        print("insufficient balance")

   
     
sender = {'account_number':'1234','balance':1000}
recipient = {'account_number':'5678','balance':900}

transfer(sender,recipient,200)  
print("sender balance",sender['balance']) 
print("recipient balance",recipient['balance']) 

hdfc = {'account_number':'2356','balance':12000}
icic = {'account_number':'3457','balance':3000}

def transcition(hdfc_acc,icic_acc,amount):
     
     
     

     if hdfc_acc['balance'] >=amount:
        icic_acc['balance']=amount
        
        
        
        print("transfer succesfully to icic bank")
     else:
          print("insufficient balance")

    
print("sender balance",hdfc['balance']) 
print("recipient balance",icic['balance']) 


hdfc = {'account_number':'2356','balance':22000}
sbi = {'account_number':'8970','balance':33000}


def export(hdfc_acc,sbi_acc,amount):

   if hdfc_acc['balance'] >=amount:
        sbi_acc['balance']=amount
        
        
        
        print("transfer succesfully to icic bank")
   else:
          print("insufficient balance")


print("sender balance",hdfc['balance']) 
print("recipient balance",sbi['balance']) 

hdfc = {'account_number':'2356','balance':2500}
bob = {'account_number':'1979','balance':3000}

def export(hdfc_acc,bob_acc,amount):

   if hdfc_acc['balance'] >=amount:
        bob_acc['balance']=amount
        
        
        
        print("transfer succesfully to icic bank")
   else:
          print("insufficient balance")


print("sender balance",hdfc['balance']) 
print("recipient balance",bob['balance']) 

    
print("welcome to piggybank")
print("Type d to Deposit")
print("Type w to Withdraw")
print("Type q to quit")
print("Type a for account transfer")
print("type b for bank transfer to another bank")
print("type c for bank transfer to another bank sbi")
print("type e for bank transfer to another bank to bob")
print("type m for the menu")

action = input("action> ").lower()
if(action == "d"):

    

        amount = int(input("deposit> "))

        deposit(amount)

        print("balance deposit total",balance)
        print("balance deposit afterwards",lt1)
        print(" statement of deposit Lt",statement1)

elif(action == "w"):

        amount = int(input("withdraw> "))

        withdraw(amount)

        print("balance withdraw total",balance)
        print("balance withdraw afterwards",lt2)
        print(" statement of withdraw Lt",statement2) 

elif(action == "a") :

     amount = int(input("transfer> "))

     
     
     print("sender balance",sender['balance']) 
     print("recipient balance",recipient['balance']) 

elif(action == "b") :

     amount = int(input("transfer to another bank> "))

     
     
     print("sender balance from hdfc bank",hdfc['balance']) 
     print("recipient balance from icic bank",icic['balance']) 

elif(action == "c") :

     amount = int(input("transfer to another bank name sbi> "))

     
     
     print("sender balance from hdfc bank",hdfc['balance']) 
     print("recipient balance from icic bank",sbi['balance']) 

elif(action == "e") :

     amount = int(input("transfer to another bank name bob> "))

     
     
     print("sender balance from hdfc bank",hdfc['balance']) 
     print("recipient balance from icic bank",bob['balance']) 

elif(action == "m"):
     
     

      print("welcome to piggybank")
      print("Type d to Deposit")
      print("Type w to Withdraw")
      print("Type q to quit")
      print("Type a for account transfer")
      print("type b for bank transfer to another bank")
      print("type c for bank transfer to another bank sbi")
      print("type e for bank transfer to another bank to bob")
      
      action = input("action> ").lower()




while(action != "q"):

  print("Please Enter A Correct Command")
  action = input("action> ").lower()

else:

   print("Thank you for using PiggyBank...")

print ("thanks visit again")





     




     

     









