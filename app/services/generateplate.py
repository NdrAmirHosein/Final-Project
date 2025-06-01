from app.handler.generatePlate import check_cityCode_and_set_Plate

def generatePlate(nationalCode):
    try:
        print("11 | Tehran\n22 | Mashhad\n31 | Isfahan\n44 | Tabriz\n51 | Shiraz\n61 | Ahvaz\n71 | Qom\n81 | Kermanshah\n91 | Urmia")
        cityCode = input("Enter Your City Code: ")
        print(f"\nPlate generated successfully: {check_cityCode_and_set_Plate(cityCode, nationalCode)}\n")
            
    except ValueError as e:
        print(e)