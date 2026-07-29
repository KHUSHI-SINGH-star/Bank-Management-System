from bank import Bank

user = Bank()

while True:

    print("\n" + "=" * 50)
    print("        WELCOME TO BANK MANAGEMENT SYSTEM")
    print("=" * 50)

    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Account Details")
    print("5. Update Account Details")
    print("6. Delete Account")
    print("7. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        user.CreatAccount()

    elif choice == "2":
        user.Depositemoney()

    elif choice == "3":
        user.Withdrawmoney()

    elif choice == "4":
        user.details()

    elif choice == "5":
        user.Updatedetails()

    elif choice == "6":
        user.delete()

    elif choice == "7":
        print("\nThank you for using our Bank Management System.")
        print("Have a Nice Day!")
        break

    else:
        print("\nInvalid Choice! Please try again.")

    input("\nPress Enter to continue...")