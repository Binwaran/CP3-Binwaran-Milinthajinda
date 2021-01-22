import random
import tkinter
from tkinter import *


foodlist = ['กระเพาหมูสับ', 'ผัดพริกแกง', 'มาม่า']

dessertlist = ["ทับทิมกรอบ", "บัวลอย", "ลอดช่อง"]

drinklist = ["น้ำเปล่า", "ชาเย็น", "ชามะนาว", "ชาดำเย็น"]


def food_button(event):
    foodresult = random.choice(foodlist)
    foodresult_label.configure(foodresult)
def dessert_button(event):
    dessertresult = random.choice(dessertlist)
    dessertresult_label.configure(dessertresult)
def drink_button(event):
    drinkresult = random.choice(drinklist)
    drinkresult_label.configure(drinkresult)


main_window = Tk()


#info label
info_label = Label(main_window, text = "กินอะไรดี", fg = "black", bg = "#bdfff9", font = ("arial", 14))
info_label.grid(row = 0, column = 2)


#Thank you label
info_label = Label(main_window, text = "-ขอบคุณที่ใช้บริการแอพกินอะไรดี-", fg = "black", bg = "#bdfff9", font = ("arial", 14))
info_label.grid(row = 10, column = 2)


#Label function
food_label = Label(main_window, text = "อาหารคาว", fg = "#000000", font = ("arial", 12))
food_label.grid(row = 2, column = 0)
dessert_label = Label(main_window, text = "อาหารหวาน", fg = "#000000", font = ("arial", 12))
dessert_label.grid(row = 5, column = 0)
drink_label = Label(main_window, text = "เครื่องดื่ม", fg = "#000000", font = ("arial", 12))
drink_label.grid(row = 8, column = 0)


#Button function
foodrandom_button = Button(main_window, text = "สุ่มเลือกอาหารคาว", fg = "#000000", font = ("arial", 10))
foodrandom_button.grid(row = 2, column = 2)
foodrandom_button.bind('<Button-1>', food_button)
dessertrandom_button = Button(main_window, text = "สุ่มเลือกอาหารหวาน", fg = "#000000", font = ("arial", 10))
dessertrandom_button.grid(row = 5, column = 2)
dessertrandom_button.bind('<Button-1>', dessert_button)
drinkrandom_button = Button(main_window, text = "สุ่มเลือกเครื่องดื่ม", fg = "#000000", font = ("arial", 10))
drinkrandom_button.grid(row = 8, column = 2)
drinkrandom_button.bind('<Button-1>', drink_button)


#Result
foodresult_label = Label(main_window, text = "ผลลัพธ์อาหารคาวที่แนะนำสำหรับมื้อนี้", fg = "#000000", font = ("arial", 12))
foodresult_label.grid(row = 2, column = 5)
dessertresult_label = Label(main_window, text = "ผลลัพธ์อาหารหวานที่แนะนำสำหรับมื้อนี้", fg = "#000000", font = ("arial", 12))
dessertresult_label.grid(row = 5, column = 5)
drinkresult_label = Label(main_window, text = "ผลลัพธ์เครื่องดื่มที่แนะนำสำหรับมื้อนี้", fg = "#000000", font = ("arial", 12))
drinkresult_label.grid(row = 8, column = 5)

main_window.mainloop()
