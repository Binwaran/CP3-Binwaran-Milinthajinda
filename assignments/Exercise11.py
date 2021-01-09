inputNumber = int(input("Number:"))
bank = " "
for i in range(inputNumber):
    christmasStar = (bank*(inputNumber-(i-1))+("*"*(2*i+1)))
    print(christmasStar)
