def login():
    usernameInput = input("Username:")
    passwordInput = input("Password:")
    if usernameInput == "admin" and passwordInput == "123456":
        print("---Welcome to iShop!---")
        return showMenu()
    else:
        print("Please try again")
        return login()
def showMenu():
    print("-----iShop-----")
    print("1.Vat Calculator")
    print("2.Price Calculator")
    return selectMenu()
def selectMenu():
    userSelected = int(input(">>"))
    if userSelected == 1:
        price = int(input("Pleas enter the price: "))
        return vatCalculate(price)
    else:
        userSelected == 2
        return priceCalculate()

def vatCalculate(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return print(result)

def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("First Product Price : "))
    return vatCalculate(price1 + price2)

login()