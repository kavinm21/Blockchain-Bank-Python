import hashlib as h
import time
import os
accounts={}
class Block:
    def __init__(self,amt,acc,bal=0):
        self.account=acc
        self.amount=amt
        self.hash="\0"
        self.balance=bal
        self.next=None
    def hashify(self,string):
        res=h.sha256(string.encode())
        self.hash=res.hexdigest()
    def printblock(self):
        if self.account==0:
            if self.amount>=0:
                print("Account credited with Rs.%d\t Balance: Rs.%d"%(self.amount,self.balance))
            else:
                print("Account debited with Rs.%d\t Balance: Rs.%d"%(self.amount*-1,self.balance))
        else:
            if self.amount<0:
                print("Amount of Rs.%d transferred to Account Number %d\t Balance: Rs.%d"%(self.amount*-1,self.account,self.balance))
            else:
                print("Amount of Rs.%d received from Account Number %d\t Balance: Rs.%d"%(self.amount,self.account,self.balance))
class Block_Chain:
   def __init__(self):
       self.head=None
   def add_block(self,amt,acc=0):
       newblock=Block(amt,acc)
       if self.head is None:
           newblock.hashify("Null value")
           newblock.balance=newblock.balance+newblock.amount
           self.head=newblock
       else:
            temp=self.head
            while (temp.next):
                temp=temp.next
            newblock.balance=temp.balance+newblock.amount
            newblock.hashify(str(temp))
            temp.next=newblock
   def view_chain(self):
       temp=self.head
       while (temp):
           temp.printblock()
           temp=temp.next
   def returnBalance(self):
       temp=self.head
       if temp==None:
           return 0
       if temp.next==None:
           return temp.balance
       while (temp.next):
           temp=temp.next
       return temp.balance
def intro():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n \t\t\t\t\t Account Ledger Using Blockchain \n")
    print(" \t\t\t\t\t\t\t\t By ")
    print(" \t\t\t\t\t\t\t\t    Kavin M- 19PD18")
    print(" \t\t\t\t\t\t\t\t    Sai Karthik R- 19PD28")
    time.sleep(5)
    os.system('cls')
def newaccount():
    os.system('cls')
    print("Enter account number: ",end='')
    key=int(input())
    if key in accounts.keys():
        print("Account Number already in use")
        return
    print("Enter new password: ",end='')
    password=input()
    accounts[key]=[password]
    transactions=Block_Chain()
    accounts[key].append(transactions)
    os.system('cls')
def add_transaction():
    os.system('cls')
    print("Enter account number: ",end='')
    acc=int(input())
    print("Enter password: ",end='')
    passw=input()
    if acc in accounts.keys():
        if accounts[acc][0]==passw:
            print("\t\tEnter w for withdrawal\n\t\tEnter t for transfer\n\t\tEnter d for deposit")
            ch=input()
            print("Enter amount in transaction: ",end='')
            amt=int(input())
            if ch!='w' and ch!='W' and ch!='t' and ch!='T' and ch!='d' and ch!='D':
                print("Invalid Input\n\t\tPress any key to return to menu")
                input()
                os.system('cls')
            if ch=='w' or ch=='W':
                if amt>accounts[acc][1].returnBalance():
                    print("Insufficient Balance\n\t\tPress any key to return to menu")
                    input()
                    os.system('cls')
                    return
                else:
                    print("Withdrawal Successfull\n\t\tPress any key to return to menu")
                    input()
                    os.system('cls')
                amt=amt*-1
            acc1=0
            if ch=='t' or ch=='T':
                if amt>accounts[acc][1].returnBalance():
                    print("Insufficient Balance\n]\t\tPress any key to return to menu")
                    input()
                    os.system('cls')
                    return
                else:
                    print("Transfer Successfull\n\t\tPress any key to return to menu")
                    input()
                    os.system('cls')
                print("Enter the other account number: ",end='')
                acc1=int(input())
                amt=amt*-1
                if acc1 in accounts.keys():
                    accounts[acc1][1].add_block(amt*-1,acc)
                else:
                    print("Account does not exist")
                    return 
            if accounts[acc][1] is None:
                accounts[acc][1]=Block_Chain()
            if ch=='d' or ch=='D':
                print("Deposit Successfull\n\t\tPress any key to return to menu")
                input()
                os.system('cls')
            accounts[acc][1].add_block(amt,acc1)
        else:
            print("Password Incorrect")
    else:
        print("Invalid Account")
    os.system('cls')
def view_transaction():
    os.system('cls')
    print("Enter account number: ",end='')
    acc=int(input())
    print("Enter password: ",end='')
    passw=input()
    if acc in accounts.keys():
        if accounts[acc][0]==passw: 
            print("Transaction Details")
            accounts[acc][1].view_chain()
        else:
            print("Password Incorrect")
    else:
        print("Invalid Account")
    print("\n\n\t\t\tPress any key to return to menu")
    input()
    os.system('cls')
def outro():
    os.system('cls')
    print("\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\tThank You\n")
    print("\t\t\t\t\t Account Ledger Using Blockchain \n")
    print(" \t\t\t\t\t\t\t\t By ")
    print(" \t\t\t\t\t\t\t\t    Kavin M- 19PD18")
    print(" \t\t\t\t\t\t\t\t    Sai Karthik R- 19PD28")
    time.sleep(5)
    os.system('cls')
if __name__ == '__main__':
    intro()
    x=int(1)
    while True: 
        print("\n\n\n\n\n\n\n\n\n\n\n")
        print("\t\t\t\t\tPress 1 to Create Account\n")
        print("\t\t\t\t\tPress 2 to Add New Transaction\n")
        print("\t\t\t\t\tPress 3 to View All Transactions\n")
        print("\t\t\t\t\tPress 4 to Exit\n")
        x=int(input())
        if x==1:
            newaccount()
        elif x==2:
            add_transaction()
        elif x==3:
            view_transaction()
        elif x==4:
            outro()
        else:
            print("Incorrect input. \nEnter again. \n")
            time.sleep(3)
            
        