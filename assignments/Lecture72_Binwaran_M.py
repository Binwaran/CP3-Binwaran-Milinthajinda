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
        menuPrice = input("Price: ")
        menuList.append([menuName,menuPrice])

showBill()