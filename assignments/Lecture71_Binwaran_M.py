menuList = []
pricelist = []

def showBill():
    totalPrice = 0
    print("----My Shop----")
    for number in range(len(menuList)):
        print(menuList[number], pricelist[number])
        totalPrice += int(pricelist[number])
    print("Total Price : ",totalPrice,"THB")

while True:
    menuName = input("Please Enter Menu : ")
    if(menuName.lower()=="exit"):
        break
    else:
        menuPrice = input("Price : ")
        menuList.append(menuName)
        pricelist.append(menuPrice)
showBill()

