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
        menuPrice = input("Please Enter Price : ")
        menuList.append([menuName,menuPrice])


showBill()