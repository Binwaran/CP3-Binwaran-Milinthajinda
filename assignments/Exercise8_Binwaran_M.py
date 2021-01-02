usernameInput = input("User Name: ")
passwordInput = input("Password: ")
if usernameInput == "customer" and passwordInput == "1234":
    print("-----eShop-----")
    print("Please select your order")
    print("A.Lay     price: 25 THB")
    print("B.Paprika price: 20 THB")
    print("C.Hanami  price: 18 THB")
    print("D.Oreo    price: 15 THB")
    print("E.Carada  price: 15 THB")
    print("Noted: All products not included Vat")
    userSelected = input("Select products : ")
    amount = int(input("amount : "))
    if userSelected == "A":
        priceA = 25
        vat = 7
        Aprice = (priceA*amount)+(priceA*vat/100)
        print("Total amount: ",Aprice,"THB")
    elif userSelected == "B":
        priceB = 20
        vat = 7
        Bprice = (priceB*amount)+(priceB*vat/100)
        print("Total amount: ",Bprice,"THB")
    elif userSelected == "C":
        priceC = 18
        vat = 7
        Cprice = (priceC*amount)+(priceC*vat/100)
        print("Total amount: ",Cprice,"THB")
    elif userSelected == "D":
        priceD = 15
        vat = 7
        Dprice = (priceD*amount)+(priceD*vat/100)
        print("Total amount: ",Dprice,"THB")
    elif userSelected == "E":
        priceE = 18
        vat = 7
        Eprice = (priceE*amount)+(priceE*vat/100)
        print("Total amount: ",Eprice,"THB")
else: print("Error")





