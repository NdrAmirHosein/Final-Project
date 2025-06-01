from app.services.generateplate import generatePlate
def userPanel(nationalCode):
    while True:
        print("   ...User Panel...  ")
        print("1. Generate Plate")
        print("2. exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            generatePlate(nationalCode)
        elif choice == "2":
            break