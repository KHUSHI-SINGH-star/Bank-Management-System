import json
import random
import string
from pathlib import Path


class Bank:
    database = "data.json"
    data = []


    try:
        if Path(database).exists():
            with open(database, "r") as fs:
                data = json.load(fs)
        else:
            with open(database, "w") as fs:
                json.dump([], fs)
            data = []

    except json.JSONDecodeError:
        data = []

    # ---------------- Save Data ---------------- #

    @classmethod
    def __update(cls):
        with open(cls.database, "w") as fs:
            json.dump(cls.data, fs, indent=4)

    # ---------------- Generate Account ---------------- #

    @classmethod
    def __accountgenerate(cls):

        while True:

            account = (
                "".join(random.choices(string.ascii_uppercase, k=3))
                + "".join(random.choices(string.digits, k=4))
            )

            exist = any(user["accountNo"] == account for user in cls.data)

            if not exist:
                return account

   
    def find_user(self):

        accnumber = input("Enter Account Number : ")

        pin = input("Enter 4 Digit PIN : ")

        if not pin.isdigit():
            print("Invalid PIN")
            return None

        pin = int(pin)

        for user in Bank.data:

            if user["accountNo"] == accnumber and user["Pin"] == pin:
                return user

        print("Invalid Account Number or PIN")
        return None

    

    def CreatAccount(self):

        name = input("Enter Name : ").strip()

        try:
            age = int(input("Enter Age : "))
        except:
            print("Invalid Age")
            return

        email = input("Enter Email : ").strip()

        pin = input("Enter 4 Digit PIN : ")

        if age < 18:
            print("Age must be at least 18.")
            return

        if "@" not in email or "." not in email:
            print("Invalid Email")
            return

        if not pin.isdigit() or len(pin) != 4:
            print("PIN must contain exactly 4 digits.")
            return

        for user in Bank.data:
            if user["Email"] == email:
                print("Email already exists.")
                return

        info = {
            "Name": name,
            "Age": age,
            "Email": email,
            "Pin": int(pin),
            "accountNo": Bank.__accountgenerate(),
            "Balance": 0,
        }

        Bank.data.append(info)

        Bank.__update()

        print("\nAccount Created Successfully\n")

        for key, value in info.items():
            print(f"{key} : {value}")

        print("\nPlease save your Account Number.\n")

   

    def Depositemoney(self):

        user = self.find_user()

        if user is None:
            return

        try:
            amount = int(input("Enter Amount : "))
        except:
            print("Invalid Amount")
            return

        if amount <= 0:
            print("Amount must be greater than 0")
            return

        if amount > 10000:
            print("Maximum deposit limit is 10000")
            return

        user["Balance"] += amount

        Bank.__update()

        print("Money Deposited Successfully")

        print("Current Balance :", user["Balance"])

    

    def Withdrawmoney(self):

        user = self.find_user()

        if user is None:
            return

        try:
            amount = int(input("Enter Amount : "))
        except:
            print("Invalid Amount")
            return

        if amount <= 0:
            print("Invalid Amount")
            return

        if amount > user["Balance"]:
            print("Insufficient Balance")
            return

        user["Balance"] -= amount

        Bank.__update()

        print("Money Withdrawn Successfully")

        print("Remaining Balance :", user["Balance"])

   
    def details(self):

        user = self.find_user()

        if user is None:
            return

        print("\n------ Account Details ------\n")

        for key, value in user.items():
            print(f"{key} : {value}")

    
            

    def Updatedetails(self):

        user = self.find_user()

        if user is None:
            return

        print("\nLeave field blank if you don't want to change it.\n")

        name = input("New Name : ").strip()

        email = input("New Email : ").strip()

        pin = input("New PIN : ").strip()

        if name:
            user["Name"] = name

        if email:

            if "@" not in email or "." not in email:
                print("Invalid Email")
                return

            user["Email"] = email

        if pin:

            if not pin.isdigit() or len(pin) != 4:
                print("PIN must contain exactly 4 digits")
                return

            user["Pin"] = int(pin)

        Bank.__update()

        print("Details Updated Successfully")

  

    def delete(self):

        user = self.find_user()

        if user is None:
            return

        choice = input("Type YES to delete account : ")

        if choice.upper() == "YES":

            Bank.data.remove(user)

            Bank.__update()

            print("Account Deleted Successfully")

        else:

            print("Deletion Cancelled")
