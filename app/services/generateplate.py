from app.handler.generatePlate import check_cityCode

def generatePlate():
    try:
        print("11 | Tehran\n22 | Mashhad\n31 | Isfahan\n44 | Tabriz\n51 | Shiraz\n61 | Ahvaz\n71 | Qom\n81 | Kermanshah\n91 | Urmia")
        cityCode = input("Enter Your City Code: ")
        print(check_cityCode(cityCode))
            
    except ValueError as e:
        print(e)