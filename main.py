import json
import random
from pathlib import Path
import string

class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database,'r') as fs:
                data = json.loads(fs.read())
        else:
            print("database does not exist.")
    except Exception as err:
        print(f"Error {err} occured..")

    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountnumgen(cls):
        char = random.choices(string.ascii_letters,k=4)
        digits = random.choices(string.digits,k=3)
        spchar = random.choices("@$#%&^*",k=1)
        unum = char + digits + spchar
        random.shuffle(unum)
        return "".join(unum)

    def Createaccount(self):
        info = {
            "name" : input("enter your name: "),
            "age" : int(input("enter your age: ")),
            "email":input("enter your email id: "),
            "pin":input("enter your 4 digit pin: "),
            "account":Bank.__accountnumgen(),
            "balance": 0
        }
        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print("your account cannot be created!")
        else:
            print("ACCOUNT CREATED SUCCESFULLY.")
            for i in info:
                print(f"{i} : {info[i]}")
            print("Note your details.")
            Bank.data.append(info)
            Bank.__update()

    def depositmoney(self):
        acc = input("Enter your account number: ")
        pin = input("Enter your account pin: ")

        userdata = [i for i in Bank.data if i['account']==acc and i['pin']==pin]

        if userdata== False:
            print("No data found!")

        else:
            amount = int(input("Enter amount to deposit"))
            if amount>=10000 or amount<0:
                print("Sorry cannot deposit!")
            else:
                userdata[0]['balance']+=amount
                Bank.__update()
                print("Deposit Successful!")

    def withdrawmoney(self):
        acc = input("Enter your account number: ")
        pin = input("Enter your account pin: ")
        
        userdata = [i for i in Bank.data if i['account']==acc and i['pin']==pin]
        
        if userdata== False:
            print("No details found!")
        
        else:
            amount = int(input("Enter amount to withdraw: "))
            if amount>userdata[0]['balance']:
                print("Sorry cannot withdraw!")
            else:
                userdata[0]['balance']-=amount
                Bank.__update()
                print("Withdraw Successful!")

    def showdetails(self):
        acc = input("Enter your account number: ")
        pin = input("Enter your account pin: ")
                
        userdata = [i for i in Bank.data if i['account']==acc and i['pin']==pin]
                
        if userdata== False:
            print("No details found!")
        else:
            print("your information are \n\n")
            for i in userdata[0]:
                print(f"{i} : {userdata[0][i]}")


    def updatedetails(self):
        acc = input("Enter your account number: ")
        pin = input("Enter your account pin: ")
                
        userdata = [i for i in Bank.data if i['account']==acc and i['pin']==pin]
                
        if userdata== False:
            print("No details found!")
                
        else:
            print("age, balance and account number cannot be changed..")
            print("fill the details here:")
            newdata = {
                "name" : input("update name here (or press enter to skip): "),
                "pin": input("Enter new pin here (or press enter to skip): "),
                "email":input("Enter new email here (or press enter to skip): ")
            }
            if newdata['name']=="":
                newdata['name']=userdata[0]['name']
            if newdata['pin']=="":
                newdata['name']=userdata[0]['pin']
            if newdata['name']=="":
                newdata['email']=userdata[0]['email']

            newdata['age']=userdata[0]['age']
            newdata['balance']=userdata[0]['balance']
            newdata['account']=userdata[0]['account']

            if type(newdata['pin'])==str:
                newdata['pin'] = int(newdata['pin'])

            for i in newdata:
                if newdata[i]==userdata[0][i]:
                    continue
                else:
                    userdata[0][i]=newdata[i]

            Bank.__update()
            print("Details updated Successfully")

    def Delete(self):
        acc = input("Enter your account number: ")
        pin = input("Enter your account pin: ")
                        
        userdata = [i for i in Bank.data if i['account']==acc and i['pin']==pin]
                        
        if userdata== False:
            print("No details found!")
                        
        else: 
            index = Bank.data.index(userdata[0])
            Bank.data.pop(index)
            Bank.__update()
            print("ACCOUNT DELETED SUCCESSFULLY!")

user = Bank()
print("press 1 for creating an account")
print("press 2 for Deposititing the money in the bank ")
print("press 3 for withdrawing the money ")
print("press 4 for details ")
print("press 5 for updating the details")
print("press 6 for deleting your account")

check = int(input("tell your response :- "))

if check == 1:
    user.Createaccount()

if check == 2:
    user.depositmoney()

if check == 3:
    user.withdrawmoney()

if check == 4:
    user.showdetails()

if check == 5:
    user.updatedetails()

if check == 6:
    user.Delete()