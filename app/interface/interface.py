from app.interface.costumerPanel import costumerPanel



while True:
    print("1. Costumer")
    print("2. Admin")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        costumerPanel()
    elif choice == "2":
        pass
    elif choice == "3":
        break
    else:
        print("Invalid choice")