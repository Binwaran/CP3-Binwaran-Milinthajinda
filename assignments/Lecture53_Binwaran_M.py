def vatCalculate(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result
price = int(input("Please enter price: "))
print("Price includeing Vat is: ",vatCalculate(price))