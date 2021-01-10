systemMenu = {"ข้าวมันไก่":40,"ข้าวหมกไก่":45,"ข้าวมันไก่ทอด":45,"ข้าวมันไก่ผสม":50}
menuList = []
def showBill():
    totalPrice = 0
    textShop = ("My Shop")
    print(textShop.center(21,"-"))
    for number in range(len(menuList)):
        print(menuList[number])
        totalPrice += int(menuList[number][1])
    print("Total price",totalPrice,"THB")


while True:
    menuName = input("Please Enter Menu: ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName,systemMenu[menuName]])

showBill()