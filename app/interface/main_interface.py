from app.interface.costumerPanel import costumerPanel
from app.interface.admin_interface import adminlogin
from app.Phase4.core import phase4_core

def interface():
    while True:
        print("1. Costumer")
        print("2. Admin")
        print("3. Phase 4")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            costumerPanel()
        elif choice == "2":
            adminlogin()
        elif choice == "3":
            ranked_users = phase4_core()
            for i in range(10):
                print(f"{i+1}. National Code:  {ranked_users[i].national_code},  Score:  {ranked_users[i].score}")
        elif choice == "4":
            break
        else:
            print("Invalid choice")