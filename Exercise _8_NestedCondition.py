Username = input("UserName : ")
password = input("Password : ")
if Username == "Warakorn" and password == "P@ssw0rd":
    print("**** Welcome To TorToey IT Shop ****")
    print("**** Please Select Order ****")
    print("Item --------------------- Price")
    print("Item 1.Monitor             5,500 (THB)")
    print("Item 2.Ram DDR4 64GB       3,500 (THB)")
    print("Item 3.HDD SSD M2 1TB      4,500 (THB)")
    print("Item 4.NoteBook           35,000 (THB)")
    print("Item 5.Mainboard           6,000 (THB)")
    item = int(input("Please Select Itam : "))
    userselected = 0
    if item == 1:
        userselected = int(input(" How Many Pieces >>> "))
        print("*******************")
        print("Monitor X",userselected,"Total = ",userselected*5500,"THB")
        print("*****ThanK You*****")
    elif item == 2:
        userselected = int(input(" How Many Pieces >>> "))
        print("*******************")
        print("Ram DDR4 64GB X",userselected,"Total = ",userselected*3500,"THB")
        print("*****ThanK You*****")
    elif item == 3:
        userselected = int(input(" How Many Pieces >>> "))
        print("*******************")
        print("HDD SSD M2 1TB X",userselected,"Total = ",userselected*4500,"THB")
        print("*****ThanK You*****")
    elif item == 4:
        userselected = int(input(" How Many Pieces >>> "))
        print("*******************")
        print("Notebook X",userselected,"Total = ",userselected*35000,"THB")
        print("*****ThanK You*****")
    elif item == 5:
        userselected = int(input(" How Many Pieces >>> "))
        print("*******************")
        print("Mainboard X",userselected,"Total = ",userselected*6000,"THB")
        print("*****ThanK You*****")
    else:
        print("Error! Please Check Item Number")
else:
    print("Error! Please Check UserName or Password ")



