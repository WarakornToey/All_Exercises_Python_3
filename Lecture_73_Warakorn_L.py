systemMenu = {"ไก่ทอด": 35,"เป็ดทอด": 45,"ปลาทอด": 55,"ผักทอด": 20}
menuList =[]
def showBill():
    total = 0
    print("-----TorToey Food Shop-----")
    for number in range(len(menuList)) :
        print(menuList[number])
        total += int(menuList[number][1])
    print ("Total :", total)

while True:
    menuName = input("Please Enter Menu : ")
    if (menuName.lower() == 'exit'):
        break
    else:
        menuList.append([menuName,systemMenu[menuName]])
showBill()