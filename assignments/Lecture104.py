class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Add product to ",self.name,self.lastName,"'s cart")

customer1 = Customer()
customer1.name ="Binwaran"
customer1.lastName = "M"
customer1.addCart()

customer2 = Customer()
customer2.name ="Dang"
customer2.lastName = "N"
customer2.addCart()

customer3 = Customer()
customer3.name ="Kob"
customer3.lastName = "O"
customer3.addCart()

customer4 = Customer()
customer4.name ="Kai"
customer4.lastName = "R"
customer4.addCart()