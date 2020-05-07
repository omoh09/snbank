

database = ''
session = []
data = []
from random import randint
import time
import json
import datetime
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

class SavingsAcct():

    def welcome(self):
        print("**************************")
        print("|   Welcome to SNHBank   |")
        print("**************************")
        print('''Enter 1 for staff login  |
Enter 2 to close App     |''')
        print("--------------------------")
        print()
        try:
            ask = int(input('Enter a choice: '))
            if ask == 1:
                self.login(self)
            elif ask == 2:
                print('Thanks for using this app, BYE')
                quit()
            else:
                self.welcome(self)
        
        except ValueError:
            print("Invalid input, follow instructions.")
            self.welcome(self)
            
    def login(self):
        Username = str(input("Enter username: "))
        passw = str(input("Enter password: "))
        with open('staff.txt') as jon_file:  
            data = json.load(jon_file)
            for p in data['staff']:
                if p["username"] == Username:
                    if p["password"] == passw:
                        open('session.txt', 'w')
                        database = open('session.txt', 'a')
                        session = [p['fullname'], Username, st]
                        database.write(str(session)+'\n')
                        database.close()
                        print("_____________________________________________")
                        print('Welcome ' + p['fullname'].upper()+ ' to your staff Dashboard   ') 
                        print("---------------------------------------------")
                        return self.action(SavingsAcct, Username)
                else:
                    print('Invalid login, try Again')
                    return self.login(SavingsAcct)

    def createUser(self, Username):
        print("*********************")
        print('Cheers '+ Username)  
        print("*********************")
        accountname = str(input("Account Name: "))
        database = open('customer.txt', 'a')
        database.write(str(accountname)+' ')
        database.close()
        openingbalance = int(input("Opening Balance: "))
        database = open('customer.txt', 'a')
        database.write(str(openingbalance)+' ')
        database.close()
        accounttype = str(input("Account Type: "))
        database = open('customer.txt', 'a')
        database.write(str(accounttype)+' ')
        database.close()
        accountemail = str(input("Account Email: "))
        database = open('customer.txt', 'a')
        database.write(str(accountemail)+' ')
        database.close()
        accountnumber = randint(1000000000, 9999999999)
        database = open('customer.txt', 'a')
        database.write(str(accountnumber)+' ')
        database.close()
        print("Account Number: " + str(accountnumber))
        print('Your Account ' + str(accountname) + ' Has been succesfully Created ' + str(accountnumber))
        print("_____________________________________________")
        return SavingsAcct.action(SavingsAcct, Username)

    def checkAccount(self, Username):
        print("*********************")
        print('Cheers '+ Username)  
        print("*********************")
        try:
            accountno = int(input("Enter an account number: "))
            database=open('customer.txt','r').read()
            if str(accountno) in database:
                database=open('customer.txt','r').readlines()
                details = ["Name","Account opening","Account type","Email", "Account number"]
                for i in zip(details, database):
                    print(i)
                    print("_____________________________________________")
                return SavingsAcct.action(SavingsAcct, Username)
            else:
                print("_____________________________________________")
                self.checkAccount(SavingsAcct,Username)
        except ValueError:
            print("Invalid account number, try again.")
            print("_____________________________________________")
            self.checkAccount(SavingsAcct,Username)

    def action(self, Username):
        print('''Enter 1 Create new bank account                     
Enter 2 Check Account Details
Enter 3 to Logout                                    ''')
        print("_____________________________________________")
        print()
        try:
            action = int(input('>>>>>: '))
            if action == 3:
                import os
                if os.path.exists("session.txt"):
                    os.remove("session.txt")
                
                for i in range(1):
                    print("Logining out...")
                    print('''Taking your back to the main menu in...\n...3''')
                    time.sleep(2)
                    print('...2')
                    time.sleep(2)
                    print('...1')
                    time.sleep(2)
                    SavingsAcct.welcome(self)
            elif action == 1:
                SavingsAcct.createUser(SavingsAcct, Username)
            elif action == 2:
                self.checkAccount(SavingsAcct,Username)
            else:
                print('Invalid Command')
                return SavingsAcct.action(SavingsAcct, Username)
        except ValueError:
            print("Invalid input, follow instructions.")
            SavingsAcct.action(SavingsAcct, Username)

SavingsAcct.welcome(SavingsAcct)
