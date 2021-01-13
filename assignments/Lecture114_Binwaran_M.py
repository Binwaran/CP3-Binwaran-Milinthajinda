from tkinter import *
from tkinter import ttk
from forex_python.converter import CurrencyRates


currency_rate = CurrencyRates()


def LeftClickButton(event):
    result = (currency_rate.convert(first_currency_box.get(), second_currency_box.get(), float(first_currency_amount.get())))
    result_label.configure(text = ("Result = %.2f") % (result))



main_window = Tk()

# Info Label
info_label = Label(main_window, text = "Welcome to Currency Converter", fg = "black", bg = "#bdfff9", font = ("arial", 14))
info_label.grid(row = 0, column = 1)


# First Currency
first_currency_label = Label(main_window, text = "First Currency")
first_currency_label.grid(row = 1 , column = 0)
first_currency_box = ttk.Combobox(main_window)
first_currency_box['values'] = list(currency_rate.get_rates("").keys())
first_currency_box.current(29)
first_currency_box.bind("<<ComboboxSelected>>")
first_currency_box.grid(row = 2 , column = 0)
amount_label = Label(main_window, text = "Please Enter Amount")
amount_label.grid(row = 4 , column = 0)
first_currency_amount = Entry(main_window)
first_currency_amount.grid(row = 5 , column = 0)


# Convert text
convert_label = Label(main_window, text = "Convert to")
convert_label.grid(row = 2 , column = 1)


# Second currency
second_currency_label = Label(main_window, text = "Second Currency")
second_currency_label.grid(row = 1 , column = 3)
second_currency_box = ttk.Combobox(main_window)
second_currency_box["values"] = list(currency_rate.get_rates("").keys())
second_currency_box.current(10)
second_currency_box.bind("<<ComboboxSelected>>")
second_currency_box.grid(row = 2 , column = 3)


# Convert Button
convert_button = Button(main_window, text = "Convert", width = 20, height = 2, bg = "#baa3ff")
convert_button.bind('<Button-1>', LeftClickButton)
convert_button.grid(row = 5 , column = 1)


# Result
result_label = Label(main_window, text = "Result", fg = "black", bg = "#dcffbd", font = ("arial", 10))
result_label.grid(row = 5 , column = 3)


main_window.mainloop()