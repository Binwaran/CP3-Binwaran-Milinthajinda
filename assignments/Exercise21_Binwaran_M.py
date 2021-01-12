from tkinter import *
import math

def leftClickButton(event):
    Weight = float(textBoxWeight.get())
    Height = float(textBoxHeight.get())
    BMI = Weight/math.pow(Height/100,2)
    print(BMI)
    labelresult.configure(text=BMI)
    if BMI >= 30:
        labelCaption.configure(text="ค่า BMI 30 ขึ้นไป อยูในเกณฑ์: อ้วนมาก",fg="#000000",bg="#fc0303")
    elif BMI >= 25 and BMI < 30:
        labelCaption.configure(text="ค่า BMI 25.0 - 29.9 อยูในเกณฑ์: อ้วน",fg="#000000",bg="#fcad03")
    elif BMI >= 23 and BMI < 25:
        labelCaption.configure(text="ค่า BMI 23.0 - 24.9 อยูในเกณฑ์: น้ำหนักเกิน",fg="#000000",bg="#fcfc03")
    elif BMI >= 18.6 and BMI < 23:
        labelCaption.configure(text="ค่า BMI 18.6 - 22.9 อยูในเกณฑ์: น้ำหนักปกติ",fg="#000000",bg="#62fc03")
    else:
        labelCaption.configure(text="ค่า BMI 18.5 อยูในเกณฑ์: ผอมเกินไป",fg="#000000",bg="#f403fc")



mainWindow = Tk()
labelHeight = Label(mainWindow,text="ส่วนสูง(cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(mainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeight = Label(mainWindow,text="น้ำหนัก(kg.)")
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(mainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(mainWindow,text="คำนวณ BMI")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=2,column=0)
labelresult= Label(mainWindow,text="แสดงค่า BMI")
labelresult.grid(row=2,column=1)
labelCaption = Label(mainWindow, text="คุณอยู่ในเกณฑ์ใด")
labelCaption.grid(row=3, column=1)

mainWindow.mainloop()